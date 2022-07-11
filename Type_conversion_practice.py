# Type conversions

# num_char = len(input("What is your name?"))
# new_num_char = str(num_char)
# print("Your name has " + new_num_char + " characters.")


# a = float(123)
# print(type(a))

# print(70 + float("100.5"))
# # output will be 170.5 because we converted from string to a float and then added to seventy

# print(str(70) + str(100))
# Will print 70100

##########################################################################################################################
# Write a program that adds the digits in a 2 digit number. e.g. if the input was 35, then the output should be 3 + 5 = 8

two_digit_number = input("Type a two digit number: ")
first_digit = two_digit_number[0]
second_digit = two_digit_number[1]
result = int(first_digit) + int(second_digit)
print(result)