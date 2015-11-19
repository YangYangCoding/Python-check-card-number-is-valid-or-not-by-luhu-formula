#!/usr/bin/python

# check if the credit card number is valid or not by using luhn formula.
# write by Yang Yang for python learning

import sys, re

def luhn_checksum(number):
	checksum = 0
	rever_num = reversed(number) # reverse the number
	for (index,digit) in enumerate(rever_num):

		if index % 2 != 0:
			index_sum = int(digit) * 2 # double the digit for every second most right digit
			if index_sum > 9:
				index_sum = index_sum % 10 + 1 # cal the sum for double digit, like: 8*2 = 16, sum == 1 + 6 =7.
			checksum += index_sum
		else:
			checksum += int(digit)
	return checksum

def validation(card_num):
	if len(card_num) != 16:
		print card_num + " is not 16 digits number, it is invalid."
	else:
		reminder = luhn_checksum(card_num) % 10
		if reminder == 0:
			print card_num + " is valid."
		else:
			print card_num + " is invalid."
		

	
if __name__ == "__main__":
	for arg in sys.argv[1:]:
		validation(arg)

		
		
