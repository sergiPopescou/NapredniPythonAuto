"""
Chain of responsibility
- A chain of components who all get a chance to process a command
  or a query, optionally having default processing implementation
  and an ability to terminate the processig chain.

Command Query Separation
- Command = asking for an action or change (e.g., please set your
  attack value to 2)
- Query = asking for information (e.g., please give me your attack)
- CQS = having separate means of sending commands and queries
"""


class Job:
    def __init__(self, issue):
        self.issue = issue
        self.status = "NOT STARTED"

    def __str__(self):
        return f'{self.issue} in status {self.status}'


class JobStep:
    def __init__(self, job):
        self.job = job
        self.next_step = None

    def add_step(self, step):
        if self.next_step:
            self.next_step.add_step(step)
        else:
            self.next_step = step

    def handle(self):
        if self.next_step:
            self.next_step.handle()


class StaticStep(JobStep):
    def handle(self):
        print(f'static analysis of code on job {self.job.issue}')
        self.job.status = "STATIC"
        # if fail then no super handle and status failed
        super().handle()


class BuildStep(JobStep):
    def handle(self):
        print(f'Building {self.job.issue}...')
        self.job.status = "BUILD"
        # if fail then no super handle
        super().handle()
class UnitTestStep(JobStep):
    def handle(self):
        print(f'Testing {self.job.issue}...')
        self.job.status = "TEST"
        # if fail then no super handle
        super().handle()

class PackingStep(JobStep):
    def handle(self):
        print(f'Packing {self.job.issue}...')
        self.job.status = "PACK"
        # if fail then no super handle
        super().handle()

class DeployStep(JobStep):
    def handle(self):
        print(f'Deploying {self.job.issue}...')
        self.job.status = "DEPLOYED"
        # if fail then no super handle
        super().handle()


if __name__ == '__main__':
    job = Job('Issue-112')
    print(job)

    rootJob = JobStep(job)

    rootJob.add_step(StaticStep(job))
    rootJob.add_step(BuildStep(job))
    rootJob.add_step(UnitTestStep(job))
    rootJob.add_step(PackingStep(job))
    rootJob.add_step(DeployStep(job))

    rootJob.handle()  # apply modifiers
    print(job)