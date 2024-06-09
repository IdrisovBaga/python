immutable_var=1, 2, 'b', 'G'
immutable_var[0]=3 # кортежи неизменяемы. Если нам нужны изменяемые последовательности, используем списки
mutable_list=1, [2, 'b', 'essen', 2.1]
mutable_list[1][0]=3
print(mutable_list)
mutable_list=1, [2, 'b', 'essen', 2.1]
mutable_list[1][3]=3
print(mutable_list)