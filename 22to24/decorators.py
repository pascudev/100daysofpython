from functools import wraps


def make_html(element):
    @wraps(element)
    def wrapper():
        return f'<{s}>' #+ fn() + f'</{s}>'
    return wrapper

@make_html('p')
#@make_html('strong')
def get_text():
    return 'I code with PyBites'


print(get_text())
