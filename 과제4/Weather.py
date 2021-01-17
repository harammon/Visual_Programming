"""
 * 파일명 : Weather.py
 * 작성일 : 2020년 11월 13일
 * 작성자 : 문헌정보학과 20142611 이하람
 """
f = open('Weather.csv', 'r')
v = f.readline()
data = []
while True:
    v = f.readline()
    if v == '':
        break
    v = v[:-1]
    s = v.split(',')
    data.append(s)
city = []
for i in range(len(data)):
    if data[i][1] not in city:
        city.append(data[i][1])     #처음 등장 도시 city리스트에 추가
print("도시를 선택하세요 (", end = "")
for i in range(len(city)):
    if i<len(city)-1:
        print("%d:%s, " %(i+1, city[i]), end = "")
    else:
        print("%d:%s) " %(i+1, city[i]), end = "")
        userInput = int(input())
print("===================================================================================")
i=0
j=0
day = []
temp_dict = {}
rain_dict = {}
while True:
    if data[i][1] == city[userInput -1]:    #입력받은 도시가 data리스트의 도시명과 같다면
        if data[i][2][:7] not in day:   #'년-월'까지 끊은 날짜 데이터가 아직 기존에 day리스트에 없다면, 해당 날짜를 key로 하는 딕셔너리의 value에 리스트를 삽입
            if data[i][3] == "":    #평균 온도가 공백이면
                if data[i][4] != "" and data[i][5] != "":
                    temp_dict[data[i][2][:7]] = [float((float(data[i][4])+float(data[i][5])))/2]
                if data[i][4] != "" and data[i][5] == "":
                    temp_dict[data[i][2][:7]] = [float(data[i][4])]
                if data[i][4] == "" and data[i][5] != "":
                    temp_dict[data[i][2][:7]] = [float(data[i][5])]
            else:
                temp_dict[data[i][2][:7]] = [float(data[i][3])]
            rain_dict[data[i][2][:7]] = [float(data[i][6])]
            day.append(data[i][2][:7])
        else:   #'년-월'까지 끊은 날짜 데이터가 day리스트에 있다면, 해당 날짜를 key로하는 딕셔너리의 value에(리스트) append
            if data[i][3] == "":
                if data[i][4] != "" and data[i][5] != "":
                    temp_dict[data[i][2][:7]].append(float((float(data[i][4])+float(data[i][5])))/2)
                if data[i][4] != "" and data[i][5] == "":
                    temp_dict[data[i][2][:7]].append(float(data[i][4]))
                if data[i][4] == "" and data[i][5] != "":
                    temp_dict[data[i][2][:7]].append(float(data[i][5]))
            else:
                temp_dict[data[i][2][:7]].append(float(data[i][3]))
            rain_dict[data[i][2][:7]].append(float(data[i][6]))
    if i == len(data)-1:
        break
    i += 1  #다음 데이터 행 접근

print("%16s 기후 분석       평균 기온       월별 강수량(mm)" %city[userInput-1])
print("===================================================================================")
while True:
    result = sum(temp_dict[day[j]])
    temp_avg = result / len(temp_dict[day[j]])
    rain_sum = sum(rain_dict[day[j]])
    if day[j][5] == '0':
        print("%16s년 %2s월 %17.1f %20.1f" %(day[j][:4], day[j][6], temp_avg, rain_sum))
    else:
        print("%16s년 %2s월 %17.1f %20.1f" %(day[j][:4], day[j][5:7], temp_avg, rain_sum))
    j += 1
    if j == len(day):
        break