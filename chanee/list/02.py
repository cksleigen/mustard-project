# 리스트 요소 삭제하는 메소드 암기하기... (어떤 게 값을 레퍼런스하고 어떤 게 인덱스를 레퍼런스하는지...)
# 중복값 제거해주는 set(arr) 메소드 암기

def solution(arr:list)->list:
    sortedArr = sorted(arr, reverse=True)
    for i, value in enumerate(sortedArr):
        maxIndex = len(sortedArr) - 1
        if i+1 <= maxIndex:
            if sortedArr[i] == sortedArr[i+1]:
                sortedArr.pop(i)
            elif i != i+1:
                pass
        elif i+1 > maxIndex:
            pass
    return sortedArr

firstTestCase = [4,2,2,1,3,4]
secondTestCase = [2,1,1,3,2,5,4]

print(solution(firstTestCase))
print(solution(secondTestCase))