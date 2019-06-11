def decorat(funct):
    def func_wrapper(name):
        print(name)
        return name
    return func_wrapper


@decorat
def m(nume):
    return 'nume'

mine = m("Ovidiu")
print(mine)
