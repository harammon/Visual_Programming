"""
 * 파일명 : 5.py
 * 작성일 : 2020년 10월 3일
 * 작성자 : 문헌정보학과 20142611 이하람
 * 출력결과 : 9592 개
              It took  1.5887486934661865  seconds.
 """
import time
startTime = time.time()
cnt = 0
for i in range(2, 100001):
    for j in range(2, int(i**(1/2))+1): 
        if (i%j) == 0: 
            cnt = cnt + 1
            break
result = (100000-1) - cnt
print(result, "개")
endTime = time.time()
print ("It took ", endTime-startTime, " seconds.")   