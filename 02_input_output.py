#input은 사용자로 부터 값을 입력받는다.

name = input("이름 입력:")
print(name)


#정수를 입력해도 문자로 입력받기에 문자열 처럼 취급된다.
a = input('첫 번째 숫자:')
b = input('두 분째 숫자:')
print(a + b)


#자료형을 정수로 형변환
a = int(input('첫 번째 숫자:'))
b = int(input('두 분째 숫자:'))
print(a + b)


#출력하는 여러 방법

##,로 구분
name = input('이름 입력:')
print('입력하신 이름은',name)

##% 형식 지정자를 이용한 출력
name = input('이름 입력:')
print('입력하신 이름은 %s 입니다.'%name)

a = int(input('첫 번째 숫자:'))
b = int(input('두 분째 숫자:'))
print('%a + %d = %d'%(a,b,a+b))

a = int(input('첫 번째 숫자:'))
b = int(input('두 분째 숫자:'))
print('%a + %d = %f'%(a,b,a/b))

## format() 함수를 이용한 출력
a = int(input('첫 번째 숫자:'))
b = int(input('두 분째 숫자:'))
print('{0} * {1} = {2}'.format(a,b,a*b))

