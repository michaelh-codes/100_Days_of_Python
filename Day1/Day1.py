#   Part 1 - Printing
#   Must use quotations to show that this is a "String" or regular text, not code.


print("Hello world!")

#   stackoverflow.com can be used for some troubleshooting issues

#######################################################

#   Exercise 1 - Printing

#   Example Output:
#   Day 1 - Python Print Function
#   The function is declared like this:
#   print('what to print')



#   Exercise 1 - Solution

print("Day 1 - Python Print Function")
print("The function is declared like this:")
print("print('what to print')")


#######################################################

#   Exercise 2 - Debugging Practice

#   Exmple Output:

#   Day 1 - String Manipulation
#   String Concatenation is done with the "+" sign.
#   e.g. print("Hello " + "world")
#   New lines can be created with a backslash and n.


#   Fix the code below

#   print(Day 1 - String Manipulation")
#   print("String Concatenation is done with the "+" sign.")
#     print('e.g. print("Hello " + "world")')
#   print(("new lines can be created with a backslash and n.")


#   Excercise 2 - Solution

print('Day 1 - String Manipulation\nString Concatenation is done with the "+" sign.\ne.g. print("Hello " + "world")\nNew lines can be created with a backslash and n.')


########################################################

#   Exercise 3 - Input Function

#   Example Input:
#   Angela

#   Example Output:
#   What is your name? {user input}
#   {length of name}

#   Exercise 3 - Solution

#   This was my code without watching the video
print("What is your name?")
name = input()
print(len(name))

#   Actual Solution
print( len( input("What is your name?") ) )


########################################################

#   Exercise 4 - Variables

#   Write a program that switches the values stored in the variables a and b.

#   Example Input:
#   a: 3
#   b: 5

#   Example Output:
#   a: 5
#   b: 3


#   Exercise 4 Solution

#  Don't change the code below
a = input("a: ")
b = input("b: ")
#  Don't change the code above

####################################
#Write your code below this line

floata = str(a)
floatb = str(b)

a = str(floatb)
b = str(floata)

#   Instructor Solution
#   c = a
#   a = b
#   b = c

#Write your code above this line
####################################

#  Don't change the code below
print("a: " + a)
print("b: " + b)


###############################################################
print("\n\n")
###############################################################

print("Variable Rules\nNames should make sense for troubleshooting later on\nNumbers cannot be at the start of a Variable\nDon't use common commands as Variables")

################################################################

#   Day 1 - Challenge

#   Create a band name generator that asks for the name of the city you grew up in and your pets name. The code will combine the two inputs and generate a band name. When prompted for input, the cursor should be on a new line.

#   Example Output:
#   Welcome to the Band Name Generator.
#   What's the name of the city you grew up in?
#   Bristol
#   What's your pet's name?
#   Rabbit
#   Your band name could be Bristol Rabbit


#   Day 1 - Challenge Solution

print("Welcome to the Band Name Generator.")
print("What's the name of the city you grew up in?")
city = input()
print("What's your pet's name?")
pet_name = input()
print("Your band name could be " + city + " " + pet_name)
