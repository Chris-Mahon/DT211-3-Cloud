"""Euler 4-
Highest Palindrome with a 3 digit number
The code consists of 2 for loops, which goes through every possible combination of number. 
It then checks if the product is the same backwards as it is forwards and adds it to a number that represents the highest palindrone that has occurred"""
i=0
j=0
reverse=0
Highest = 0

print("Hello")
for i in range(0, 1000):
  for j in range(0, 1000):
    Number=i*j
    if int(str(Number)[::-1]) == Number:
      if Highest < Number:
        Highest = Number 
      elif Highest == 0:
        Highest = Number
      
print("Highest Palindrone is", Highest)