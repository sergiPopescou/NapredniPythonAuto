import yaml
import os
from random import choice
from string import ascii_letters
from tdd.modules.issue import Issue, Nivo


def loadIssues(filePath=None):
    if filePath is None:
        filePath = os.sep.join([os.getcwd(), "..", "klijent_issues.yaml"])
    retval = []
    with open(filePath, 'r') as f:
        issues = list(yaml.load_all(f, Loader=yaml.SafeLoader))
        for issue_ in issues[0]["issues"]:
            nivo = Nivo.createNivo(issue_['nivo'])
            retval.append(Issue(issue_['naziv'], nivo=nivo))
    return retval


def dumpIssues(issues, filePath=None):
    if filePath is None:
        filePath = os.sep.join([os.getcwd(), "..", "klijent_issues_dump.yaml"])
    issues_dict_list = { "issues": [{"naziv": iss.__dict__["naziv"],
                                     "nivo": iss.__dict__["nivo"].name} for iss in issues]}
    with open(filePath, 'w') as f:
        f.write(yaml.dump(issues_dict_list, Dumper=yaml.SafeDumper))


def randomIssueNaziv(str_size=12):
    return ''.join(choice(ascii_letters) for x in range(str_size))


def generateIssues(amount=100, filePath=None):
    if filePath is None:
        filePath = os.sep.join([os.getcwd(), "..", "generated_issues.yaml"])
    nivoi = [e.name for e in Nivo]
    issues_dict_list = {"issues": [{"naziv": randomIssueNaziv(),
                                    "nivo": choice(nivoi)} for i in range(amount)]}
    with open(filePath, 'w') as f:
        f.write(yaml.dump(issues_dict_list, Dumper=yaml.SafeDumper))


if __name__ == "__main__":
    filePath = os.sep.join([os.getcwd(), "..", "klijent_issues.yaml"])
    issues = loadIssues(filePath)
    for i in issues:
        print(i, type(i))
    # dumpIssues(issues)
    # generateIssues()