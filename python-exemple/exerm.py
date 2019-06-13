def decorat(funct):
    """docstring for decorat function"""

    def func_wrapper(name):
        '''func_wrapper'''

        print(name)
        return name
    return func_wrapper


@decorat
def mimi(nume):
    return 'nume'

minemi = mimi("Ovidiu")
print(minemi)
