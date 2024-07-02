before = ['дом', 'квартира', 'поместье']
after = list(map(lambda x: ''.join(reversed(x)), before))
print(before, "\n", after)