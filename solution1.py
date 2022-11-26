class MinStat:
    def __init__(self):
        self.stack = []

    def add_number(self, n):
        self.stack.append(n)

    def result(self):
        return min(self.stack)


class MaxStat(MinStat):
    def result(self):
        return max(self.stack)


class AverageStat(MinStat):
    def result(self):
        return sum(self.stack) / len(self.stack)
