"""
 * 파일명 : WordChain.py
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

word = 'apple'
myDict = dict(zip(dictKey, dictValue))
wordList = []

while True:
    print("%s 끝말 잇기? " %word, end = "")
    userInput = input()
    if myDict.get(userInput) == None or myDict.get(userInput)[0] != 'n': #사전에 없거나 명사가 아닌 경우
        print("사전에 없는 단어입니다(%s의 끝말을 이으세요)." %word)
        print("")
    elif len(userInput) == 5:  #사전에 있고, 명사이며, 길이가 5인경우
        if word[-1] == userInput[0]:    #끝말을 잇는다면 
            if userInput not in wordList:   #이전에 등장한 단어가 아니라면
                print("정답입니다(%s의 끝말을 이으세요)." %userInput)
                print("")
                word = userInput    #끝말을 이어야하는 단어에 현재 사용자의 입력을 넣기
                wordList.append(word)
            else:
                print("중복된 단어입니다(%s의 끝말을 이으세요)." %word)
                print("")
        else:   #사전에 있고, 명사이며 길이가 5이나, 끝말을 잇지 못하는 경우
            print("틀렸습니다(%s의 끝말을 이으세요)." %word)
            print("")
    else:   #사전에 있고, 명사이지만 길이가 5가 아닌 경우
        if len(userInput)>5:
            print("단어가 길어요(%s의 끝말을 이으세요)." %word)
            print("")
        else:
            print("단어가 짧아요(%s의 끝말을 이으세요)." %word)
            print("")
f.close()