user = {'username': 'jose123', 'access_level': 'admin'}


def user_has_permissions(func):
    def secure_function():
        if user.get('access_level') == 'admin':
            return func()
    return secure_function


def my_function():
    return 'Password panel is 1234.'


my_secure_function = user_has_permissions(my_function)
print(my_secure_function())
