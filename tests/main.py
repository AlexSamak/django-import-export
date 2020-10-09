import pprint

a = {'a': 10, 'b': 20, 'c': 30, 'd': 30}

b = {'a': 30, 'b': 10, 'c': 20, 'e': 50}

a.update(b)

pprint.pprint(a)

