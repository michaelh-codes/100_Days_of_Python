#   Day 2 of Python
#   By the end of the day, we will be able to build a tip calculator which can split the bill and change tip percentage.

#   len() is used to get the length of a text String

#   Data Types
#   Today we will learn about these basic data types:

#   Strings
#       String of characters "Hello"
#       Can add brackets "Hello"[0] - shows the first letter of a string, first always starts with 0.
#       This process is called "Subscripting"
#       Anything inside quotes is a String, therefore "123" will not be counted as a number.

#   Itegers
#       Numbers without decimal places
#       ex. print(123 + 345)
#       ot. 468
#       In large numbers, commas are replaced with underscores
#       ex. 1,000,000 becomes 1_000_000
#       Computer ignores these underscores, but increases readability.

#   Floats
#       Floating point number
#       Numbers with decimal places

#   Booleans
#       Two values:
#       True or False
#       No quotes or anything around the word.

#   Video Challenge:
#   Change this code to print the small o.
#   print("Hello"[0])

#   Video Challenge Solution:
print("print('Hello[4]')")
print("Hello"[4])


print("\n")
#   Type function
#   Use type() to check the type of data you are working with.

num_char = len(input("What is your name?"))
#   Converts the integer to a String
new_num_char = str(num_char)

#   This line of code will produce a Type error without adding the str(num_char) variable
print("Your name has " + new_num_char + " characters.")
print("num_char Type")
print(type(num_char))
print("new_num_char Type")
print(type(new_num_char))

print("\n")
print("Data Type Examples")

a = 123
print("the variable is set as a = 123")
print(type(a))

b = "123"
print("the variable is set as b = '123'")
print(type(b))

c = float(123)
print("the variable is set as c = float(123)")
print(type(c))

print("\n")

print("Different examples of data converstions in code:")
print("print(70 + float('100.5')")
print("Output: 170.5")
print("print(str(70) + str(100))")
print("Output: 70100")

print("\n")



#   Challenge 1 - Data types
#   Create a code that takes a two digit number and adds them together. Example below.

#   Type a two digit number: 26
#   8

print("Challenge 1: Data Types - Add any two digit number together.")

user_num = input("Type a two digit number:")
num1 = user_num[0]
num2 = user_num[1]
print(int(num1) + (int(num2)))

print("\n")

print("Different mathmatical operations using Python")
print("3 + 5 is used for addition\n7 - 4 is used for subtraction\n3 * 2 is used for multiplication\n6 / 3 is used for division and will always produce a floating number\n2 ** 2 is used for exponents or 'the power' of a number\n")
print("Using math in Python on the same line of code will follow PEMDAS from left to right:\nParentheses\nExponenets\nMultiplication\nDivision\nAddition\nSubtraction\n")
print("print(3 * 3 + 3 / 3 - 3)")
print("7.0 - Outputs a floating number because of the division\n")

print("Video Challenge - Change the code so it outputs 3")
print("print(3 * (3 + 3) / 3 - 3)")
print("3.0\n")


#   Challenge 2 - BMI calculator
#   Create a code that takes someones weight and height and converts them into their BMI. BMI = Weight(kg)/Height^2(m^2)
#   Convert the result to a whole number

print("Challenge 2: BMI Calculator - User inputs weight and height to calculate their BMI")

height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

height_squared = float(height) ** 2
bmi = float(weight) / float(height_squared)
print(int(bmi))

print("\n")

#   The round() function can be used to round numbers to the nearest whole number. ie 4.5 to 5 and 4.4 to 4.
print("Using the round() function\nprint(round(8/3))")
print(round(8/3))

print("\n")
#   Specify the number of decimal places
print("Use a comma in the round() function to speciy the number of decimal places, example:\nprint(round(8/3, 2))")
print(round(8/3, 2))

print("\n")

#   Floor division
print("Use floor division by using // in code.\nExample: print(8 // 3) will convert the output as a interger, avoiding the floating number all together\nprint(8 // 3)")
print(8 // 3)

print("\n")

#   f Strings
#can be used to incorporate code in a string.

score = 0
height = 1.8
isWinning = True

print('print(f"your score is {score}, your height is {height}, you are winning is {isWinning}")\n\n')

#   Challenge 3: Life in Weeks
#   Create a program using maths and f-Strings that tells us how many days, weeks, and months we have if we live until 90 years old.
#   It will take your current age as the input and output a message with our time left in this format:
#   You have x days, y weeks, and z months left

print("Challenge 3: Life in Weeks\nCreate a program that calculates how many days, weeks, and months a user has left assuming they live until 90.")

age = input("What is your current age?")

years = int(90) - int(age)
months = years * int(12)
weeks = years * int (52)
days = years * int(365)

print(f"You have {days} days, {weeks} weeks, and {months} months left.\n")

#   Day 2 Project - Tip calculator
#   Program will ask what the total bill is, what percentage tip you want to give, and how many people are going to split the bill.
#   Program should round the output to two decimal places

print("Day 2 Project: Tip Calculator - Enter total bill, tip percentage, and then how many people will split the bill. Output should be 2 decimal places.")

print("How much was the bill?")
bill = input()
print("What percentage would you like to tip?")
tip = input()
print("How many people will split the bill?")
ppl = input()

billtip = float(tip) / int(100) * float(bill)
ttlbill = float(billtip) + float(bill)
cost = float(ttlbill) / float(ppl)

amt = round(cost, 2)

print(f"Each person will need to pay ${amt}.")
