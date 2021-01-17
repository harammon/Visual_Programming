"""
 * 파일명 : problem2.py
 * 작성일 : 2020년 10월 22일
 * 작성자 : 문헌정보학과 20142611 이하람
 """
 
while True:
    userInput = input("문장을 입력하세요 : ")
    case1_index = userInput.find("이라고 합니다.")
    case2_index = userInput.find("입니다.")
    if userInput[:2] == "저는":
        if case1_index  >= 4:
            print(userInput[3:case1_index])
        elif case2_index >= 4:
            print(userInput[3:case2_index])
    elif userInput[:5] == "제 이름은":
        if case2_index >= 7:
            print(userInput[6:case2_index])
    