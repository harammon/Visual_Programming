"""
 * 파일명 : 2.py
 * 작성일 : 2020년 10월 3일
 * 작성자 : 문헌정보학과 20142611 이하람
 * 출력예시 : 동을 입력하세요 (x를 입력하면 종료합니다.) 사당동
              2 번째 동입니다.
              동을 입력하세요 (x를 입력하면 종료합니다.) 가츠동
              새로운 동명입니다. 6 번째 동으로 등록합니다.
              동을 입력하세요 (x를 입력하면 종료합니다.) 가츠동
              6 번째 동입니다.
 """

dong = ['흑석동', '사당동', '상도동', '노량진동', '규동']
while True:
    dongInput=input("동을 입력하세요 (x를 입력하면 종료합니다.) ")
    if dongInput=="x":
        break
    elif dongInput in dong:
        print(dong.index(dongInput)+1,"번째 동입니다.")
    else:
        dong.append(dongInput)
        print("새로운 동명입니다.", len(dong),"번째 동으로 등록합니다.")
        