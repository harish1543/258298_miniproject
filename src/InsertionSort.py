def InsertionSort(Input_list,List_size):
    for i in range(List_size):
        key = Input_list[i]
        j = i-1
        while(j >= 0 and Input_list[j]>key):
            Input_list[j+1] = Input_list[j]
            j-=1
        Input_list[j+1] = key

if __name__ =="main":
    print("Insertion Sort")