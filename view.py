from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import QDir
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QMainWindow, QFileDialog, QTableWidgetItem, QHeaderView, \
    QDesktopWidget
from PyQt5.uic import loadUi

from controller import Controller


class View(QMainWindow):
    def __init__(self):
        super(View, self).__init__()
        self.controller = Controller()
        # load user interface
        loadUi("view/mainWindow.ui", self)
        self.initUI()

    def initUI(self):
        """
        Initialize UI elements
        """
        self.setWindow()
        self.setEvents()
        self.setProjectArea()
        self.setCodeArea()
        self.setTestArea()
        self.setFeedbackArea()

    def setWindow(self):
        """
        Set window properties
        """
        self.setGeometry(100, 100, 1370, 990)
        self.setWindowTitle("Programming Tutor")
        self.setWindowIcon(QIcon("icons/tutor.png"))
        # centering the window
        qr = self.frameGeometry()  # geometry of the main window
        cp = QDesktopWidget().availableGeometry().center()  # center point of screen
        qr.moveCenter(cp)  # move rectangle's center point to screen's center point
        self.move(qr.topLeft())  # centering

    def setEvents(self):
        """
        Set button events
        """
        self.importFileBtn.clicked.connect(self.importFile)
        self.importFileBtn.setCursor(QtCore.Qt.PointingHandCursor)
        self.generateFeedbackBtn.clicked.connect(self.generateFeedback)
        self.generateFeedbackBtn.setCursor(QtCore.Qt.PointingHandCursor)
        self.saveCodeBtn.clicked.connect(self.saveCodeToFile)
        self.saveCodeBtn.setCursor(QtCore.Qt.PointingHandCursor)
        self.hintBtn.clicked.connect(self.generateHint)
        self.hintBtn.setCursor(QtCore.Qt.PointingHandCursor)
        self.solvingHintBtn.clicked.connect(self.generateSolvingHint)
        self.solvingHintBtn.setCursor(QtCore.Qt.PointingHandCursor)

    def setProjectArea(self):
        """
        Set project area fields
        """
        for row, project in enumerate(self.controller.getProjects()):
            self.projectsList.addItem(project['name'])
            if project["difficulty"] == "easy":
                self.projectsList.item(row).setIcon((QIcon("icons/greenSquare.png")))
            elif project["difficulty"] == "medium":
                self.projectsList.item(row).setIcon((QIcon("icons/orangeSquare.png")))
            elif project["difficulty"] == "hard":
                self.projectsList.item(row).setIcon((QIcon("icons/redSquare.png")))
        self.projectsList.setCurrentRow(0)
        self.setProjectDescription(self.controller.getCurrentProject())
        self.projectsList.currentItemChanged.connect(self.changeProject)
        self.projectsList.setCursor(QtCore.Qt.PointingHandCursor)

    def setCodeArea(self):
        """
        Set code area fields
        """
        with open(self.controller.getCurrentProject()["implementationFilename"], 'r') as f:
            data = f.read()
            self.codeTextEdit.setPlainText(data)
        self.codeTextEdit.setTabStopWidth(self.codeTextEdit.fontMetrics().width(' ' * 6))
        self.progressBar.setVisible(False)

    def setTestArea(self):
        """
        Set test area fields
        """
        self.testTabWidget.tabBar().setCursor(QtCore.Qt.PointingHandCursor)
        self.refreshTestArea()

    def setFeedbackArea(self):
        """
        Set feedback area fields
        """
        self.feedbackTabWidget.tabBar().setCursor(QtCore.Qt.PointingHandCursor)
        self.refreshFeedbackArea()
        self.solvingHintLabel.setText("")

    def importFile(self):
        """
        Import Python file into the code area zone
        """
        dialog = QFileDialog()
        dialog.setFileMode(QFileDialog.AnyFile)
        dialog.setFilter(QDir.Files)
        if dialog.exec_():
            filename = dialog.selectedFiles()
            if filename[0].endswith('.py'):
                with open(filename[0], 'r') as f:
                    data = f.read()
                    self.codeTextEdit.setPlainText(data)

    def saveCodeToFile(self):
        """
        Save source code to implementation file as a backup
        """
        sourceCode = self.codeTextEdit.toPlainText()
        self.controller.saveCodeToFile(sourceCode)

    def setProjectDescription(self, project):
        """
        Format project description fields
        """
        self.projectNameLabel.setText(project["name"])
        self.projectRequirementLabel.setText(project["requirement"])
        self.functionSignatureLabel.setText(project["functionDefinition"])
        self.projectInputLabel.setText(project["input"])
        self.projectOutputLabel.setText(project["output"])
        if project["difficulty"] == "easy":
            self.projectDifficultyLabel.setPixmap(QPixmap("icons/greenSquare.png"))
            self.projectDifficultyLabel.setToolTip('<b style="color:black;font-size:14px;">Dificultate UȘOARĂ</b>')
        elif project["difficulty"] == "medium":
            self.projectDifficultyLabel.setPixmap(QPixmap("icons/orangeSquare.png"))
            self.projectDifficultyLabel.setToolTip('<b style="color:black;font-size:14px;">Dificultate MEDIE</b>')
        elif project["difficulty"] == "hard":
            self.projectDifficultyLabel.setPixmap(QPixmap("icons/redSquare.png"))
            self.projectDifficultyLabel.setToolTip('<b style="color:black;font-size:14px;">Dificultate GREA</b>')

    def changeProject(self):
        """
        Change current selected project
        """
        # set project description
        name = self.projectsList.currentItem().text()
        self.setProjectDescription(self.controller.setCurrentProject(name))
        # refresh test and feedback areas
        self.refreshTestArea()
        self.refreshFeedbackArea()
        self.solvingHintLabel.setText("")
        # get source code saved in implementation file
        with open(self.controller.getCurrentProject()["implementationFilename"], "r") as f:
            self.codeTextEdit.setPlainText(f.read())

    def refreshTestArea(self):
        """
        Clear fields in test area
        """
        self.testsResultIcon.clear()
        self.testsResult.setText("")
        self.totalNoTests.setText("")
        self.noPassedTests.setText("")
        self.noFailedTests.setText("")
        self.testsTable.clear()
        self.testsTable.setRowCount(0)

    def refreshFeedbackArea(self):
        """
        Clear fields in feedback area
        """
        self.feedbackResultIcon.clear()
        self.feedbackResultLabel.setText("")
        self.wizardIcon.clear()
        self.wizardHelpLabel.setText("")
        self.hintLabel.setText("")
        self.hintLabel.setStyleSheet("background-color: #1C2833")
        self.hintBtn.setVisible(False)
        # self.solvingHintLabel.setText("")
        self.crystalBallIcon.setPixmap(QPixmap("icons/crystalBallIcon.png"))
        self.crystalBallIcon.setScaledContents(True)

    def progressBarAnimation(self):
        """
        Create progress bar animation for loading effect
        """
        self.progressBar.setVisible(True)
        self.progressBar.setValue(0)
        completed = 0
        while completed < 100:
            completed += 0.0001
            self.progressBar.setValue(completed)
        self.progressBar.setVisible(False)

    def setTestTableView(self, tests, testInputs):
        """
        Fill table view with tests
        """
        # compute no rows and cols
        if len(tests) % 3 == 0:
            noRows = len(tests) // 3
        else:
            noRows = len(tests) // 3 + 1
        noColumns = 3
        # set no rows and cols
        self.testsTable.setRowCount(noRows)
        self.testsTable.setColumnCount(noColumns)
        for index, pair in enumerate(tests):
            test = pair[0]
            testType = pair[1]
            item = QTableWidgetItem(test)
            item.setFlags(QtCore.Qt.ItemIsEnabled)
            row = index // 3
            column = index % 3
            if testType == 0:  # passed
                item.setForeground(QtGui.QColor("#18CB3B"))
                item.setToolTip('<b><p style="color:black;font-size:14px"><span style="color:#158A02">TEST '
                                'PASSED:</span><br>{}</p></b>'.format(testInputs[index]))
            elif testType == 1:  # failed
                item.setForeground(QtGui.QColor("#E70026"))
                item.setToolTip('<b><p style="color:black;font-size:14px"><span style="color:#E70026">TEST '
                                'FAILED:</span><br>{}</p></b>'.format(testInputs[index]))
            self.testsTable.setItem(row, column, item)
        # table will fit the screen horizontally
        self.testsTable.horizontalHeader().setStretchLastSection(True)
        self.testsTable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        # hide horizontal and vertical header
        self.testsTable.horizontalHeader().hide()
        self.testsTable.verticalHeader().hide()

    def fillTestArea(self, tests, noPassed, noFailed):
        """
        Fill test area with tests
        """
        if len(tests) != noPassed:
            self.testsResult.setText("Soluția ta NU a trecut toate testele!")
            self.testsResult.setStyleSheet("color: #EC1A1A")
            self.testsResultIcon.setPixmap(QPixmap("icons/incorrectIcon.png"))
            self.testsResultIcon.setScaledContents(True)
        else:
            self.testsResult.setText("Soluția ta este corectă!")
            self.testsResult.setStyleSheet("color: #18CB3B")
            self.testsResultIcon.setPixmap(QPixmap("icons/correctIcon.png"))
            self.testsResultIcon.setScaledContents(True)
        self.totalNoTests.setText("Nr de teste rulate: " + str(len(tests)))
        self.noPassedTests.setText("PASSED: " + str(noPassed))
        self.noFailedTests.setText("FAILED:  " + str(noFailed))

    def fillFeedbackArea(self, noFailed):
        """
        Fill feedback area fields
        """
        # if solution has no failed tests, it's considered to be correct
        if noFailed != 0:
            self.feedbackResultLabel.setText("Soluția ta nu este corectă. Mai încearcă.")
            self.feedbackResultLabel.setStyleSheet("color: #EC1A1A")
            self.feedbackResultIcon.setPixmap(QPixmap("icons/incorrectIcon.png"))
            self.feedbackResultIcon.setScaledContents(True)
            self.wizardIcon.setPixmap(QPixmap("icons/wizardIcon.png"))
            self.wizardIcon.setScaledContents(True)
            self.wizardHelpLabel.setText("Ai tot încercat și te-ai blocat?")
            self.wizardHelpLabel.setStyleSheet("color: #ffffff")
            self.hintBtn.setVisible(True)
            self.hintLabel.setStyleSheet("background-color: #212F3D; color: #B562FF;")
        else:
            self.feedbackResultLabel.setText("Soluția ta este corectă. Felicitări, nota 10!")
            self.feedbackResultLabel.setStyleSheet("color: #18CB3B")
            self.feedbackResultIcon.setPixmap(QPixmap("icons/correctIcon.png"))
            self.feedbackResultIcon.setScaledContents(True)

    def hasCompilationErrors(self, error):
        """
        Verify if program contains compilation errors
        :return: boolean - True if contains, False otherwise
        """
        if error != "":
            self.feedbackResultLabel.setText(error)
            self.feedbackResultLabel.setStyleSheet("color: #EC1A1A")
            self.feedbackResultIcon.setPixmap(QPixmap("icons/errorIcon.png"))
            self.feedbackResultIcon.setScaledContents(True)
            return True
        else:
            return False

    def hasRuntimeErrors(self, runtimeErrors):
        """
        Verify if program contains runtime errors and show the first one
        :param runtimeErrors: list of strings - runtime error messages
        :return: boolean - True if contains, False otherwise
        """
        if len(runtimeErrors) > 0:
            error = runtimeErrors[0]
            self.feedbackResultLabel.setText(error)
            self.feedbackResultLabel.setStyleSheet("color: #EC1A1A")
            self.feedbackResultIcon.setPixmap(QPixmap("icons/errorIcon.png"))
            self.feedbackResultIcon.setScaledContents(True)
            return True
        return False

    def generateHint(self):
        """
        Generate hint for program repair
        """
        hint = self.controller.getHint()
        self.hintLabel.setText(hint)

    def generateSolvingHint(self):
        """
        Generate a general algorithm for solving selected project
        """
        hint = self.controller.getCurrentProject()["algorithm"]
        self.solvingHintLabel.setText(hint)

    def generateFeedback(self):
        """
        Generate feedback
        """
        self.generateTestFeedback()

    def generateTestFeedback(self):
        """
        Generate feedback based on test cases
        """
        # refresh test and feedback area
        self.refreshTestArea()
        self.refreshFeedbackArea()
        # change tab pages
        self.feedbackTabWidget.setCurrentIndex(0)
        self.testTabWidget.setCurrentIndex(0)
        # save source code
        self.saveCodeToFile()
        # create progress bar animation
        self.progressBarAnimation()

        # verify function name
        isFunctionNameOk = self.controller.verifyFunctionName()
        if not isFunctionNameOk:
            self.feedbackResultLabel.setText("Funcția scrisă de tine nu corespunde definiției cerute în cerință.")
            self.feedbackResultLabel.setStyleSheet("color: #EC1A1A")
            self.feedbackResultIcon.setPixmap(QPixmap("icons/errorIcon.png"))
            self.feedbackResultIcon.setScaledContents(True)
            return

        # run tests and verify if program goes into infinite loop
        isInfiniteProgram = self.controller.runTests()

        if isInfiniteProgram:
            self.feedbackResultLabel.setText("Programul tău conține o buclă infinită.")
            self.feedbackResultLabel.setStyleSheet("color: #EC1A1A")
            self.feedbackResultIcon.setPixmap(QPixmap("icons/errorIcon.png"))
            self.feedbackResultIcon.setScaledContents(True)
            return

        # verify if program contains COMPILATION ERRORS
        error = self.controller.extractCompilationErrors()
        if self.hasCompilationErrors(error):
            return

        # get tests result
        self.controller.computeTestResults()
        noPassed = self.controller.getNoPassed()
        noFailed = self.controller.getNoFailed()
        runtimeErrors = self.controller.getRuntimeErrors()
        tests = self.controller.getTests()
        testInputs = self.controller.getTestInputs()

        # verify if program contains RUNTIME ERRORS
        if self.hasRuntimeErrors(runtimeErrors):
            return

        # fill test and feedback areas
        self.setTestTableView(tests, testInputs)
        self.fillTestArea(tests, noPassed, noFailed)
        self.fillFeedbackArea(noFailed)
