class Printer:
    def print(self):
        pass

class Scanner:
    def scan(self):
        pass

class MultiFunctionDevice(Printer, Scanner):
    def print(self):
        return "Printing"

    def scan(self):
        return "Scanning"

class SimplePrinter(Printer):
    def print(self):
        return "Printing"

def use_printer(printer):
    print(printer.print())

simple_printer = SimplePrinter()
use_printer(simple_printer)
