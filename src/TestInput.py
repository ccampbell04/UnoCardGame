from Input import Input

class TestInput(Input):

    listOfTestInputs = []

    def setListOfTestInputs(self, listOfInputs):
        self.listOfTestInputs = listOfInputs

    def getString(self, message):
        return self.listOfTestInputs.pop(0)