print('WELCOME TO MY LOVE CALCULATOR.')
print('What is your name?')
name = input() 
print('Hi ' + name + ' COME HERE TO SEE HOW MUCH LOVE IS THERE IN YOUR LIFE')
print('Note : Score is out of 50.')
your_name = str(input('Enter Your name: '))
crush_name = str(input('Enter Your partner name: '))
x = (len(your_name))
y = (len(crush_name))
 
S1 = (your_name[:1])
S2 = (crush_name[:1])
POINTS = x + y
if x == y:
    POINTS = POINTS + 20
elif S1 == "a" or "e" or "i" or "o" or "u":
    POINTS = POINTS + 5
else:
    POINTS = POINTS + 2.5
if S2 == "a" or "e" or "i" or "o" or "u":
    POINTS = POINTS + 5
else:
    POINTS = POINTS + 2.5
print (POINTS)
if (POINTS == 50 and POINTS>=40) :
    print('Congrats you are leading a great love life.')
elif (POINTS <=40 and POINTS >=30):
    print('You are putting good efforts.Keep it up.')
elif (POINTS<=30 and POINTS>=20):
    print('Give attention to ur partner.Need hardwork.')
elif POINTS>20:
    print('Are you sure you have any partner???')
else:
    print('ERROR!!!TRY AFTER SOMETIME....')


import time
time.sleep(30)