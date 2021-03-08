import random
#n = 0
#while True:
    #if n > 9:
    #    break
   # print(f"a random value 1-10", random.randint(1,10))
    #n = n + 1

#for val in range(0, 10):
   # print(random.randint(1,10))

sum = 0
for val in range(0, 10):
   sum = sum + random.randint(1, 10)

print(f"The sum of 10 random numbers is {sum}")