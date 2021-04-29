from src.BubbleSort import BubbleSort
from src.SelectionSort import SelectionSort
from src.InsertionSort import InsertionSort
from src.MergeSort import MergeSort


while(True):
    print("Enter Array Size: ")
    Array_size = int(input())
    Array = [int(element) for element in input("Enter Elements: ").split()] 
    print(" 1. Bubble Sort\n 2. Selection Sort\n 3. Insertion Sort\n 4. Merge Sort\n")
    choice = int(input("Enter Choice: "))
    if choice == 1:
        BubbleSort(Array,Array_size)
    elif choice == 2:
        SelectionSort(Array,Array_size)
    elif choice == 3:
        InsertionSort(Array, Array_size)
    elif choice == 4:
        MergeSort(Array,0,Array_size-1)
    else:
        print("Invalid Choice")
    print("Sorted array is:",end= " ")
    for element in Array:
        print(element,end= " ")
    print("\n 1. Perform Another Sorting\n 2. Exit")
    secondchoice = int(input("Enter Choice: "))
    if secondchoice == 2:
        print("Exiting...")
        break