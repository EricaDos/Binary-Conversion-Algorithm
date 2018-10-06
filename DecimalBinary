
binary_number = "0."
cal = 0
floating_number = float(input("Enter a floating point number thats >= 0 and <= 1  "))
#<---------------------------------------------------------------------------------------------------------------------------------------------------------->
# In the above we have created a string that the binary number will be printed onto it starts with "0." and the following binary numbers will be added it to
# it producing a completed conversion. The cal variable is a variable used for calculations later on.
# Floating number refers to the number that will be inputed by the user that is between 0 and 1
#<---------------------------------------------------------------------------------------------------------------------------------------------------------->

while floating_number < 0 or floating_number > 1:
    floating_number = float(input("Number is not  >= 0 and <= 1, Please enter a floating point number thats >= 0 and <= 1   "))
    if floating_number < 0 or floating_number > 1:
        continue
#<---------------------------------------------------------------------------------------------------------------------------------------------------------->
# above we have written a while loop that insures that the program will not continue until the user inputs a number between 0 and 1 and will keep looping
# until the user does so.
#<---------------------------------------------------------------------------------------------------------------------------------------------------------->
binary_digits = 0
#<---------------------------------------------------------------------------------------------------------------------------------------------------------->
# variable used in the code below.
#<---------------------------------------------------------------------------------------------------------------------------------------------------------->

while floating_number > 0:
    binary_digits += 1

    if binary_digits > 20:
        break

    cal = floating_number * 2
    binary_number += str(int(cal))

    floating_number = cal - int(cal)

# <---------------------------------------------------------------------------------------------------------------------------------------------------------->
# The above loop insures that when our floating number is greater than zero we will add one decimal point to our binary digits variable until it reaches
# Twenty popihnts where it will break. After that we have our calulations which multiplys our floating by 2 and takes the string integer of it and add its to
# The Binary number variable. our new floating number is the decimal part of our cal variable.
# <---------------------------------------------------------------------------------------------------------------------------------------------------------->

print("Your converted Binary Number is:  ",binary_number)
# <---------------------------------------------------------------------------------------------------------------------------------------------------------->
# The above then prints out our result.
# <---------------------------------------------------------------------------------------------------------------------------------------------------------->
