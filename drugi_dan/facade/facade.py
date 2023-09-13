from drugi_dan.chain.modifiers import *
# facade
class JenkinsJob:
    def __init__(self, issue):
        self.job = Job(issue)

        self.rootJob = JobStep(self.job)

        self.rootJob.add_step(StaticStep(self.job))
        self.rootJob.add_step(BuildStep(self.job))
        self.rootJob.add_step(UnitTestStep(self.job))
        self.rootJob.add_step(PackingStep(self.job))
        self.rootJob.add_step(DeployStep(self.job))

    def handle(self):
        print(self.job)
        self.rootJob.handle()  # apply modifiers
        print(self.job)


if __name__ == "__main__":
    jj = JenkinsJob(123)
    jj.handle()