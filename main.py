from solution1 import MinStat, MaxStat, AverageStat
values = [1, 2, 4, 5]
mins = MinStat()
maxs = MaxStat()
average = AverageStat()
for v in values:
    mins.add_number(v)
    maxs.add_number(v)
    average.add_number(v)
print(mins.result(), maxs.result(), average.result())
