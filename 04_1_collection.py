#리스트의 기본
a=[10,10,10,10]
a[0]=int(input('num1:'))
a[1]=int(input('num2:'))
a[2]=int(input('num3:'))
a[3]=int(input('num4:'))
hap=a[0]+a[1]+a[2]+a[3]
print('hap',hap)


#리스트 항목추가 함수
a=[10,20]
a.append(30)
a.append([40,50])
a.insert(1,15)

#정렬
a.sort()
a.sort(reverse=True)

#갯수파악
a.count(20)

#삭제
a.pop()
a.pop(1)
a.remove(30)

#딕셔너리
menu={'김밥':2000,'라면':3000}
menu['김밥']
menu['라면']=3500

#딕셔너리 키, 값, 항목 추출
menu.keys()
menu.values()
menu.items()

#에러처리가 가능한 get함수
name={100:'황복동',200:'황채연',300:'황나연'}
name.get(100)
#name[400] error
name.get(400,'not Found')

#딕셔너리 항목 삭
del(name[100])
name.pop(200)


