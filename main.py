# print out the numbers 1 - 10

counter = 1
while(counter <= 10): # or (counter < 11)
  print(counter)
  counter += 1

print()
# print out all even numbers between 0 - 20
print()

counter = 2
while(counter <= 20):
  print(counter)
  counter += 2

print()
# ask the user for a number
# print all the numbers up to the user's number started at 1
print()

userNumber = int(input("Give a number: "))
counter = 1
while(counter <= userNumber):
  print(counter)
  counter += 1

print()
# while () :
#     if (condition)
#         print

# Alternative way to print even numbers
counter = 1
while(counter <= 20):
  if(counter % 2 == 0):
    print(counter)
  counter += 1

print()
# print all the numbers between 1-100 that are divisable by 3 or 7
# BUT NOT BOTH
counter = 1
while(counter <= 100):
  if (counter % 3 == 0 or counter % 7 == 0):
    if not (counter % 3 == 0 and counter % 7 == 0):
      print(counter)
  counter += 1

print()
# print all the numbers between 1-100
# if the number is divisible by 3, print out "Fizz"
# if the number is divisible by 5, print out "Buzz"
# if the number is divisible by BOTH, print out "FizzBuzz"
counter = 1
while(counter <= 100):
  if(counter % 3 == 0 and counter % 5 == 0):
    print("FizzBuzz")
  elif(counter % 3 == 0):
    print("Fizz")
  elif(counter % 5 == 0):
    print("Buzz")
  else:
    print(counter)
  counter += 1