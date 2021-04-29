def SelectionSort(Input_list,List_size):
    for i in range(List_size-1):
        min_index = i
        for j in range(i+1,List_size):
            if Input_list[j] < Input_list[min_index]:
                min_index = j
        Input_list[i], Input_list [min_index] = Input_list[min_index], Input_list[i]

if __name__ =="main":
    print("-------Selection Sort-------")