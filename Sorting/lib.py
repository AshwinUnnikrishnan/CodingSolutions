
def swap(A, i, j):
    temp = A[i]
    A[i] = A[j]
    A[j] = temp

class QuickSort:
    def quickSort(self, A):
        '''
        Perform quick sort on list A
        :param A: List of unsorted elements
        :return: the sorted array
        '''
        if len(A) == 0 or len(A) == 1:      # if 0 or 1 element return the list
            return A
        pivot = len(A) - 1                      #Taking last element as pivot ( Can add preprocessing to make sure it dosent fall in the corner cases )
        i = self.partition(A, pivot)            #Setting the pivot to the right position
        A[0:i] = self.quickSort(A[0:i])         #Performing quicksort on elements less or equal to pivot
        A[i+1:len(A)] = self.quickSort(A[i+1:len(A)])   #perform quicksort on elements greater than pivot
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


