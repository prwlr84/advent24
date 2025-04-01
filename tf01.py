from tf01i import inputString
# 1
lines = [list(map(int, line.split())) for line in inputString.splitlines()]
first, second = zip(*lines)

dist = sum(abs(x - y) for x, y in zip(sorted(first), sorted(second)))
print("first:", str(dist))
# 2
col1, col2 = zip(*[line.split() for line in inputString.splitlines()])
summ = sum(col2.count(e) * int(e) for e in col1)
print("second:", summ)

#
# lines = inputString.split('\n')
# first = []
# second = []
#
# for line in lines:
#     tmp = line.split()
#     first.append(int(tmp[0]))
#     second.append(int(tmp[1]))
#
# first.sort()
# second.sort()
#
# dist = 0
#
# for i, f in enumerate(first):
#     dist += abs(f-second[i])
#
# print(dist)

# col1, col2 = [[], []]
# for line in inputString.splitlines():
#     arr = line.split()
#     col1.append(arr[0])
#     col2.append(arr[1])
#
# summ = 0
# for e in col1:
#     summ += col2.count(e) * int(e)
#
# print("second: " + str(summ))