
converted_number = "0."
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

base = int(input("Enter a base between 2 and 16  "))
while base < 2 or base > 16:
    base = int(input("Input is not between 2 and 16, Please enter a base that is between 2 and 16   "))
    if base < 2 or base > 16:
        continue
#<---------------------------------------------------------------------------------------------------------------------------------------------------------->
# this is the same as above however its with bases
#<---------------------------------------------------------------------------------------------------------------------------------------------------------->
decimal_points = 0
letter = ""
bin = []
#<---------------------------------------------------------------------------------------------------------------------------------------------------------->
# these are variable used in the code below letter refers to an empty string and bin is an empty array that will have calculations added to it.
#<---------------------------------------------------------------------------------------------------------------------------------------------------------->
while floating_number > 0:
  decimal_points += 1

  if decimal_points > 20:
       break

  cal = floating_number * base
  cal = (round(cal, 3))
  if cal in bin:
      print(bin)
      print("WARNING: periodic pattern detected")
      break
  bin.append(cal)
# <---------------------------------------------------------------------------------------------------------------------------------------------------------->
# the above while loop insures that when my floating point number is greater than zero we will add 1 to our decimal points variable in the condition that
# decimal points exceeds 20 points our code will break. Under that we have our calculations which is multiplying our floating point number by the inputed base
# and then rounding that to 3 places to avoid prevent rounding mistakes later on. After that we have our condition which stops recurring binarys basically what
#  it does is it check if our variable cal is inside the bin functiona nd if its repeating if so it will break the code And print our answer to five decimal
# places with a message it does so by appending cal into our empty array and iterating through it,
# <---------------------------------------------------------------------------------------------------------------------------------------------------------->
  if int(cal) <= 9:
      converted_number += str(int(cal))
  else:
      if int(cal) == 10:
          letter = "A"
      if int(cal) == 11:
          letter = "B"
      if int(cal) == 12:
          letter = "C"
      if int(cal) == 13:
          letter = "D"
      if int(cal) == 14:
          letter = "E"
      if int(cal) == 15:
          letter = "F"
      converted_number += str(letter)
# <---------------------------------------------------------------------------------------------------------------------------------------------------------->
# above are if conditions the will be added to the string letter used when converting hex numbers for example if we get the value 10 the if statement will make
# sure that the letter A will be printed instead.
# <---------------------------------------------------------------------------------------------------------------------------------------------------------->

  floating_number = cal-int(cal)

print("Your converted Binary Number is:  ", converted_number)
#<---------------------------------------------------------------------------------------------------------------------------------------------------------->
# the above prints the final value and also givesw us our new floating point number for the loop by minusing the integer the value from cal we are left with
# a floating decimal.
#<---------------------------------------------------------------------------------------------------------------------------------------------------------->
