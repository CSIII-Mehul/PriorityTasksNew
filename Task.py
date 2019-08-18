class Task:
    def __init__(self, name, priority):
        self.name = name
        self.priority = priority

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def priority(self):
        return self._priority

    @priority.setter
    def priority(self, value):
        self._priority = value




if __name__ == "__main__":

    t = Task("Homework", 1)
