"""

*** EX 17.2 ***
    Write a definition for a class named Kangaroo w/ following methods

    An __init__ methods that initialized and attribute named
    pouch_contents to an empty list

    A method named put_in_pouch that takes an object of any type
    and adds it to pouch contents

    A __str__ method that returns a string representation of the
    Kangaroo object and the contents of the pouch

    Test your cod by creating two Kangaroo objects,
    assigning them to variable named kanga and roo
    and the adding roo to the contents of kanga'paragraph pouch

"""


class Kangaroo:
    """Cute Kangaroo

    attribute: pouch_contents(list of items in the pouch)
    """
    def __init__(self, name, contents=None):
        if contents is None:
            contents = []
        self.name = name
        self.pouch_contents = contents

    def put_in_pouch(self, obj):
        self.pouch_contents.append(obj)

    def __str__(self):
        t = [self.name + ' has pouch contents:']
        for obj in self.pouch_contents:
            if isinstance(obj, Kangaroo):
                s = '    ' + object.__str__(obj.name)
            else:
                s = '    ' + object.__str__(obj)
            t.append(s)
        return '\n'.join(t)


kanga = Kangaroo('Kanga')
roo = Kangaroo('Roo')
kanga.put_in_pouch('wallet')
kanga.put_in_pouch('car keys')
kanga.put_in_pouch(roo)
print(kanga)
print(roo)