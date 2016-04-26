#
# Create a menu and ask the user which of the following conversions they wish to perform:
# a. Miles to kilometers
# b. Gallons to liters
# c. Dollars to GBP
# d. Pounds to kilograms
# e. Inches to centimeters
# f. Fahrenheit to Celsius
#
# 2. Your program must raise an exception if the user chooses any item not on the menu presented. Along with raising an exception, write the code to handle this exception. (LO 5)
#
# 3. Once the user has chosen a menu item the program should:
#
# a. Ask the user for a value to convert. Refer to the input validations in Lab 3. Your program must raise and exception, and handle the exception, if an input errors occurs. (LO 5)
#
# b. Perform the conversion and write the original value, the original unit, the converted value, and the converted unit to an output file named conversions.txt. (LO 1, 3)
#
# c. Repeat steps a and b 4 times (in a loop).


## validate inputs and catch errors
def validateInput(data, type):
    ## give user 3 attempts
    for x in range(3):
        i = str(x + 1)  # offset attempts by one
        ## what type of data are we trying to parse
        if type == 'float':
            try:
                data = float(data)
                return data
            except ValueError:
                data = raw_input('Value was not a floating point; please try again: (attempt: ' + i + ')')
        elif type == 'int':
            try:
                data = int(data)
                return data
            except ValueError:
                data = raw_input('Value was not a integer; please try again: (attempt: ' + i + ')')
        else:
            ## default is to return a string value
            return data
    print("Sorry, but you entered an incorrect value too many times.")
    exit(1)


# Define all conversion functions here
def milesToKilometers():
    miles = validateInput(raw_input('Please enter number of miles:'), 'float')
    # return list is original val, oringinal unit, new val, new unit
    return [miles, 'miles', miles * 1.6, 'kilometers']

def poundsToKilogram():
    pounds = validateInput(raw_input('Please enter number of pounds:'), 'float')
    return [pounds, 'pounds', pounds * 2.2, 'kilograms']


# decide what function to run
def selectFunction(choice):
    try:
        # return the function the user picked
        # make sure to register conversion functions here
        return {
            'a': milesToKilometers,
            'd': poundsToKilogram
        }[choice]
    except KeyError:
        print('The select option you selected was invalid.')
        exit(1)


# main function take input
def main():
    print('Welcome! Please select a conversion:')
    print('"a" for miles to kilometers')
    print('"b" for gallons to liters')
    print('"c" for dollars to GBP')
    print('"d" for pounds to kilograms')
    print('"e" for inches to centimeters')
    print('"f" for fahrenheit to Celsius')
    # select a function and fire it off immediately
    returnValues = selectFunction(raw_input())()

    print('The result is ' + str(returnValues[2]) + ' ' + returnValues[3])
    return returnValues


f = open('workfile', 'w')
# is this what she meant about running it 4 times?
for i in range(4):
    toWrite = main()
    # make list a string so it can be written to file
    print(toWrite)
    # write to file and add a 'newline' character to the line
    toWrite = str(toWrite) + '\n'
    print(toWrite)
    f.write(toWrite)
f.close()
