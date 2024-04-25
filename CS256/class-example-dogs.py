class Dog:
    def __init__(self, name, color):
        self.name = name
        self.color = color
        self.tricks = []

#getters and setters
    def get_name(self):
        return self.name
    def set_name(self,new_name):
        self.name = new_name

    def get_color(self):
        return self.color
    def set_color(self,new_color):
        self.color = new_color

    def get_tricks(self):
        return self.tricks

#define other methods
    def addTrick(self,trick):
        self.tricks.append(trick)

    def showTricks(self):
        for trick in self.tricks:
            print(trick)

    def showDog(self):
        print(self.name, self.color)
        self.showTricks()

#define tester
if __name__ == "__main__":
    dog1 = Dog("fido", "brown")
    dog2 = Dog("muffin", "tan")
    dog1.showDog()

    dogs = []
    dogs.append( Dog("mutt", "black and white"))
    dogs.append( dog1 )
    for d in dogs:
        d.showDog()
