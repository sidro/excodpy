def calculate(**kwargs):
    operations = {
        'add': kwargs.get('first', 0) + kwargs.get('second', 0),
        'subtract': kwargs.get('first', 0) - kwargs.get('second', 0),
        "multiply": kwargs.get("first", 0) * kwargs.get("second", 0),
        "divide": kwargs.get("first", 0) / kwargs.get("second", 0)
    }
    is_float = kwargs.get("make_float", False)
    result = operations[kwargs.get("operation", '')]
    if is_float:
        final = "{} {}".format(kwargs.get("message",
                                          "The result is "), float(result))
    else:
        final = "{} {}".format(kwargs.get("message",
                                          "The result is "), int(result))
    return final


print(calculate(make_float=False, operation='multiply',
                message='You just added', first=2, second=4))
print(calculate(make_float=True, operation='divide', first=3.5, second=5))
