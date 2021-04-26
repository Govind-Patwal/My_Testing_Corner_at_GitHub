def my_logger(fn_to_be_decorated):
    import logging
    logging.basicConfig(filename='{}.log'.format(fn_to_be_decorated.__name__), level=logging.INFO)

    def wrapper(*args, **kwargs):
        logging.info('Ran with args: {}, and kwargs: {}'.format(args,kwargs))
        return fn_to_be_decorated(*args, **kwargs)

    return wrapper

@my_logger
def display_info(*args, **kwargs):
    print('display_info ran with arguments ({}, {})'.format(args[0], args[1]))

display_info('John', 25)