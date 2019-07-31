

def BubbleSort(arr):
  n = len(arr)
  for i in range(0, n):
    for j in range(0, n - i - 1):
      if arr[j] > arr[j + 1]:
        arr[j], arr[j + 1] = arr[j + 1], arr[j]



def insertionSort(arr):
  for i in range(1,len(arr)):
    key = arr[i]
    j = i-1
    while j>=0 and key<arr[j]:
      arr[j+1] = arr[j]
      j -= 1
    arr[j+1] = key

'''
MergeSort(arr[], l,  r)
If r > l
     1. Find the middle point to divide the array into two halves:  
             middle m = (l+r)/2
     2. Call mergeSort for first half:   
             Call mergeSort(arr, l, m)
     3. Call mergeSort for second half:
             Call mergeSort(arr, m+1, r)
     4. Merge the two halves sorted in step 2 and 3:
             Call merge(arr, l, m, r)
'''
def merge(arr, l, m, r):
  n1 = m - l + 1
  n2 = r - m
  L = [0] * n1
  R = [0] * n2
  for i in range(0, n1):
    L[i] = arr[l + i]
  for j in range(0, n2):
    R[j] = arr[m+1+j]

  i,j,k=0,0,l
  while i < n1 and j <n2:
    if L[i]<=R[j]:
      arr[k] = L[i]
      i += 1
    else:
      arr[k] = R[j]
      j += 1
    k+=1
  while i < n1:
    arr[k] = L[i]
    i += 1
    k += 1
  while j < n2:
    arr[k] = R[j]
    j += 1
    k += 1


def MergeSort(arr, l, r):
  if r > l:
    mid = (l+r-1) / 2
    MergeSort(arr, l, mid)
    MergeSort(arr, mid+1, r)
    merge(arr, l, mid, r)


'''
quickSort(arr[], low, high)
{
    if (low < high)
    {
        /* pi is partitioning index, arr[pi] is now
           at right place */
        pi = partition(arr, low, high);

        quickSort(arr, low, pi - 1);  // Before pi
        quickSort(arr, pi + 1, high); // After pi
    }
}
/* This function takes last element as pivot, places
   the pivot element at its correct position in sorted
    array, and places all smaller (smaller than pivot)
   to left of pivot and all greater elements to right
   of pivot */
partition (arr[], low, high)
{
    // pivot (Element to be placed at right position)
    pivot = arr[high];  
 
    i = (low - 1)  // Index of smaller element

    for (j = low; j <= high- 1; j++)
    {
        // If current element is smaller than or
        // equal to pivot
        if (arr[j] <= pivot)
        {
            i++;    // increment index of smaller element
            swap arr[i] and arr[j]
        }
    }
    swap arr[i + 1] and arr[high])
    return (i + 1)
}
'''


def partition(arr, l, r):
 pivot = arr[r]
 smaller, equal, larger = l, l, r
 while equal <= larger:
   if arr[equal] < pivot:
     arr[smaller], arr[equal] = arr[equal], arr[smaller]
     smaller += 1
     equal += 1
   elif arr[equal] == pivot:
     equal += 1
   else:
     arr[larger], arr[equal] = arr[equal], arr[larger]
     larger -= 1
 return arr.index(pivot)


def QuickSort(arr, l, r):
  if l <r:
    pivotIdx = partition(arr, l, r)
    QuickSort(arr, l, pivotIdx -1)
    QuickSort(arr, pivotIdx+1, r)

# Driver code to test above
arr = [12, 11, 13, 7, 60]

QuickSort(arr,0,4)
print arr



