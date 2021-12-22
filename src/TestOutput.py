from Output import Output

class TestOutput(Output):

    listOfTestOutputs = []

    def display(self, message):
        return self.listOfTestOutputs.append(message)

    def clear(self):
        self.listOfTestOutputs = []
