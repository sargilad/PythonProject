class MySimpleClass:

    def __init__(self):
        print('init name')
        self._name = ""

    def get_name(self):
        print("Getting name")
        return self._name

    def set_name(self, name):
        print("set name")
        self._name = name

    def del_name(self):
        print("delete name")
        del self._name

    prop = property(get_name, set_name, del_name)
