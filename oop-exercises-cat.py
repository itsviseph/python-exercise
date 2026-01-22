class Cat:
    def __init__(self, name):
        self._name = name
        self._energy = 50

    def show_energy(self):
        print(f"{self._name} energy is {self._energy}")

    def eat(self):
        self._energy = min(100, self._energy + 30)
        print(f"{self._name} has eaten. Current energy is {self._energy}")

    def play(self):
        if self._energy >= 20:
            self._energy -= 20
            print(f"{self._name} has played. Current energy is {self._energy}")
        else:
            print(f"{self._name} is too tired to play. Energy is {self._energy}")

    def sleep(self):
        self._energy = 100
        print(f"{self._name} had a nap. Energy is restored to {self._energy}")


class LazyCat(Cat):
    def play(self):
        if self._energy >= 10:
            self._energy -= 10
            print(f"{self._name} has played lazily. Current energy is {self._energy}")
        else:
            print(f"{self._name} is too tired to play. Energy is {self._energy}")


class ActiveCat(Cat):
    def play(self):
        if self._energy >= 30:
            self._energy -= 30
            print(f"{self._name} has played Actively. Current energy is {self._energy}")
        else:
            print(f"{self._name} is too tired to play. Energy is {self._energy}")


class CatManager:
    def __init__(self, cats):
        self.cats = cats

    def play_all(self):
        for cat in self.cats:
            cat.play()

    def eat_all(self):
        for cat in self.cats:
            cat.eat()

    def sleep_all(self):
        for cat in self.cats:
            cat.sleep()


cats = [Cat("Oscar"), LazyCat("Milo"), ActiveCat("Leo")]

manager = CatManager(cats)

manager.play_all()
manager.eat_all()
manager.sleep_all()
