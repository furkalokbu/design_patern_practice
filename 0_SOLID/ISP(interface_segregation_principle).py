from abc import abstractmethod


class Machine:
    def print(self, document):
        raise NotImplementedError
    def scan(self, document):
        raise NotImplementedError
    def fax(self, document):
        raise NotImplementedError


class MultiFunctionPrinter(Machine):
    def print(self, document):
        pass
    def scan(self, document):
        pass
    def fax(self, document):
        pass


class OldFashionedPrinter(Machine):
    def print(self, document):
        pass
    def fax(self, document):
        pass
    def scan(self, document):
        raise NotImplementedError('Printer cannot scan!')


class Printer:
    @abstractmethod
    def print(self, document):
        pass


class Scanner:
    @abstractmethod
    def scan(self, document):
        pass


class Fax:
    @abstractmethod
    def fax(self, document):
        pass

class MyPrinter(Printer):
    def print(self, document):
        print(document)


class MultiFunctionDevice(Printer, Scanner):
    @abstractmethod
    def print(self, document):
        pass

    @abstractmethod
    def scan(self, document):
        pass


class MultiFunctionMachine(MultiFunctionDevice):

    def __inut__(self, scanner, printer):
        self.scanner = scanner
        self.printer = printer

    def print(self, document):
        self.printer.print(document)

    def scan(self, document):
        self.scanner.scan(document)