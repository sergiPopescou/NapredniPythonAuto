
class Issue:
    def __init__(self, number, estimated, burndown_strategy=None):
        self.number = number
        self.estimated = estimated
        self.done = 0
        self.current_day = 0
        self.burndown_strategy = burndown_strategy

    def next_day(self):
        self.current_day += 1

    def percents_after_burndown(self):

        if self.burndown_strategy:
            percents = self.burndown_strategy(self)
        else:
            percents = 0

        return self.done + percents

    def __repr__(self):
        msg = "Percentage: {}, after burndown: {}"
        return msg.format(self.done, self.percents_after_burndown())


def linear_burndown(issue):
    days_left = issue.estimated - issue.current_day
    current_pct = days_left/issue.estimated * 100
    return current_pct - issue.done

def every_day_10_percent_burndown(issue):
    if issue.current_day <= issue.estimated:
        current_pct = (10 - issue.current_day) * 10
        return current_pct - issue.done
    return 0


if __name__ == "__main__":
    issue1 =Issue(123, 10)
    print(issue1)
    issue1.next_day()
    print(issue1)

    """linearno"""
    issue2 = Issue(234, 5, burndown_strategy=linear_burndown)
    print(issue2)
    issue2.next_day()
    print(issue2)
    issue2.next_day()
    issue2.next_day()
    issue2.next_day()
    print(issue2)

    """with discount strategy as On Sale Discount"""
    issue3 = Issue(345, 9, burndown_strategy=every_day_10_percent_burndown)
    print(issue3)
    issue3.next_day()
    print(issue3)
