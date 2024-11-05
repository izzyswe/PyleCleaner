# import os
# import pyinputplus as pyip
from sys import exit


class pyleCleanerModule:
    def __init__(self, fileType, fileAge, fileModified):
        self.fileType = fileType
        self.fileAge = fileAge
        self.fileModified = fileModified

    def CheckFileLastOpened(self, opened):
        pass

    def delDownloadFiles(self):
        pass

    def delTempFiles(self):
        pass

    def delRecycleBin(self):
        pass

    def fileTypeDeletion(self):
        pass

    def WelcomeConsole(self):
        print("___________ .PyleCleaner. ______________")
        print("| Choose which to clean                |")
        print("|                                      |")
        print("|  1. Temp File                        |")
        print("|  2. Downloads                        |")
        print("|  3. Recycle Bin                      |")
        print("|  4. Clean only File Type             |")
        print("|  5. Exit                             |")
        print("|______________________________________|")
        options = int(input())

        match options:
            case 1:
                self.delTempFiles()
            case 2:
                self.delDownloadFiles()
            case 3:
                self.delRecycleBin()
            case 4:
                self.fileTypeDeletion()
            case 5:
                exit(0)
                # successful exit
