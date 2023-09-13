from enum import Enum

class Seniority(Enum):
    JUNIOR = 1
    MEDIOR = 2
    SENIOR = 3

class Person:

    def __init__(self, name, seniority):
        self.name = name
        self.seniority = seniority
        self.issue = None

    def addIssue(self, issue):
        self.issue = issue