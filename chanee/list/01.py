# sort(), sorted() 차이점 이해하기
# sort() 메소드는 리스트 원본 값을 변경함

def solution(intList:list)->list:
    sortedList = sorted(intList)
    return sortedList

firstTestCase = [1,-5,2,4,3]
print(solution(firstTestCase))

print(firstTestCase.sort()) # None
print(sort(firstTestCase)) # sort()라는 함수 없음

firstTestCase.sort()
print(firstTestCase)
print(sorted(firstTestCase))