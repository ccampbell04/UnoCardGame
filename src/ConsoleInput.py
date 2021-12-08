from Input import Input

class ConsoleInput(Input):

    def getString(self, message):
        return input(message)