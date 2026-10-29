base=int(input("Enter Base: "))
power=int(input('Enter power: '))
result=1
for i in range(power):
    result*=base

print(result)