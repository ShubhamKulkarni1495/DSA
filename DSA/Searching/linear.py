def linear_search(arr,key):
    for i in range(len(arr)):
        if key == a[i]:
            print(key,"found at position",i)
            break
    else:
        print("Element is not in the list")
a=[1,4,7,8,21,34,54]
key=int(input("enter the element to be searched:"))
linear_search(a,key)