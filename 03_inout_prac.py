#본인의 이름과 취미를 입력받아 콤마(,)를 이용하여 출력하기
#실습1
name = input('이름 :')
hobby = input('취미 :')
print('이름은',name,'이고 취미는',hobby,'입니다')

#실습2
radius = int(input('반지름 입력:'))
area = 3.14 * radius*radius
print('원의 넓이는 %.2f입니다.'%area)

#실습3
width = int(input('가로 길이 입력:'))
height = int(input('세로 길이 입력:'))
area = width *height
print('가로: {}, 세로{}, 넓이{}'.format(width, height, area))



#도전문제 1: 시간의 초를 입력 받아 분과 초를 출력하는 실행 결과가 나오도록
#           빈칸을 완성하시오

total = int(input('시간의 전체 초 입력:'))
min = total//60
sec = total % 60
print('{} 초: {}분 {}초'.format(total, min, sec))


#도전문제 2:이번 학기 수강하는 파이썬 과목은 성적 반용비율이 아래외 같다
#           (출석: 20%, 과제 :20%, 중간:30%, 기말:30%)
#           항목 점수를 각가 입력 받아 전체 총점을 출력하는 프로그램이다.
#           단, 출석점수와 과제점수는 소수점이 발생하지 않는다. 중간, 기말점수는
#           소수점이 발생할 수 있다. 전체 총점은 소수점 둘째 자리까지 표시한다.
#           빈칸을 완성하시오

name=input('이름:')
attent=int(input('출석점수'))
homework=int(input('과제점수'))
mid=float(input('중간점수'))
final=float(input('기말점수'))
total=attent*0.2+ homework*0.2+mid*0.3+final*0.3
print('name:%s'%name)
print('total:%.2f'%total)


#도전문제 3:커피 메뉴가 ame, latte, moca,있을때 하루에 판매 된 수량을 각각 입력 받아 총
#           매출액을 계산하는 프로그램을 작성하시오
#           또한 하루 재료비가 100,000원 일 경우 순이익을 구하시오.
#           가격:ame=2000,latte=3000,moca=4000

ame=int(input('ame 몇잔?'))
latte=int(input('latte 몇잔?'))
moca=int(input('moca 몇잔?'))

gross=ame*2000 + latte*3000 + moca*4000
net = gross - 100000
print('순이익 :{}'.format(net))
