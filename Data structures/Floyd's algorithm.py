# Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), 
# prove that at least one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.

# Example 1:

# Input: [1,3,4,2,2]
# Output: 2
# Example 2:

# Input: [3,1,3,4,2]
# Output: 3
# Note:

# You must not modify the array (assume the array is read only).
# You must use only constant, O(1) extra space.             ????
# Your runtime complexity should be less than O(n^2).
# There is only one duplicate number in the array, but it could be repeated more than once. 

#Why doesn't n(n+1)/2 = i from i=1 to n.  Given the sum of the array and the difference of the sum from i=1 to n. Doesn't work as the duplicate could be
#repeated

#Time complexity < O(n^2) floyd's algorithm = O(n), need to learn about time complexity. Sorting has a time complexity of O(nlog(n))
#can't be sorted though because it is not allowed to modify the array

#Method 1: Sort / Scan
# def findDuplicate(nums):
#     nums.sort()
#     for i in range(1, len(nums)):
#         if nums[i] == nums[i-1]:
#             return nums[i]

# print(findDuplicate([3, 1, 4, 2, 4]))

#Time: O(nlog(n))
#space: O(1)
#Issue: Array was modified      nums.sort()


#Method 2: Set, dictionary
# def findDuplicate(nums):
#     seen = {}
#     for num in nums:
#         if num in seen:
#             return num
#         seen[num] = True

# print(findDuplicate([3, 1, 3, 4, 2]))

#Time: O(n)
#space: O(n)        ?Not explained well: "The worst case scenario is that it would contain all the elements."
#Issue: not space O(1)


#Method 3: Floyd's algorithm        cycling through elements till they've found the duplicate
def findDuplicate(nums):
    tortoise = nums[0]
    hare = nums[0]
    while True:
        tortoise = nums[tortoise]
        hare = nums[nums[hare]]   #moves at a pace that's twice as fast as the tortoise
        if tortoise == hare:      #The point at which they meet
            break
    
    ptr1 = nums[0]    #will loop from the beginning 
    ptr2 = tortoise
    while ptr1 != ptr2:
        ptr1 = nums[ptr1]   #Will move one step at a time
        ptr2 = nums[ptr2]   #will move one step at a time and at the end find the duplicate
    
    return ptr1
print(findDuplicate([3, 1, 4, 5, 2, 6, 7, 8, 9, 10, 11, 4]))

#Why does it work?
#         *
# * * * Ø   M 
#         *
# <-x->        The number of nodes/distance before landing at the start of the cycle
#     *
# Ø       M
#     *
# the distance/number of nodes from M (meetingpoint) to the beginning of the cycle Ø counter clockwise will be = y
# the distancer/number of nodes from M to Ø (the rest of the cycle) clockwise will be = z
# the length of the cycle L = y + z
# M = x + y

# What we want to prove: x mod L = z   The remainder of x/L = Z. When this is true the hare and the tortoise will meet at the duplicate

# Turtle distance = x + y
# Hare distance = 2(x+y)
# rewritten: M + c*L      where c (the amount of loops) is a constant as the hare could cycle through an infinite amount of times
# 2(x+y) = x+y + c*L
# 2x + 2y = x+y + c*L
# x + y = c*L
# x = c*L - y 
# x modL = (c*L-y)modL
# x modL = (L+L+L... -y)modL #where the amount of cycles is determined by c) The remainder will be -y as it is lesser than L(L= y + z) 
# x modL = L-y
# x modL = z+y-y
# x modL = z 
# Therefore they must meet at the duplicate


#Time: O(nlog(n))
#space: O(1)
#Issue: 


#A project could be to have the cycle visualized on my Personal portfolio website, when running through a given list/array

