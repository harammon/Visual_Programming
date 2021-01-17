"""
 * 파일명 : 3.py
 * 작성일 : 2020년 10월 3일
 * 작성자 : 문헌정보학과 20142611 이하람
 * 출력예시 : 안녕하세요. 다음의 메뉴 중 원하는 메뉴를 선택하세요.
              (noodle, ham, egg, spaghetti)  ham
              200원 입니다.
              안녕하세요. 다음의 메뉴 중 원하는 메뉴를 선택하세요.
              (noodle, ham, egg, spaghetti)  noodle
              500원 입니다.
              안녕하세요. 다음의 메뉴 중 원하는 메뉴를 선택하세요.
              (noodle, ham, egg, spaghetti)  egg
              100원 입니다.
              안녕하세요. 다음의 메뉴 중 원하는 메뉴를 선택하세요.
              (noodle, ham, egg, spaghetti)  spaghetti
              900원 입니다.
              안녕하세요. 다음의 메뉴 중 원하는 메뉴를 선택하세요.
              (noodle, ham, egg, spaghetti)  bread
              그런 메뉴는 없습니다.
 """

menuBoard = ['noodle', 'ham', 'egg', 'spaghetti']
price = ['500원', '200원', '100원', '900원']
while True: 
    print("안녕하세요. 다음의 메뉴 중 원하는 메뉴를 선택하세요.")
    order = input("(noodle, ham, egg, spaghetti)  ")
    if order in menuBoard:
        print(price[menuBoard.index(order)], "입니다.")
    else:
        print("그런 메뉴는 없습니다.")