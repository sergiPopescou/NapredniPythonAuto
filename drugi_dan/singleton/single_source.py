import random
from drugi_dan.singleton.issue import Issue
import yaml


class DataSource:

    _instance = None
    _data = []

    def __init__(self):
        id = random.randint(1, 101)
        print('Loading issues from file')
        print(f'id = {id}')
        if not DataSource._data:
            retval = []
            with open("issues.yml", 'r') as f:
                issues = list(yaml.load_all(f, Loader=yaml.SafeLoader))
                for issue_ in issues[0]["issues"]:
                    retval.append(Issue(issue_['number'], issue_['difficulty']))
                DataSource._data = retval

    # redefine allocator
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(DataSource, cls)\
               .__new__(cls, *args, **kwargs)
        return cls._instance

D1 = DataSource()
D2 = DataSource()

print(D1 == D2)
