from functools import wraps


def ensure_authorized(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        if kwargs.get('role') == 'admin':
            return fn(*args, **kwargs)
        return "Unauthorized"
    return wrapper


@ensure_authorized
def ark(*args, **kwargs):
    return "Shh! Don't tell anybody!"


print(ark(role="admin"))
