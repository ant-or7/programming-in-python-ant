limit=int(input("Enter Number: "))
if limit==1:
    print('0')
elif limit>1:
    arr=[0,1]
    for i in range(2,limit):
        arr.append(arr[i-1]+arr[i-2])
    print(arr)