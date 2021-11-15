def binary(a,key):
    count=0
    for i in a:
        count+=1
    low=0
    high=count-1
    while low <= high:
        mid=(low+high)//2
        if key == a[mid]:
            return key
        elif key < a[mid]:
            high=mid-1
        else:
            low=mid+1
    print("Element not found")
a=[1,4,7,8,21,34,54,86,91,92,96,99]
key=int(input("enter the element to be searched:"))
print(binary(a,key))