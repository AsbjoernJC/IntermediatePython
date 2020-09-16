#information is stored in ram as bits. 1 byte is 8 bits.

stock_prices = [298, 305, 320, 301, 292]
# """ stock_prices[0] points to -> 0x00500
# stock_prices[2] -> 0x00500 + 2 * sizeof(integer) where an integer is stored as 4 bytes
# 0x00500 +2*4 bytes = 0x0508 and now we have found the pointer / memory address
# Lookup by index O(1) because of constant time operation
# On what day was the price 301? 
for i in range(len(stock_prices)):
    if stock_prices[i]==301:
        print(i)
# O(n) seen from the worst case scenario
# print all prices
for price in stock_prices:
    print(price)
# O(n)
#Insert new price 284 at index 1
# stock_prices.insert(1, 284)
# O(n) when inserting an integer at an index it will causes all the other memoryaddresses to swap n numbers of time. 
# stock_prices.remove()
# O(n) causes all other memory addresses to switch upwards. It's a bit different in python because it uses objects and references 
# in python, list is implemented as a dynamic array in other languages there static and dynamic arrays""""

# static arrays allocates memory for a fixed size
# dynamic arrays will allocate some initial capacit in the memory. 
# if the capacity has been met and a new element is inserted. It will allocate one new memory area at a different location. Initial capacity = 10 now the capacity will be 10*2 = 20.
# and the dynamic arrays containers will have the values copyed to the other area. WHen inserting a 21st element it will allocate a new memory segment
# will allocate 30 and 30*2 so the new capacity will be 90. This is called geometric progression.  

#arrays can store numbers, text or complex objects. Python can even store multiple different data types in an array
#can have 2 and 3d dimensional arrays, nested arrays/lists

dynamic_n_static = [{"python": {"static array": "doesn't exist", "dynamic array": "list"}}, 
{"Java": {"static array": "Native array", "dynamic array": "Arraylist"}},
{"C++": {"static array": "Native array", "dynamic array": "std::vector"}}]

print(dynamic_n_static[0]["python"].keys(), dynamic_n_static[0]["python"].values())

