import time

def decorator_with_arguments(dec1arg):  
    def decorator(func):
        def wraper(*args, **kwargs):
            print('Started')
            val = func(*args, **kwargs)
            print(type(val))
            print(f'Converting the value to specified {dec1arg} type')
            match dec1arg:
                case 'string':
                    val = str(val)
                case 'list':
                    val = list(val)
                case 'tuple':
                    val = tuple(val)
                case 'float':
                    val = float(val)
                case 'dict':
                    val = dict(val)
                case 'set':
                    val = set(val)

            print(type(val), val, sep = ' ', end = '\n')
        return wraper
    return decorator


@decorator_with_arguments('string')
def function1(a, b):
    return a ** b

function1(2, 10)