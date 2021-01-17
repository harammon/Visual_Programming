"""
 * 파일명 : problem4.py
 * 작성일 : 2020년 10월 21일
 * 작성자 : 문헌정보학과 20142611 이하람
 """
directory = {"홍길동":"010-4444-5555", "김중앙":"010-9191-8181", "심청":"010-3232-5454"}
name = directory.keys()
number = directory.values()
while True:
    found = False
    userInput = input("이름>> ")
    for index in name:
        if userInput in index:
            print(index, directory[index])
            found = True
    if userInput == "add":
            inputName = input("이름은? ")
            inputNumber = input("전화번호는? ")
            directory[inputName] = inputNumber
            print(inputName, "전화번호가 추가되었습니다.")
    elif found == False:
        print("찾을 수 없습니다.")