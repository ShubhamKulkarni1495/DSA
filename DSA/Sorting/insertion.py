def insertion_sort(a):
    for i in range(1,len(a)):
        min_value=a[i]
        j=i-1
        while j >=0 and min_value < a[j]:
            a[j+1] = a[j]
            j -= 1
        a[j+1] = min_value
    print(a)
a=[5,76,32,86,3,2]
insertion_sort(a)