def selection_sort(a):
    for i in range(len(a)):
        min_idx = i
        for j in range(i+1, len(a)):
            if a[min_idx] > a[j]:
                min_idx = j        
        a[i] = a[min_idx]
        a[min_idx]= a[i]
    print(a)
a = [64, 25, 12, 22, 11]
selection_sort(a)