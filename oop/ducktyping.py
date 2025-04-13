class Duck(object):
    def __init__(self, name):
        self.name = name

    def walk(self):
        print("walking,,,")

    def quack(self):
        print("quack quack....")

    def fly(self):
        print("Whee!!")

class Penguin:
    def __init__(self, name):
        self.name = name

    def walk(self):
        print("walking,,,")

    def quack(self):
        print("quack quack...??")

    def swim(self):
        print("swimming!")

def walk_and_quak(duck):
    duck.walk()
    duck.quack


if __name__ == "__main__":
    donald = Duck("Donald")
    pingu = Penguin("Pingu")
    donald.walk()
    donald.quack()
    pingu.walk()
    pingu.quack()