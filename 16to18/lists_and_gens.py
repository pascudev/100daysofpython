import string

NAMES = ['arnold schwarzenegger', 'alec baldwin', 'bob belderbos',
         'julian sequeira', 'sandra bullock', 'keanu reeves',
         'julbob pybites', 'bob belderbos', 'julian sequeira',
         'al pacino', 'brad pitt', 'matt damon', 'brad pitt']

titled_names = [name.title() for name in NAMES]

print(titled_names)


def name_options(list):
    for l in list:
        yield f'<option value={l}>{l.title()}</option>'

get_options = name_options(NAMES)

print(list(get_options))