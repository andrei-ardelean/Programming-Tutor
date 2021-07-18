import fileinput
import subprocess
import re

from model import Model


class Controller:
    def __init__(self):
        self.model = Model()
        # initializing variables
        self.currentProject = self.model.getCurrentProject()
        self.tests = []
        self.noPassed = 0
        self.noFailed = 0
        self.noError = 0
        self.runtimeErrors = []
        self.failedTestIndexes = []
        self.testErrorMessages = [test["errorMessage"] for test in self.currentProject["tests"]]
        self.testInputs = [test["data"].replace("; ", "<br>") for test in self.currentProject["tests"]]

    def reinitialize(self):
        """
        Reinitialize variables
        """
        self.currentProject = self.model.getCurrentProject()
        self.tests = []
        self.noPassed = 0
        self.noFailed = 0
        self.noError = 0
        self.runtimeErrors = []
        self.failedTestIndexes = []
        self.testErrorMessages = [test["errorMessage"] for test in self.currentProject["tests"]]
        self.testInputs = [test["data"].replace("; ", "<br>") for test in self.currentProject["tests"]]

    def getProjects(self):
        """
        Get all projects
        :return: list of objects
        """
        return self.model.getProjects()

    def getCurrentProject(self):
        """
        Get current project
        :return: object - current project
        """
        return self.model.getCurrentProject()

    def setCurrentProject(self, name):
        """
        Set current project
        :param name: name of the project
        :return: object - new current project
        """
        return self.model.setCurrentProject(name)

    def getOutputFilename(self):
        """
        Get output filename
        :return: string
        """
        return self.model.getOutputFilename()

    def getCompileFilename(self):
        """
        Get compile filename
        :return: string
        """
        return self.model.getCompileFilename()

    def getTests(self):
        """
        Get tests
        :return: list of strings
        """
        return self.tests

    def getNoPassed(self):
        """
        Get number of passed tests
        :return: int
        """
        return self.noPassed

    def getNoFailed(self):
        """
        Get number of failed tests
        :return: int
        """
        return self.noFailed

    def getNoError(self):
        """
        Get number of tests with error
        :return: int
        """
        return self.noError

    def getRuntimeErrors(self):
        """
        Get errors occurred at runtime
        :return: list of strings
        """
        return self.runtimeErrors

    def getFailedTestIndexes(self):
        """
        Get indexes of failed tests
        :return: list of integers
        """
        return self.failedTestIndexes

    def getTestErrorMessages(self):
        """
        Get error message of each test in test-suite
        :return: list of strings
        """
        return self.testErrorMessages

    def getTestInputs(self):
        """
        Get input data of each test in test-suite
        :return: list of strings
        """
        return self.testInputs

    def getHint(self):
        """
        Get hint - error message of the first failed test
        :return: string - hint
        """
        return self.testErrorMessages[self.failedTestIndexes[0]]

    def saveCodeToFile(self, sourceCode):
        """
        Save code to implementation file
        """
        filename = self.getCurrentProject()["implementationFilename"]
        with open(filename, 'w') as f:
            f.write(sourceCode)
        # replace tabs with spaces to avoid indentation errors
        with fileinput.FileInput(filename, inplace=True) as file:
            for line in file:
                print(line.replace('\t', ' ' * 4), end='')

    def verifyFunctionName(self):
        """
        Verify if function has the name mentioned in requirement
        :return: True if it has, False otherwise
        """
        with open(self.getCurrentProject()["implementationFilename"], 'r') as f:
            # first written line should contain function signature
            line = f.read().strip()
            while line == "":
                line = f.read().strip()
            signature = self.getCurrentProject()["functionDefinition"]
            functionName = signature.split("(")[0] + "("
            if functionName in line:
                return True
            return False

    def extractCompilationErrors(self):
        """
        Verify if compilation file is empty
        :return: pair of boolean (True/False) and string (error)
        """
        with open(self.getCompileFilename(), 'r') as f:
            error = f.read().strip()
            if error != "":
                lineNumbers = re.findall('line [0-9]+', error)
                line = ""
                if lineNumbers:
                    line = lineNumbers[-1].split(" ")[1]
                if "unindent does not match" in error or "unindent" in error or "expected an indented block" in error:
                    errorMessage = "Linia " + line + ": Programul conține o eroare de indentare! Încearcă să " \
                                                     "păstrezi o coerență între taburi/spații."
                elif "invalid syntax" in error:
                    errorMessage = "Linia " + line + ": Programul conține o eroare de sintaxă!"
                else:
                    errorMessage = "Linia " + line + ": Programul tău conține o eroare de compilare!"
                return errorMessage
            else:
                return ""

    def runTests(self):
        """
        Run test suite over implementation wrt a timeout
        If timeout is exceeded, it means program has infinite loop
        :return: False if timeout is exceeded, True otherwise
        """
        try:
            testPath = self.getCurrentProject()["testPath"]
            subprocess.run(['python', testPath], timeout=1.5)
            return False
        except subprocess.TimeoutExpired:
            return True

    def extractTests(self, firstLine):
        """
        Extract tests result and compute how many of them are passed/failed/error
        """
        for index, value in enumerate(firstLine):
            testNumber = "Test #"
            if index < 9:
                testNumber += "0"
            if value == ".":
                self.tests.append((testNumber + str(index + 1) + ": PASSED.", 0))
                self.noPassed += 1
            elif value == "F":
                self.tests.append((testNumber + str(index + 1) + ": FAILED.", 1))
                self.failedTestIndexes.append(index)
                self.noFailed += 1
            elif value == "E":
                self.tests.append((testNumber + str(index + 1) + ": ERROR.", 2))
                self.noError += 1

    def extractRuntimeErrors(self, runtimeErrorLines):
        """
        Extract different types of runtime errors
        """
        for errorLine in runtimeErrorLines:
            # Wrong function definition (less or more parameters given)
            if (errorLine[0].startswith("TypeError: ") and ("positional arg" and "were given" in errorLine[0])) \
                    or (errorLine[0].startswith("TypeError: ") and (
                    "missing" and "required positional argument" in errorLine[0])):
                runtimeError = "Funcția scrisă de tine nu corespunde definiției cerute în cerință."
                self.runtimeErrors.append(runtimeError)
            # Uninitialized variable
            elif errorLine[0].startswith("UnboundLocalError: local variable") and "referenced before assignment" in \
                    errorLine[0]:
                var = errorLine[0].split("'")[1]
                runtimeError = "Linia " + errorLine[1] + ": Ai folosit variabila '" + var + "' înainte s-o " \
                                                                                            "inițializezi. "
                self.runtimeErrors.append(runtimeError)
            # Index Error
            elif errorLine[0].startswith("IndexError: list index out of range"):
                runtimeError = "Linia " + errorLine[1] + ": Ai o eroare de indexare. Indexul pus de tine e în afara " \
                                                         "lungimii listei. "
                self.runtimeErrors.append(runtimeError)
            # Name Error
            elif errorLine[0].startswith("NameError: name") and " is not defined" in errorLine[0]:
                var = errorLine[0].split("'")[1]
                runtimeError = "Linia " + errorLine[1] + ": Variabila " + var + " nu este definită."
                self.runtimeErrors.append(runtimeError)
            # Division by 0
            elif errorLine[0].startswith("ZeroDivisionError: integer division or modulo by zero")\
                    or errorLine[0].startswith("ZeroDivisionError: float modulo"):
                runtimeError = "Linia " + errorLine[1] + ": Se produce împărțire la 0, ceea ce e nepermis."
                self.runtimeErrors.append(runtimeError)
            # Iterating an integer
            elif errorLine[0].startswith("TypeError: 'int' object is not iterable"):
                runtimeError = "Linia " + errorLine[1] + ": Variabilele de tipul int nu pot fi iterate."
                self.runtimeErrors.append(runtimeError)
            # Others
            else:
                runtimeError = "Linia " + errorLine[1] + ": " + errorLine[0]
                self.runtimeErrors.append(runtimeError)

    def computeTestResults(self):
        """
        Compute tests result
        """
        # reinitialize variables
        self.reinitialize()

        # read output file
        with open(self.getOutputFilename(), 'r') as f:
            allLines = f.readlines()
            # first line contains unittest results
            firstLine = [ch for ch in allLines[0].strip()]

            # compute how many are passed/failed/error
            self.extractTests(firstLine)

            # if there are runtime errors
            if self.noError != 0:
                # get lines with runtime errors
                runtimeErrorLines = []
                for index, error in enumerate(allLines):
                    # find error line
                    lines = re.findall('line [0-9]+', error)
                    if lines:
                        line = lines[-1].split(" ")[1]
                    # find error message
                    if "Error" in error:
                        error = error.strip()
                        if error not in runtimeErrorLines:
                            runtimeErrorLines.append((error, line))

                # get runtime errors
                self.extractRuntimeErrors(runtimeErrorLines)
