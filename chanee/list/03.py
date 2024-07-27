def solution(lst:list)->list:
    for i, value in enumerate(lst):
        maxIndex = len(lst) - 1
        print(maxIndex)
        if i+1 <= maxIndex:
            pass
            # for j in range(0, maxIndex, 1):
            #     print(j)
            #     lst.append(lst[i] + lst[j])
                
    return set(lst)

firstTestCase = [2,1,3,4,1]
secondTestCase = [5,0,2,7]

print(solution(firstTestCase))