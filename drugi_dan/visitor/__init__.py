from __future__ import generators
import random

class Issue(object):
    def __init__(self, number):
        self.number = number

    def accept(self, visitor):
        visitor.visit(self)
    def __str__(self):
        return f"Issue {self.number}"


class Person:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Person {self.name}"

class Worker(Person):
    def visit(self, issue):
        # issue.working(self)
        print(issue, "work by", self)

class Reviewer(Person):
    def visit(self, issue):
        print(issue, "reviewed by", self)

worker = Worker("Mane")
reviewer = Reviewer("Dane")
issue = Issue(123)
issue.accept(worker)
issue.accept(reviewer)
