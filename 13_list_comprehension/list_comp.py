numbers = [-4, -3, -2, -1, 0, 2, 4, 6]

neg_and_cero = [i for i in numbers if i <= 0]
print(neg_and_cero)

list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
one_lst = [number for row in list_of_lists for x in row for number in x]
print(one_lst)

list_tuple = [(i, 1, i, i**2, i**3, i**4, i**5) for i in range(11)]
print(list_tuple)
