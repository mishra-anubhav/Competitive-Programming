"""Write a function get_products_of_all_ints_except_at_index() that takes a list of integers and returns a list of the products.

For example, given:

  [1, 7, 3, 4]

Python 2.7
your function would return:

  [84, 12, 28, 21]

Python 2.7
by calculating:

  [7 * 3 * 4,  1 * 3 * 4,  1 * 7 * 4,  1 * 7 * 3] """

# CODE
arr =   [1, 7, 3, 4]
arr2 = []

def get_products_of_all_ints_except_at_index(arr):
    n=len(arr)
    index=0
    for j in range(0, n):
        result =1
        for i in range(0, n):
            if i == index:
                continue
            else:
                result = result* arr[i]
        arr2.append(result)
        index = index+1
    print(arr2)

get_products_of_all_ints_except_at_index(arr)