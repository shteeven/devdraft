import sys

class Address:

	def __init__(self, addressLine):
		self.addressLine = addressLine

	def getStreetAddress(self):
		#take everything before the first comma
		return self.addressLine.split(",")[0].strip()

	def getCityName(self):
		#the city appears after the first comma
		return self.addressLine.split(",")[-2].strip()

	def getState(self):
		#state appears after 2 commas
		stateLine = self.addressLine.split(",")[-1].strip()
		return stateLine.split(" ")[0].strip().lower()

	def getZipCode(self):
		#zip is last element
		stateLine = self.addressLine.split(",")[-1].strip()
		return int(stateLine.split(" ")[1].strip())


class TaxCalculator:

	@staticmethod
	def calculateTax(orderAmount, state):
		if state == "arizona" or state == "az":
			return orderAmount / 100 * 5
		if state == "washington" or state == "wa":
			return orderAmount / 100 * 9
		if state == "california" or state == "ca":
			return orderAmount / 100 * 6
		if state == "delaware" or state == "de":
			return 0
		return orderAmount / 100 * 7

class ShippingCalculator:

	@staticmethod
	def calculateShipping(zipCode):
		if zipCode > 75000:
			return 10
		elif zipCode >= 25000:
			return 20
		else:
			return 30


#main
numTestCases = int(sys.stdin.readline().strip())

for i in range(numTestCases):
	basePrice = int(sys.stdin.readline().strip())
	addressString = sys.stdin.readline().strip()
	addr = Address(addressString)

	taxAmount = TaxCalculator.calculateTax(basePrice, addr.getState())
	shippingAmount = ShippingCalculator.calculateShipping(addr.getZipCode())

	print (basePrice + taxAmount + shippingAmount)