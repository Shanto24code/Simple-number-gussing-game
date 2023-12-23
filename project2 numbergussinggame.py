import random
rn = random.randrange(1,100)
print(rn)
userinput = int(input('guess the number :'))
if userinput > rn:
    print('number is too high')

elif rn > userinput:
    print('nuber is too low')

else:
    print('you win')