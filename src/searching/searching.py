# STRETCH: implement Linear Search				
def linear_search(arr, target):
  
  # TO-DO: add missing code
  for index, num in enumerate(arr):
    if num == target:
      return index
  return -1   # not found


# STRETCH: write an iterative implementation of Binary Search 
def binary_search(arr, target):

  if len(arr) == 0:
    return -1 # array empty
    
  low = 0
  high = len(arr)-1

  # TO-DO: add missing code
  arr = sorted(arr)
  while low <= high:
    middle = low + (high - low) // 2
    if arr[middle] == target:
      return middle
    elif arr[middle] < target:
      low = middle + 1
    else:
      high = middle - 1

  return -1


# STRETCH: write a recursive implementation of Binary Search 
def binary_search_recursive(arr, target, low, high):
  
  middle = (low+high)//2

  if len(arr) == 0: return -1 # array empty
  elif arr[middle] == target: return middle
  elif low > high: return -1
  elif arr[middle] < target: return binary_search_recursive(arr, target, middle + 1, high)
  else: return binary_search_recursive(arr, target, low, middle - 1)
