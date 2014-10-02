""""Find the difference between the sum 
of the squares of the first one hundred natural 
numbers and the square of the sum. 
This was completed by Dovydas.""""

i = 0
sum1 = 0
for i in range (1, 101):
sum1 = sum1 + i**2

sum2 = 0
for i in range (1,101):
sum2 = sum2 + i

sum2 = sum2**2


sum3 = 0
sum3 = sum2 - sum1

print sum1
print sum2
print sum3
