x = int(input("Enter lower boundary: "))
y = int(input("Enter upper boundary: "))
'z = int(input("Enter ierations number: "))'

t = 0

for i in range(x, y + 1) :
    print("Old value of", t)
    t +=i

print("Sum equals: ", t)

