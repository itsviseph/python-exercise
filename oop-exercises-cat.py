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
