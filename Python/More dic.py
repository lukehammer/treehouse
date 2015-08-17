__author__ = 'luke'
dicts = [
    {'name': 'Michelangelo',
     'food': 'PIZZA'},
    {'name': 'Garfield',
     'food': 'lasanga'},
    {'name': 'Walter',
     'food': 'pancakes'},
    {'name': 'Galactus',
     'food': 'worlds'}
]

string = "Hi, I'm {name} and I love to eat {food}!"

def string_factory(list_dics,string):
  to_return = []
  for dic in list_dics:
    finished_string = string.format(**dic)
    to_return.append(finished_string)
  return to_return

print string_factory(dicts,string)