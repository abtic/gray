numberOfChars = int(input("enter the number of chars to generate: "))
index = 0;
numbers = [];
NON = 2** numberOfChars;
gray = [""] * NON;

def generate(n):
    
    for t in range(0,int(n/2)):
        gray[t] += "0"

    for f in range(int(n-1),int(n/2)-1,-1):
        gray[f] += "1"  

    if n >= 3:
        generate(n/2)

def finalize(start,stop, ind):
    
    for f in range(int(start)-1,int(stop)-1,-1):
        gray[f] += gray[start-f-1][ind]


generate(NON)

for r in range(numberOfChars-1,0,-1):
    for k in range(numberOfChars - r):
        numbers.append(numberOfChars - k - 1)
     
    numbers.sort()
    for g in numbers:
        finalize(int(NON/2**(r-1)),int(NON/2**(r)),(g))
    numbers = [];

print(gray)
for t in gray:
    print(t)

input();
