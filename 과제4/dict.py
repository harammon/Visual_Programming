"""
 * 파일명 : Dict.py
 * 작성일 : 2020년 11월 12일
 * 작성자 : 문헌정보학과 20142611 이하람
 """
f = open('dict_test.TXT', 'r')
dictKey = []
dictValue = []
while True:
    line = f.readline()
    if line == '':
        break
    line = line[:-1]
    s = line.split(':')
    s[0] = s[0].rstrip()
    s[1] = s[1].lstrip()
    dictKey.append(s[0])
    dictValue.append(s[1])
myDict = dict(zip(dictKey, dictValue))
while True:
    userInput = input("단어?  ")
    if userInput == '종료':
        break
    if myDict.get(userInput) == " ":
        print(userInput, end = " ")
        print(" ")
    else:
        print(userInput, end = " ")
        if myDict.get(userInput) == None:
            print("사전에 없는 단어입니다.")
        else:
            print(myDict.get(userInput))
f.close()
