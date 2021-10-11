member = input('회원이십니까? (y/n)')
if member =='y':
    print('어서오세요')
elif member == 'n':
    print('회원가입이 필요합니다')
else:
    print('정확한 답변을 기입해주세요')

score = int(input('점수'))
if score >= 60:
    print('합격')
else:
    print('불합격')
print('end')


num = int(input('정수입력:'))

if num > 0:
    print('%d 양수' % num)
elif num < 0:
    print('음수')
else:
    print('0')

sid=input('id:')
spw=input('pw:')

if sid=='admin' and spw=='1234':
    print('로그인성공')
else :
    print('로그인 실패')
