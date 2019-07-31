# move largest to end
def bubble(arr):
  n = len(arr)
  for i in range(0, n):
    for j in range(0, n - i -1):
      if arr[j] > arr[j+1]:
        arr[j], arr[j+1] = arr[j+1], arr[j]

# move smallest to start
def selection(arr):
  for i in range(0, len(arr)):
    minidx = i
    for j in range(i+1,len(arr)):
      if arr[j] < arr[minidx]:
        minidx = j

    arr[i], arr[minidx] = arr[minidx], arr[i]

def insertion(arr):
  n = len(arr)
  for i in range(1,n):
    key = arr[i]
    j = i-1
    while j >= 0 and arr[j] > key:
      arr[j+1] = arr[j]
      j -= 1
    arr[j+1] = key

def shellsort(arr):
    # Start with a big gap, then reduce the gap
    n = len(arr)
    gap = n / 2
    # Do a gapped insertion sort for this gap size.
    # The first gap elements a[0..gap-1] are already in gapped
    # order keep adding one more element until the entire array
    # is gap sorted
    while gap > 0:

      for i in range(gap, n):
        # add a[i] to the elements that have been gap sorted
        # save a[i] in temp and make a hole at position i
        key = arr[i]
        # shift earlier gap-sorted elements up until the correct
        # location for a[i] is found
        j = i
        while j >= gap and arr[j - gap] > key:
          arr[j] = arr[j - gap]
          j -= gap
        # put temp (the original a[i]) in its correct location
        arr[j] = key
        print i, arr
      gap /= 2


arr = [1000, 98, -1, 0 , 20]
shellsort(arr)
print arr