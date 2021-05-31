str = "gilad"
print(str[::-1])
print("the {q} {b} {f}".format(q='quick', b='brown', f='fox'))

# f-strings example
nnn="asdasdas"
print(f"the {nnn}")

name = "gilads"
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


# sdfsdfsd
def myMethod(par1, par2, dflt=1, dflt2=2):
    """Form a complex number.

        Keyword arguments:
        real -- the real part (default 0.0)
        imag -- the imaginary part (default 0.0)
        retun -- sum
        """
    if type(par1) == int and type(par2) == int:
        sum = par1 * par2
        return sum


print(myMethod(par1=3, par2=4))
print(myMethod.__doc__)

myTuple = (1, "2"), (3.0, 400)
for element in myTuple:
    print(element)

num3, num4 = "as", 1

str = {'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1}


def count_chars(magic_str):
    dic = dict()
    for letter in magic_str:
        if magic_str.count(letter) > 0:
            dic[letter] = magic_str.count(letter)

    return dic


chars = count_chars("abasdasd asd asasd asdc")
for char in chars.keys():
    print(chars[char])
