Python 3.13.1 (tags/v3.13.1:0671451, Dec  3 2024, 19:06:28) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
print
<built-in function print>


print("Hello\tWorld!")
Hello	World!
print("Hello\nWorld!")
Hello
World!
s="Hello"
upper(s)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    upper(s)
NameError: name 'upper' is not defined. Did you mean: 'super'?
s.upper()
'HELLO'
"Hello".lower()
'hello'
msg="Hello"
print(msg)
Hello
Hello="World!"
msg=Hello
print(msg)
World!
message = "철수가 "안녕"이라고 말했습니다.")
SyntaxError: unmatched ')'
message = "철수가 '안녕'이라고 말했습니다."
print(message)
철수가 '안녕'이라고 말했습니다.
print('철수가\t'안녕'이라고\t말했습니다.")
      
SyntaxError: unterminated string literal (detected at line 1)
print("철수가\t'안녕'이라고\t말했습니다.")
      
철수가	'안녕'이라고	말했습니다.
print("철수가\n'안녕'이라고\t말했습니다.")
      
철수가
'안녕'이라고	말했습니다.
100 + '원'
      
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    100 + '원'
TypeError: unsupported operand type(s) for +: 'int' and 'str'
str(100)+'원'
      
'100원'
100+int('원')
      
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    100+int('원')
ValueError: invalid literal for int() with base 10: '원'
int("100")+'원'
      
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    int("100")+'원'
TypeError: unsupported operand type(s) for +: 'int' and 'str'
int('100')
      
100
str(100)
      
'100'
str(3.14)
      
'3.14'
float('3.14')
      
3.14
str x(input("이름을 입력하시오:")
      
SyntaxError: '(' was never closed
str x(input("이름을 입력하시오:"))
      
SyntaxError: invalid syntax
x = (input("이름을 입력하시오: "))
      
이름을 입력하시오: 홍길동
x = (input("이름을 입력하시오: "))
      
이름을 입력하시오: ㅇㄴㄹㅇㄹ
x = (input("이름을 입력하시오: "))
      
이름을 입력하시오: ㅇㄻ
x = (input("이름을 입력하시오: ")); print(x + "씨, 안녕하세요? 파이썬 프로그래밍의 세계에 오신것을 환영합니다.)
                                  
SyntaxError: unterminated string literal (detected at line 1)
x = (input("이름을 입력하시오: ")); print(x + "씨, 안녕하세요? 파이썬 프로그래밍의 세계에 오신것을 환영합니다.")
                                  
이름을 입력하시오: 홍길동
홍길동씨, 안녕하세요? 파이썬 프로그래밍의 세계에 오신것을 환영합니다.
x = (input("첫번째 정수를 입력하시오: ")); y = (input("두번째 정수를 입력하시오: ")) ; print(x + " 과 " + y + " 의 합은 " + x+y + " 입니다.")
                                  
첫번째 정수를 입력하시오: 300
두번째 정수를 입력하시오: 400
300 과 400 의 합은 300400 입니다.
int x = (input("첫번째 정수를 입력하시오: ")); int y = (input("두번째 정수를 입력하시오: ")) ; print(x + " 과 " + y + " 의 합은 " + x+y + " 입니다.")
                                  
SyntaxError: invalid syntax
x = int(input("첫번째 정수를 입력하시오: ")); y = int(input("두번째 정수를 입력하시오: ")) ; print(x + " 과 " + y + " 의 합은 " + x+y + " 입니다.")
                                  
첫번째 정수를 입력하시오: 300
두번째 정수를 입력하시오: 400
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    x = int(input("첫번째 정수를 입력하시오: ")); y = int(input("두번째 정수를 입력하시오: ")) ; print(x + " 과 " + y + " 의 합은 " + x+y + " 입니다.")
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> x = int(input("첫번째 정수를 입력하시오: ")); y = int(input("두번째 정수를 입력하시오: ")); x+y=z; print(x + " 과 " + y + " 의 합은 " + z + " 입니다.")
...                                   
SyntaxError: cannot assign to expression here. Maybe you meant '==' instead of '='?
>>> x = int(input("첫번째 정수를 입력하시오: ")); y = int(input("두번째 정수를 입력하시오: ")); x+y==z; print(x + " 과 " + y + " 의 합은 " + z + " 입니다.")
...                                   
첫번째 정수를 입력하시오: 300
두번째 정수를 입력하시오: 400
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    x = int(input("첫번째 정수를 입력하시오: ")); y = int(input("두번째 정수를 입력하시오: ")); x+y==z; print(x + " 과 " + y + " 의 합은 " + z + " 입니다.")
NameError: name 'z' is not defined
>>> msg = "정수를 입력하세요"; x=int(input("첫번째 정수를 입력하세요 : ")); y=int(input("두번째 정수를 입력하세요 : ")); print(x, "과", y, "의 합은", x+y," 입니다.")
...                                   
첫번째 정수를 입력하세요 : 300
두번째 정수를 입력하세요 : 400
300 과 400 의 합은 700  입니다.
>>> x=(input("경기장은 어디입니까?"));y=(input("이긴 팀은 어디입니까?"));a=(input("진 팀은 어디입니까?"));b=(input("우수선수는 누구입니까?"));c=(input("스코어는 몇대몇입니까?"));print("오늘",x,"에서 야구 경기가 열렸습니다.",y,"과",a,"은 치열한 공방전을 펼쳤습니다.",b,"의 맹활약으로",y,"가",a,"를",c, "로 이겼습니다.")
...                                   
경기장은 어디입니까?강릉
이긴 팀은 어디입니까?드림즈
진 팀은 어디입니까?비룡스
우수선수는 누구입니까?강두기
스코어는 몇대몇입니까?9:7
오늘 강릉 에서 야구 경기가 열렸습니다. 드림즈 과 비룡스 은 치열한 공방전을 펼쳤습니다. 강두기 의 맹활약으로 드림즈 가 비룡스 를 9:7 로 이겼습니다.
