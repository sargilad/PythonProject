# print("hello")
# idPublished = True
# print(idPublished)
# str = "gilad"
# print(str[::-1])
print("the {q} {b} {f}".format(q='quick', b='brown', f='fox'))
name = "gilad"
age = 3
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

print('foo' in x[2].keys())

d = {'foo': 100, 'bar': 200, 'baz': 300}
d.pop("bar")
print(d)
d2 = {}
d2.update(d)
print(d2)
