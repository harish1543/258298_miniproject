def BubbleSort(Input_list,List_size):
    for i in range(List_size-1):
        for j in range(List_size-i-1):
            if Input_list[j]>Input_list[j+1]:
                Input_list[j], Input_list[j+1] = Input_list[j+1], Input_list[j]
if __name__ == "main":
    print("------Bubble sort------")