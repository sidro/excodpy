# Metoda 1 de rezolvare. Si metoda ce-a mai buna dintre cele doua.
def multiply_even(list_):
    total = 1
    for num in list_:
        if num % 2 == 0:
            total = total * num
    return total
    

# Metoda 2 de rezolvare. Demonstrare ca se poate rezolva si cu "liste comprehensions"
def multiply_even_numbers(list_):
    even_list = [even for even in list_ if even % 2 == 0]
    total = 1
    for n in even_list:
        total = total * n
    return total

print(multiply_even_numbers([2, 3, 4, 5, 6]))
print(multiply_even([2, 3, 4, 5, 8]))