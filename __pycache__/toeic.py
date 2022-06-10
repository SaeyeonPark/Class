toeicScores = [510, 630, 750, 780, 620, 805, 930, 650, 840, 670]

counters = frequency(toeicScores)
scoreBase, maxCount = max_frequency(counters)

print("가장 많은 점수대 = %d, 빈도수 = %d" %(scoreBase, maxCount))

scoreBase, minCount = min_quency(counters)

print("가장 적은 점수대 = %d, 빈도수 = %d" %(scoreBase, minCount))