import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def raNum(min, max):
    #used to shorten getting a random num
    return random.randrange(min, max)
def runRandStr(amt):
    length = raNum(0, amt)
    string = "string: "
    for x in range(length):
        string += letters[raNum(0, amt)]
    return string
#print(runRandStr(25));

def compoundInterest(p, r, period, t):
    if (period == "monthly"):
        n = 12
    if (period == "semimonthly"):
        n = 24
    if (period == "biweekly"):
        n = 26
    if (period == "weekly"):
        n = 52
        principal=p,rate=r,period=period,time=t
    return ( principal(1 + (rate/n)) ** (n*t));
print (compoundInterest(550, ))