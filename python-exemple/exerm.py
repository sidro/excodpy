def decorat(funct):
    def func_wrapper(name):
        print(name)
        return name
    return func_wrapper


@decorat
def m():
    return 'nume'


print(m('Ovidiu'))
