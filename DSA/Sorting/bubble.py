def buuble_sort(list1):
    i=0
    temp=0
    while(i<len(list1)-1):
        j=0
        while(j<len(list1)-1):
            if(list1[j]>list1[j+1]):
                temp=list1[j]
                list1[j]=list1[j+1]
                list1[j+1]=temp
            j+=1
        i+=1
    print(list1)    
a=[5,3,8,1,7,9,4]
buuble_sort(a)