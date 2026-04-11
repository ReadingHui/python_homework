import logging

logger = logging.getLogger(__name__ + "parameter_log")
logger.setLevel(logging.INFO)
logger.addHandler(logging.FileHandler('./decorator.log', 'a'))

# Task 1: Writing and Testing a Decorator
def logger_decorator(func):
    def wrapper(*args, **kwargs):
        name = func.__name__
        logger.log(logging.INFO, f'function: {name}')
        pos_param = list(args)
        logger.log(logging.INFO, f'positional parameters: {pos_param}')
        kw_param = dict(kwargs)
        logger.log(logging.INFO, f'keyword parameters: {kw_param}')
        result = func(*args, **kwargs)
        logger.log(logging.INFO, f'return: {result}')
        return result
    return wrapper

@logger_decorator
def nothing_function():
    print(f'Hello, World!')

@logger_decorator
def true_function(*args):
    return True

@logger_decorator
def kw_func(**kwargs):
    return logger_decorator

def main():
    nothing_function()
    true_function(1, 2, 'one', True, [1, 2])
    kw_func(kw1='x', kw2=2)

if __name__ == '__main__':
    main()