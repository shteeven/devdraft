# import sys
#
# class Address:
#
# 	def __init__(self, addressLine):
# 		self.addressLine = addressLine
#
# 	def getStreetAddress(self):
# 		#take everything before the first comma
# 		return self.addressLine.split(",")[0].strip()
#
# 	def getCityName(self):
# 		#the city appears after the first comma
# 		return self.addressLine.split(",")[-2].strip()
#
# 	def getState(self):
# 		#state appears after 2 commas
# 		stateLine = self.addressLine.split(",")[-1].strip()
# 		return stateLine.split(" ")[0].strip().lower()
#
# 	def getZipCode(self):
# 		#zip is last element
# 		stateLine = self.addressLine.split(",")[-1].strip()
# 		return int(stateLine.split(" ")[1].strip())
#
#
# class TaxCalculator:
#
# 	@staticmethod
# 	def calculateTax(orderAmount, state):
# 		if state == "arizona" or state == "az":
# 			return orderAmount / 100 * 5
# 		if state == "washington" or state == "wa":
# 			return orderAmount / 100 * 9
# 		if state == "california" or state == "ca":
# 			return orderAmount / 100 * 6
# 		if state == "delaware" or state == "de":
# 			return 0
# 		return orderAmount / 100 * 7
#
# class ShippingCalculator:
#
# 	@staticmethod
# 	def calculateShipping(zipCode):
# 		if zipCode > 75000:
# 			return 10
# 		elif zipCode >= 25000:
# 			return 20
# 		else:
# 			return 30
#
#
# #main
# numTestCases = int(sys.stdin.readline().strip())
#
# for i in range(numTestCases):
# 	basePrice = int(sys.stdin.readline().strip())
# 	addressString = sys.stdin.readline().strip()
# 	addr = Address(addressString)
#
# 	taxAmount = TaxCalculator.calculateTax(basePrice, addr.getState())
# 	shippingAmount = ShippingCalculator.calculateShipping(addr.getZipCode())
#
# 	print (basePrice + taxAmount + shippingAmount)

import sys


def cascade(index, true_index, reach_list):
    current_domino = reach_list[index]
    if current_domino == 0:
        return true_index
    end = index + current_domino
    if end > 0:
        reach_values = reach_list[index:] + [current_domino + true_index]
    else:
        reach_values = reach_list[index:index + current_domino + 1] + [current_domino + true_index]
    result = max(reach_values)
    return result  # return greatest cascade+offset


def iterate_dominoes(num_dominoes, domino_heights):
    for i in range(num_dominoes):
        x = (i + 1) * -1  # x provides a neg int so that indexes start at end
        true_index = num_dominoes + x
        domino_heights[x] = cascade(x, true_index, domino_heights)

    for i in range(num_dominoes):
        domino_heights[i] -= i
    return domino_heights

# retrieve system arguments
num_dominoes = int(sys.stdin.readline())
dominoes = sys.stdin.readline()

right = [int(x) for x in dominoes.split()]
left = right[::-1]

# get results from both cascades
result_right = iterate_dominoes(num_dominoes, right)
result_left = iterate_dominoes(num_dominoes, left)[::-1]

# output
write = sys.stdout.write
write(" ".join(str(x) for x in result_right) + '\n')
write(" ".join(str(x) for x in result_left))
