def readdata():
    global score_list
    while True:
        file_name = input("파일 이름을 입력하세요. ")
        print("")
        f1 = 0
        try:
            f1 = open(file_name, 'r')
        except IOError:
            print("파일을 찾지 못했습니다.")
            print("")
        if f1 != 0:
            break
    score_list = list()
    f1.readline()
    while True:
        v = f1.readline()
        if v == '' : break;
        v=v[:-1]             
        s = v.split(',')
        score_list.append(s)
#score_list = [['이하람', '90', '80', '70'], ['김지수', '90', '100', '20']]
    for i in score_list:
        b = ['국어', '영어', '수학']
        k = -1
        for j in i[1:]:
            k = k+1
            try:
                if j.isnumeric() == False:
                    raise Exception
                else:
                    if int(j)>100 or int(j)<0:
                        raise Exception
            except:
                print(i[0]+' 학생의 ' + b[k] +' 점수에 문제가 있습니다.')
                print("")
