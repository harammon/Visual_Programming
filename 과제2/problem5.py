"""
 * 파일명 : problem5.py
 * 작성일 : 2020년 10월 21일
 * 작성자 : 문헌정보학과 20142611 이하람
 """
while True:
    cnt = 0
    a = ["천", "백", "십"]
    c = ["영", "", "이", "삼", "사", "오", "육", "칠", "팔", "구"]
    c_1 = ["영", "일", "이", "삼", "사", "오", "육", "칠", "팔", "구"]
    userInput = input("숫자는?  ")
    numPrint = format(int(userInput), ",")
    print(numPrint)
    num = int(userInput)
    numLen = len(userInput)
    if numLen<5:
        cnt = 1
    elif 5<=numLen<9:
        cnt = 2
    elif 9<=numLen<13:
        cnt = 3
    while cnt:
        if cnt == 3:
            num1 = num // 100000000
            x_1000 = num1 // 1000
            x_100 = (num1%1000) // 100
            x_10 = (num1%100) // 10
            x_1 = (num1%10)
        
            print_1000 = str(c[x_1000]+a[0])
            print_100 = str(c[x_100]+a[1])
            print_10 = str(c[x_10]+a[2])
            print_1 = str(c[x_1])
            print_1_1 = str(c_1[x_1])
            cnt -= 1
            #0000
            if x_1000 == 0 and x_100 == 0 and x_10 == 0 and x_1 == 0:
                print("", end = '')
            #0001
            if x_1000 == 0 and x_100 == 0 and x_10 == 0 and x_1 != 0:
                if x_1 == 1:
                    print("%s억" %print_1_1, end = '')
                else:
                    print("%s억" %print_1, end = '')
            #0010
            if x_1000 == 0 and x_100 == 0 and x_10 != 0 and x_1 == 0:
                print("%s억" %print_10, end = '')
            #0011
            if x_1000 == 0 and x_100 == 0 and x_10 != 0 and x_1 != 0:
                if x_1 == 1:
                    print("%s%s억" %(print_10, print_1_1), end = '')
                else:
                    print("%s%s억" %(print_10, print_1), end = '')
            #0100
            if x_1000 == 0 and x_100 != 0 and x_10 == 0 and x_1 == 0:
                print("%s억" %print_100, end = '')
            #0101
            if x_1000 == 0 and x_100 != 0 and x_10 == 0 and x_1 != 0:
                if x_1 == 1:
                    print("%s%s억" %(print_100, print_1_1), end = '')
                else:
                    print("%s%s억" %(print_100, print_1), end = '')
            #0110
            if x_1000 == 0 and x_100 != 0 and x_10 != 0 and x_1 == 0:
                print("%s%s억" %(print_100, print_10), end = '')
            #0111
            if x_1000 == 0 and x_100 != 0 and x_10 != 0 and x_1 != 0:
                if x_1 == 1:
                    print("%s%s%s억" %(print_100, print_10, print_1_1), end = '')
                else:
                    print("%s%s%s억" %(print_100, print_10, print_1), end = '')
            #1000
            if x_1000 != 0 and x_100 == 0 and x_10 == 0 and x_1 == 0:
                print("%s억" %print_1000, end = '')
            #1001
            if x_1000 != 0 and x_100 == 0 and x_10 == 0 and x_1 != 0:
                if x_1 == 1:
                    print("%s%s억" %(print_1000, print_1_1), end = '')
                else:
                    print("%s%s억" %(print_1000, print_1), end = '')
            #1010
            if x_1000 != 0 and x_100 == 0 and x_10 != 0 and x_1 == 0:
                print("%s%s억" %(print_1000, print_10), end = '')
            #1011
            if x_1000 != 0 and x_100 == 0 and x_10 != 0 and x_1 != 0:
                if x_1 == 1:
                    print("%s%s%s억" %(print_1000, print_10, print_1_1), end = '')
                else:
                    print("%s%s%s억" %(print_1000, print_10, print_1), end = '')
            #1100
            if x_1000 != 0 and x_100 != 0 and x_10 == 0 and x_1 == 0:
                print("%s%s억" %(print_1000, print_100), end = '')
            #1101
            if x_1000 != 0 and x_100 != 0 and x_10 == 0 and x_1 != 0:
                if x_1 == 1:
                    print("%s%s%s억" %(print_1000, print_100, print_1_1), end = '')
                else:
                    print("%s%s%s억" %(print_1000, print_100, print_1), end = '')
            #1110
            if x_1000 != 0 and x_100 != 0 and x_10 != 0 and x_1 == 0:
                print("%s%s%s억" %(print_1000,print_100, print_10), end = '')
            #1111
            if x_1000 != 0 and x_100 != 0 and x_10 != 0 and x_1 != 0:
                if x_1 == 1:
                    print("%s%s%s%s억" %(print_1000, print_100, print_10, print_1_1), end = '')
                else:
                    print("%s%s%s%s억" %(print_1000, print_100, print_10, print_1), end = '')
    
        if cnt == 2:
            num2 = int(userInput[-8:-4])
            x_1000 = num2 // 1000
            x_100 = (num2%1000) // 100
            x_10 = (num2%100) // 10
            x_1 = (num2%10)
            print_1000 = str(c[x_1000]+a[0])
            print_100 = str(c[x_100]+a[1])
            print_10 = str(c[x_10]+a[2])
            print_1 = str(c[x_1])
            print_1_1 = str(c_1[x_1])
            cnt -= 1
            #0000
            if x_1000 == 0 and x_100 == 0 and x_10 == 0 and x_1 == 0:
                print("", end = '')
            #0001
            if x_1000 == 0 and x_100 == 0 and x_10 == 0 and x_1 != 0:
                if x_1 == 1:
                    print("%s만" %print_1_1, end = '')
                else:
                    print("%s만" %print_1, end = '')
            #0010
            if x_1000 == 0 and x_100 == 0 and x_10 != 0 and x_1 == 0:
                print("%s만" %print_10, end = '')
            #0011
            if x_1000 == 0 and x_100 == 0 and x_10 != 0 and x_1 != 0:
                if x_1 == 1:
                    print("%s%s만" %(print_10, print_1_1), end = '')
                else:
                    print("%s%s만" %(print_10, print_1), end = '')
            #0100
            if x_1000 == 0 and x_100 != 0 and x_10 == 0 and x_1 == 0:
                print("%s만" %print_100, end = '')
            #0101
            if x_1000 == 0 and x_100 != 0 and x_10 == 0 and x_1 != 0:
                if x_1 == 1:
                    print("%s%s만" %(print_100, print_1_1), end = '')
                else:
                    print("%s%s만" %(print_100, print_1), end = '')
            #0110
            if x_1000 == 0 and x_100 != 0 and x_10 != 0 and x_1 == 0:
                print("%s%s만" %(print_100, print_10), end = '')
            #0111
            if x_1000 == 0 and x_100 != 0 and x_10 != 0 and x_1 != 0:
                if x_1 == 1:
                    print("%s%s%s만" %(print_100, print_10, print_1_1), end = '')
                else:
                    print("%s%s%s만" %(print_100, print_10, print_1), end = '')
            #1000
            if x_1000 != 0 and x_100 == 0 and x_10 == 0 and x_1 == 0:
                print("%s만" %print_1000, end = '')
            #1001
            if x_1000 != 0 and x_100 == 0 and x_10 == 0 and x_1 != 0:
                if x_1 == 1:
                    print("%s%s만" %(print_1000, print_1_1), end = '')
                else:
                    print("%s%s만" %(print_1000, print_1), end = '')
            #1010
            if x_1000 != 0 and x_100 == 0 and x_10 != 0 and x_1 == 0:
                print("%s%s만" %(print_1000, print_10), end = '')
            #1011
            if x_1000 != 0 and x_100 == 0 and x_10 != 0 and x_1 != 0:
                if x_1 == 1:
                    print("%s%s%s만" %(print_1000, print_10, print_1_1), end = '')
                else:
                    print("%s%s%s만" %(print_1000, print_10, print_1), end = '')
            #1100
            if x_1000 != 0 and x_100 != 0 and x_10 == 0 and x_1 == 0:
                print("%s%s만" %(print_1000, print_100), end = '')
            #1101
            if x_1000 != 0 and x_100 != 0 and x_10 == 0 and x_1 != 0:
                if x_1 == 1:
                    print("%s%s%s만" %(print_1000, print_100, print_1_1), end = '')
                else:
                    print("%s%s%s만" %(print_1000, print_100, print_1), end = '')
            #1110
            if x_1000 != 0 and x_100 != 0 and x_10 != 0 and x_1 == 0:
                print("%s%s%s만" %(print_1000,print_100, print_10), end = '')
            #1111
            if x_1000 != 0 and x_100 != 0 and x_10 != 0 and x_1 != 0:
                if x_1 == 1:
                    print("%s%s%s%s만" %(print_1000, print_100, print_10, print_1_1), end = '')
                else:
                    print("%s%s%s%s만" %(print_1000, print_100, print_10, print_1), end = '')
        if cnt == 1:
            num3 = int(userInput[-4:])
            x_1000 = num3 // 1000
            x_100 = (num3%1000) // 100
            x_10 = (num3%100) // 10
            x_1 = (num3%10)
        
            print_1000 = str(c[x_1000]+a[0])
            print_100 = str(c[x_100]+a[1])
            print_10 = str(c[x_10]+a[2])
            print_1 = str(c[x_1])
            print_1_1 = str(c_1[x_1])
            cnt -= 1
            #0000
            if x_1000 == 0 and x_100 == 0 and x_10 == 0 and x_1 == 0:
                print("")
            #0001
            if x_1000 == 0 and x_100 == 0 and x_10 == 0 and x_1 != 0:
                if x_1 == 1:
                    print("%s" %print_1_1)
                else:
                    print("%s" %print_1)
            #0010
            if x_1000 == 0 and x_100 == 0 and x_10 != 0 and x_1 == 0:
                print("%s" %print_10)
            #0011
            if x_1000 == 0 and x_100 == 0 and x_10 != 0 and x_1 != 0:
                if x_1 == 1:
                    print("%s%s" %(print_10, print_1_1))
                else:
                    print("%s%s" %(print_10, print_1))
            #0100
            if x_1000 == 0 and x_100 != 0 and x_10 == 0 and x_1 == 0:
                print("%s" %print_100)
            #0101
            if x_1000 == 0 and x_100 != 0 and x_10 == 0 and x_1 != 0:
                if x_1 == 1:
                    print("%s%s" %(print_100, print_1_1))
                else:
                    print("%s%s" %(print_100, print_1))
            #0110
            if x_1000 == 0 and x_100 != 0 and x_10 != 0 and x_1 == 0:
                print("%s%s" %(print_100, print_10))
            #0111
            if x_1000 == 0 and x_100 != 0 and x_10 != 0 and x_1 != 0:
                if x_1 == 1:
                    print("%s%s%s" %(print_100, print_10, print_1_1))
                else:
                    print("%s%s%s" %(print_100, print_10, print_1))
            #1000
            if x_1000 != 0 and x_100 == 0 and x_10 == 0 and x_1 == 0:
                print("%s" %print_1000)
            #1001
            if x_1000 != 0 and x_100 == 0 and x_10 == 0 and x_1 != 0:
                if x_1 == 1:
                    print("%s%s" %(print_1000, print_1_1))
                else:
                    print("%s%s" %(print_1000, print_1))
            #1010
            if x_1000 != 0 and x_100 == 0 and x_10 != 0 and x_1 == 0:
                print("%s%s" %(print_1000, print_10))
            #1011
            if x_1000 != 0 and x_100 == 0 and x_10 != 0 and x_1 != 0:
                if x_1 == 1:
                    print("%s%s%s" %(print_1000, print_10, print_1_1))
                else:
                    print("%s%s%s" %(print_1000, print_10, print_1))
            #1100
            if x_1000 != 0 and x_100 != 0 and x_10 == 0 and x_1 == 0:
                print("%s%s" %(print_1000, print_100))
            #1101
            if x_1000 != 0 and x_100 != 0 and x_10 == 0 and x_1 != 0:
                if x_1 == 1:
                    print("%s%s%s" %(print_1000, print_100, print_1_1))
                else:
                    print("%s%s%s" %(print_1000, print_100, print_1))
            #1110
            if x_1000 != 0 and x_100 != 0 and x_10 != 0 and x_1 == 0:
                print("%s%s%s" %(print_1000,print_100, print_10))
            #1111
            if x_1000 != 0 and x_100 != 0 and x_10 != 0 and x_1 != 0:
                if x_1 == 1:
                    print("%s%s%s%s" %(print_1000, print_100, print_10, print_1_1))
                else:
                    print("%s%s%s%s" %(print_1000, print_100, print_10, print_1))
    print("")