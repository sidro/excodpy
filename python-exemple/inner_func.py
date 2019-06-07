def outer():
    x = "Hahaha!!!"
    def inner():
        print(x)
        return x + "Hihihihihi!!!"
    print(inner())
    print(x)

outer()