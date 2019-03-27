def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper


def do_twice(func):
	# *args sau **kwargs post fi puse ca si variabile in loc de args
    def wrapper_do_twice(args): 
        func(args)
        func(args)
    return wrapper_do_twice


@my_decorator
def say_whee():
    print("Whee!")

@do_twice
def say_whe(name):
    print(f"WHEE! {name}")


say_whee()
say_whe("Ovidiu")
