"""
 * 파일명 : problem1.py
 * 작성일 : 2020년 11월 3일
 * 작성자 : 문헌정보학과 20142611 이하람
 """

city = ['      ', '서울', '부산', '대구', '인천', '광주', '대전', 
        '울산', '세종', '경기', '강원', '충북', '충남',
        '전북', '전남', '경북', '경남', '제주']
day = 1
yesterday = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
sum = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
while True:
    today = input("%d일차 : " %day)
    today = today.split(",")
    today = list(map(int, today))
    for i in range(17):
        sum[i] = today[i] + sum[i]
    print("")
    for i in range(18):
        print("%-4s" %city[i], end = "")
    print("")
    print("오늘   ", end = "")
    for i in range(17):
        print("%-6d" %today[i], end = "")
    print("")
    print("변동   ", end = "")
    for i in range(17):
        n = today[i]-yesterday[i]
        if n>0:
            print("+", end = "")
            print("%-5d" %n, end = "")
        else:
            print("%-6d" %n, end = "")
    print("")
    print("누계   ", end = "")
    for i in range(17):
        print("%-6d" %sum[i], end = "")
    print("")
    yesterday = today
    day += 1
    print("")
    print("")
