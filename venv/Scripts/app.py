str = "gilad"
print(str[::-1])
print("the {q} {b} {f}".format(q='quick', b='brown', f='fox'))

# f-strings example
nnn = "asdasdas"
print(f"the {nnn}")

name = "gilad"
age = 4
print(f"{name} is {age} years old")

x = [
    'a',
    'b',
    {
        'foo': 1,
        'bar':
            {
                'x': 10,
                'y': 20,
                'z': 30
            },
        'baz': 3
    },
    'c',
    'd'
]

keys = x[2].keys()
print('foo' in keys)

d = {'foo': 100, 'bar': 200, 'baz': 300}
d.pop("bar")
print(d)
d2 = {}
d2.update(d)
print(d2)
