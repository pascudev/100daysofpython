from collections import defaultdict, namedtuple, Counter, deque

cars = {
    'Ford': ['Falcon', 'Focus', 'Festiva', 'Fairlane'],
    'Holden': ['Commodore', 'Captiva', 'Barina', 'Trailblazer'],
    'Nissan': ['Maxima', 'Pulsar', '350Z', 'Navara'],
    'Honda': ['Civic', 'Accord', 'Odyssey', 'Jazz'],
    'Jeep': ['Grand Cherokee', 'Cherokee', 'Trailhawk', 'Trackhawk']
}

def get_all_jeeps(dict):
    for k, v in dict.items():
        if k == 'Jeep':
            return v
    return v

def get_first_model_each_manufacturer(dict):
    company_model = defaultdict()
    for k, v in dict.items():
        company_model[k] = v[0]
    return company_model

def get_all_matching_models(dict):
    search_str = 'trail'
    words = []
    for k, v in dict.items():
        for l in v:
            if search_str in l.lower():
                words.append(l)
    return words

def sort_car_models(dict):
    alph_sort = defaultdict()
    for k, v in dict.items():
        alph_sort[k] = sorted(v)
    return alph_sort

test = sort_car_models(cars)

print(test)