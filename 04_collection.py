#리스트의 기본형
a = [10,20,30,40]


#리스트의 인덱싱
print(a)
print(a[0]) #정방향 ->
print(a[-1]) #역방향 <-
#print(a[-4]) error

#리스트의 슬라이싱
print(a[1:3]) #시작 요소부터 (끝-1) 까지 반환

#리스트의 조작함수
#a.append() #리스트에 요소를 마지막위치에 새로 추가/ 값
#a.insert()#리스트의 해당 위치에 요소를 새로삽입/ 위치, 값
#a.sort()#오름차순정렬 , 내림차순 정렬/ void or reverse=True
#a.count()#해당요소의 개수를 반환/ 찾을 값
#a.poo()#리스트 제일 뒤의 항목을 빼내고 빼낸항목은 삭제 또는 제거할 위치에 있는 요소제거/ void or 위치
#a.remove()#해당요소를 찾아 삭제/ 삭제할 값


#튜플의 기본형
# 한번 저장된 값은 수정할 수 없는 자료형
# 읽기 전용의 데이터를 저장할 때 유용하게 사용

b = (10, 20, 30, 40)

#리스트와 조작이 비슷



#딕셔너리의 기본형
#순서가 없는 컬렉션 자료형 Key:value의 형

c = {'key1':'value1', 'key2':'value2', 'key3':'value3'}

print(c['key1'])
c['key1']='new_value1'
print(c['key1'])
print(c)
#print(c['key4']) error

#c.get() #항목접근하기/key
#c.pop() #항목꺼내고 삭제하기/key
#c.del() #항목삭제하기/[key]
#c.items()#딕셔너리에 저장된 항목
#c.keys() #딕셔너리에 저장된키
#c.values()#딕셔너리에 저장된


#세트의 기본형
#집합에 관련된 것들을 쉽게 처리하기 위해 만든 자료형 중복 허용 x
#순서가 없음

d = {10,20,30}
e = {20,40}

print(d & e)
print(d | e)
print(d - e)
