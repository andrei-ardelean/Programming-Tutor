from data.projects import getProjects


class Model:
    def __init__(self):
        self.projects = getProjects()[:-1]  # without demo
        self.currentProject = self.projects[0]
        self.outputFilename = "file/output.txt"
        self.compileFilename = "file/compile.txt"

    def getProjects(self):
        """
        Get all projects
        :return: list of objects
        """
        return self.projects

    def getCurrentProject(self):
        """
        Get current project
        :return: object - current project
        """
        return self.currentProject

    def setCurrentProject(self, name):
        """
        Set current project
        :param name: name of the project
        :return: object - new current project
        """
        for project in self.projects:
            if project["name"] == name:
                self.currentProject = project
                return self.currentProject

    def getOutputFilename(self):
        """
        Get output filename
        :return: string
        """
        return self.outputFilename

    def getCompileFilename(self):
        """
        Get compile filename
        :return: string
        """
        return self.compileFilename

