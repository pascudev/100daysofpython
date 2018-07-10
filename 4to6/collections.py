from collections import defaultdict, namedtuple, Counter, deque
import csv
import random
from urllib.request import urlretrieve

user = ('pascu', 'dev')

print(f'{user[0]} is a {user[1]}')


#NAMEDTUPLES!
#se usan para definir clases sin metodos, se crea una variable (Users) del tipo namedtuple a la cual se le asigna el nombre de la namedtuple
# 'Users' (el primer parametro) y despues sus atributos (name, role, passion)

User = namedtuple('User', 'name role passion')
user = User(name='Santiago', role='QA', passion='Music')

print(user.name)
print(user.role)
print(user.passion)

print(f'{user.name} works as a {user.role}, but his passion is {user.passion}')

