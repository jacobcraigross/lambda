# Lambda expression (ie: 'anonymous function')

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

even = filter(lambda num : num % 2 == 0, my_list)

print (list(even))

# ----------------------------------------------

new_list = [3, 6, 9, 12]

thrice = filter(lambda num : num ** 3, new_list)

print (list(thrice))
