# The point at which i stopped:
# https://youtu.be/IR_S8BC8KI0?list=PLeo1K3hjS3uu_n_a__MI_KktGTLYopZ12&t=446

#An example of when binary search should be used:

import math

#a sorted list of numbers
l = [4, 9, 15, 21, 34, 57, 68, 91]

for i in range(len(l)):
    if l[i] == 68:
        print("The number 68 can be found at index: " + str(i))
#O(n) time complexity. Imagine if the list contains a billion numbers. It would not be very efficient
#to look each number through

mid = 0
first_index = 0
last_index = 0
def binary_search(list, first_index, last_index, num):
    mid  = (first_index + last_index)//2
    if list[mid] < num:
        first_index = mid + 1
        binary_search(list, first_index, last_index, num)
    elif list[mid] > num:
        last_index = mid - 1
        binary_search(list, first_index, last_index, num)
    else:
        print("The number that your are seeking (%d) can be found at index (%d)" %(num, mid))
        return mid

binary_search(l, 0, len(l)-1, 10)

# """ search for 10. 
# iteration 1 = n/2
# iteration 2 = (n/2)/ = n/2^2
# iteration 3 = (n/2^2)/2 = n/2^3
# .... iteration k = n/2^k
# BigO. 
# 1 = n/2^k amount of iterations to get the array size to 1, because it is our worst case scenario
# n = 2^k 
# log(n) = log(2^k)
# log(n) = k*log(2)
# log(2) base n is equal to one so 
# log(n) = k*1
# k = log(n) -> O(log(n))
# k = O(log(n)) -> log(8) -> log(2^3) -> 3*log(2) -> 3 iterations
# """



# # Test array 
# arr = [ 2, 3, 4, 5, 6, 7, 8, 9, 10, 40 ] 
# x = 10

# def binary_search(arr, x): 
#     low = 0
#     high = len(arr) - 1
#     mid = 0
  
#     while low <= high: 
  
#         mid = (high + low) // 2
  
#         # Check if x is present at mid 
#         if arr[mid] < x: 
#             low = mid + 1
  
#         # If x is greater, ignore left half 
#         elif arr[mid] > x: 
#             high = mid - 1
  
#         # If x is smaller, ignore right half 
#         else: 
#             return mid 
  
#     # If we reach here, then the element was not present 
#     return -1
  



  
# # Function call 
# print(binary_search(arr, x)) 

    