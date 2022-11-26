class MinStat:
    def __init__(self):
        self.stack = []

    def add_number(self, n):
        self.stack.append(n)

    def result(self):
        try:
            return min(self.stack)
        except:
            return None


class MaxStat(MinStat):
    def result(self):
        try:
            return max(self.stack)
        except:
            return None


class AverageStat(MinStat):
    def result(self):
        try:
            return sum(self.stack) / len(self.stack)
        except:
            return None
