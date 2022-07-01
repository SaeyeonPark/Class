from tracemalloc import start


def solution(lines) :
    history = []
    for line in lines :
        end_time, t = line.split()[1:]
        end_time = end_time.split(':')
        end_time = (int(end_time[0]) * 3600 + int(end_time[1]) * 60 + float(end_time[2])) * 1000
        t = float(t[:-1]) * 1000
        start_time = end_time - t + 1
        history.append([start_time, end_time])
    answer = 1
    for hist1 in history:
        counting_0 = 0
        counting_1 = 0
        for hist2 in history:
            start1, start2 = hist1
            end1, end2 = start1 + 1000, start2 + 1000
            if hist1[1] >= start1 and end1 > hist2[0] :
                counting_0 += 1
            if hist2[1] >= start2 and end2 > hist2[0] :
                counting_1 += 1
        answer = max(answer, counting_0, counting_1)
    return answer