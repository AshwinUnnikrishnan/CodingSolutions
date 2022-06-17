from lib import QuickSort, BubbleSort, InsertionSort, SelectionSort, MergeSort, HeapSort

arr = [10,12,21, 2,4,5,6,13,11,9,100, 123,121,111,99,1,14]

#sortV = QuickSort()
#sortV = BubbleSort()

#sortV = SelectionSort()
#sortV = MergeSort()

sortV = HeapSort()


arr = sortV.sort(arr)
print(arr)
