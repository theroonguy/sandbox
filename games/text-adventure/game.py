class Item():
    def __init__(self, name, description, value):
        self.name=name
        self.description=description
        self.value=value

    def __str__(self):
        return "{}\n--------\n{}\nValue: {}\n".format(self.name, self.description, self.value)

class Gold(Item):
    def __init__(self, amt):
        self.amt=amt
        super().__init__(name="Gold",
                         description="A round coin with {} stamped on the front.".format(str(self.amt)),
                         value=self.amt)

class Weapon(Item):
    def __init__(self, name, description, value, damage):
        self.damage=damage
        super().__init__(name, description, value)

    def __str__(self):
        return "{}\n--------\n{}\nValue: {}\nDamage: {}\n".format(self.name, self.description, self.value, self.damage)

class Dagger(Weapon):
    def __init__(self):
        super().__init__(name="Dagger",
                         description="A small dagger.",
                         value=10,
                         damage=10)
        
class Enemy():
    def __init__(self, name, hp, damage):
        self.name=name
        self.hp=hp
        self.damage=damage

    def is_alive(self):
        return self.hp &amp;gt; 0

class Ogre(Enemy):
    def __init__(self):
        super().__init__(name="Ogre",
                         hp=30,
                         damage=15)
