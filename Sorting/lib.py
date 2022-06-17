
def swap(A, i, j):
    temp = A[i]
    A[i] = A[j]
    A[j] = temp

class QuickSort:
    def sort(self, A):
        '''
        Perform quick sort on list A
        :param A: List of unsorted elements
        :return: the sorted array
        '''
        if len(A) == 0 or len(A) == 1:      # if 0 or 1 element return the list
            return A
        pivot = len(A) - 1                      #Taking last element as pivot ( Can add preprocessing to make sure it dosent fall in the corner cases )
        i = self.partition(A, pivot)            #Setting the pivot to the right position
        A[0:i] = self.sort(A[0:i])         #Performing quicksort on elements less or equal to pivot
        A[i+1:len(A)] = self.sort(A[i+1:len(A)])   #perform quicksort on elements greater than pivot
        return A

    def partition(self, A, pivot):
        '''
        Takes input and then puts the pivot in the right position it belongs in the array
        :param A: List to put the right position of pivot
        :param pivot: pivot index
        :return: returns the position where the pivot is placed
        '''
        i, j = 0, len(A) - 2
        while i <= j :
            while A[i] <= A[pivot] and i <= j:          #while the left index value is less or equal to pivot increment index
                i += 1
            while A[j] > A[pivot] and i <= j:           #while the right index value is large decrement index
                j -= 1
            if i <= j:
                swap(A, i, j)
        swap(A,i, pivot)
        return i

class BubbleSort:

    def sort(self, A):
        for i in range(len(A)):
            flag = True                                     #Flag to run the algorithm in Omega(n) when already sorted array
            for j in range(len(A)-(i+1)):
                if A[j] > A[j+1]:
                    swap(A, j, j+1)
                    flag = False
            if flag == True:
                print("Already Sorted Breaking")
                break
        return A

class InsertionSort:

    def sort(self, A):
        '''
        Performs insertion sort, considers left side as sorted and takes one element at a time and places in the right position on left side
        :param A:
        :return:
        '''
        for i in range(1,len(A)):
            for j in range(i,0,-1):
                flag = False
                if A[j] < A[j-1]:
                    swap(A,j,j-1)
                    flag = True
                if flag == False:                   #Will make it run in O(n) for already sorted array
                    break
        return A

class SelectionSort:

    def sort(self, A):
        '''
        Sets minimum element one at a time from the beginning of the array
        :param A:
        :return:
        '''
        for i in range(len(A)):
            minIndex = i
            for j in range(i+1,len(A)):
                if A[minIndex] > A[j]:
                    minIndex = j
            swap(A, i, minIndex)
        return A

class MergeSort:

    def sort(self, A):
        '''
        Divide into individual elements and combine smaller lists using someother sorting algorithm
        :param A:
        :return:
        '''
        if len(A) == 0 or len(A) == 1:
            return A
        mid = len(A)//2

        L, R = self.sort(A[ : mid]), self.sort(A[mid : ])

        quick = QuickSort()
        A = quick.sort(L + R)

        return A

class HeapSort:

    def lowestOfThree(self, A, a, b, c):
        lower = A[a]
        ind = a
        if A[b] < lower :
            lower = A[b]
            ind = b
        if A[c]<lower:
            lower = A[c]
            ind = c
        return lower, ind

    def heapify(self, A, n, i):

        largest = i
        l = 2*i + 1
        r = 2*i + 2

        if l < n and A[largest] < A[l]:
            largest = l
        if r < n and A[largest] < A[r]:
            largest = r

        if largest != i:
            swap(A, largest, i)
            self.heapify(A, n, largest) #heapify rest of the below tree as well if swapped
        return A

    def sort(self, A):
        n = len(A)
        for i in range(n//2 - 1, -1, -1):
            self.heapify(A, n, i)

        for i in range(n - 1, 0, -1):
            swap(A, i, 0)
            self.heapify(A, i, 0)
        return A
