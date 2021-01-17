import readmodule
import os
def makereport(x):
    global file_name
    while True:
        user_input = input("출력 파일의 이름을 입력하세요. ")
        print("")
        file_name = user_input + '_report.txt'
        is_exist = os.path.exists(file_name)
        if is_exist:
            user_choice = input("이미 같은 이름의 파일이 존재합니다. 덮어 쓰시겠습니까? (1.예, 2.아니오) ")
            print("")
            if user_choice == '1':
                f2 = open(file_name, 'w')
                break
            elif user_choice == '2':
                print("")
            else:
                print("잘못입력하셨습니다.")
                print("")
        else:
            f2 = open(file_name, 'w')            
            break
    f2.write("==============성적표================")
    f2.write("\n")
    f2.write("%5s %5s %5s %5s %6s %6s" %('이름', '국어', '영어', '수학', '총합', '석차'))
    f2.write("\n")
    f2.write("==================================")
    f2.write("\n")
    t = 0
    for i in x:
        readmodule.score_list[t].append(i)
        t += 1
    l3 = sorted(readmodule.score_list, key = lambda x : -x[4])
    for i in l3: 
        a = i[0]
        f2.write(a)
        f2.write(" ")
        for j in i[1:4]:
            try:
                b = int(j)
                if b < 0 or b > 100:
                    raise Exception
                else:
                    f2.write("%7s" %j)
                    f2.write(" ")          
            except:
                f2.write('%7s' %'_')
                f2.write("  ")
        f2.write("%8s" %str(i[4]))
        f2.write("%7s" %str(l3.index(i)+1)+'등')
        f2.write("\n")
    print("%s파일에 출력이 완료되었습니다." %file_name)


