#BigO and time growth
#Big O notation is used to measure how running time or space requirements for your program grow as input size grows
#Mathematical representation of time complexity. Always represents the worst possible scenario

#General steps to get the time complexity:

#example: time = a*n+b
#1. Keep fastest growing term
# time = a*n
#2. Drop constants:
# time = O(n)


#Time complexity will be O(n) also read as order of n. The time it takes for a computer to execute a
#  program is equally proportionate to the numbers
#of computations. If numbers have 4 million elements it will iterate 4 million times.
def get_squared_numbers(numbers):
    squared_numbers = []
    for n in numbers:
        squared_numbers.append(n*n)
    return squared_numbers

print(get_squared_numbers([2, 4, 6, 8, 9])) # 5 iterations 



# def foo(a):           size(a) -> 100 -> runtime = 0.22
                        #size(a) -> 1000 -> runtime = 0.23 basically constant
#     #

def find_first_pe(prices, eps, index):
    pe = prices[index]/eps[index]
    return pe
#Has a time complexite of O(1)

#finding the pe of the first stock via. the price and eps. Run time would be the same if prices and eps had 4 elements or 2 milion
#because when supplied an index it will be a constant operation. Don't really understand why


numbers = [3,6,2,4,3,6,8,9]

for i in range(len(numbers)):
    for j in range(i+1, len(numbers)):
        if numbers[i] == numbers[j]:
            print(str(numbers[i]) + " is a duplicate")
            break
#time complexity = a*n^2 +b 
#1. Keep fastest growing term
# time = a*n^2
#2. Drop constants:
# time = O(n^2)   

def one_program():
    duplicate = None
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):      #n^2 iterations
            if numbers[i] == numbers[j]:
                duplicate = numbers[i]
                break

    for i in range(len(numbers)):       #n iterations 
        if numbers[i] == duplicate:
            print(i)

#Why are these the rules to find BigO?: 
#1. Keep fastest growing term
#2. Drop constants:

#Because BigO refers to very large values of n (rough ballpark estimate). Hence if there's a function like:
#time = 5*n^2 + 3*n + 20
#if n = 1000
#time = 5000000 + 3020. (3*n + 20) = 0.0604% of the time

