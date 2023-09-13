class Issue:
    def __init__(self):
        self.state = NewState()

    def new(self):
        self.state.new(self)

    def open(self):
        self.state.open(self)

    def close(self):
        self.state.close(self)

class State:
    def new(self, issue):
        print('Issue is already in new state')

    def open(self, issue):
        print('Issue is already open')

    def close(self, issue):
        print('Issue is already closed')


class NewState(State):
    def __init__(self):
        print('Issue is in new state')

    def open(self, issue):
        print('Issue to open state...')
        issue.state = OpenState()

    def close(self, issue):
        print('Issue to closed state...')
        issue.state = CloseState()


class OpenState(State):
    def __init__(self):
        print('Issue is open')

    def new(self, issue):
        print('Issue turned back to new state')
        issue.state = NewState()

    def close(self, issue):
        print('Issue to closed state...')
        issue.state = CloseState()

class CloseState(State):
    def __init__(self):
        print('Issue is closed')

    def new(self, issue):
        print('Issue turned back to new state')
        issue.state = NewState()

    def open(self, issue):
        print('Issue turned back to open state')
        issue.state = OpenState()


if __name__ == '__main__':
    issue = Issue()

    issue.open()
    issue.open()
    issue.new()
    issue.new()
    issue.close()
    issue.open()
    issue.close()