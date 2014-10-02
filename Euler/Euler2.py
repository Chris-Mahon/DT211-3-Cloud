term1 = 1
term2 = 2
sum = 0

for i in range (0, 4000000):
    sum = term1 + term2
    term1 = term2
    term2 = sum
    
print("Fibinacci up to 4000000 is ", sum)