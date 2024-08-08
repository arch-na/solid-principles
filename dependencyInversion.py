class Keyboard:
    def type(self):
        return "Typing"

class Monitor:
    def display(self):
        return "Displaying"

class Computer:
    def __init__(self, keyboard, monitor):
        self.keyboard = keyboard
        self.monitor = monitor

    def operate(self):
        print(self.keyboard.type())
        print(self.monitor.display())

keyboard = Keyboard()
monitor = Monitor()
computer = Computer(keyboard, monitor)
computer.operate()
