i=0
j=0
reverse=0
print("Hello")
for i in range(0, 999):
  for j in range(0, 999):
    Number=i*j
    print(Number, str(Number)[::-1])
    if str(Number)[::-1] is Number:
      print("Reverse!")
      reverse+=1
      
print("Times reversed is ", reverse)