from collections import Counter


def frequency(toeicScores) :
    counters = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for toeicScore in toeicScores:
        counters[toeicScore//100] += 1
    return counters

def max_frequency(counters) :
    max = 0
    scoreBase = 0
    N = len(counters)
    for i in range(N) :
        if max < counters[i] :
            max = counters[i]
            scoreBase = i * 100
    return max

def min_frequrncy(counters) :
    scoreBase = 0
    N = len(counters)
    min = 11
    for i in range(N) :
        if counters[i] != 0 and min > counters[i] :
            scoreBase = i * 100
            min = counters[i]
    return min

toeicScores = [510, 630, 750, 780, 620, 805, 950, 650, 840, 670]

copunters = frequency(toeicScores)
maxCount = max_frequency(Counter)

for i in range(len(counters)) :
    if counters[i] == maxCount :
        scoreBase = i * 100
        print("가장 많은 점수대 = %d, 빈도수 = %d" %(scoreBase, maxCount))

minCount = min_frequrncy(copunters)

for i in range(len(copunters)) :
    if copunters[i] == minCount :
        scoreBase = i * 100
        print("가장 작은 점수대 = %d, 빈도수 = %d" %(scoreBase, minCount))