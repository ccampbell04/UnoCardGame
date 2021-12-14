from Output import Output

class TestOutput(Output):

    listOfTestOutputs = []

    def setListOfTestOutput(self, listOfOutputs):
        self.listOfTestOutputs = listOfOutputs

    def display(self, message):
        return self.listOfTestOutputs.append()