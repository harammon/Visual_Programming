import readmodule
import writemodule

# readmodule.score_list = [['이하람', '90', '100', '80'], ['김지수', '50', '100', '80']]
def makerank():
    global l1
    l1 = list()
    #print(readmodule.score_list)
    a = readmodule.score_list
    for i in a:
        sum = 0
        for j in i[1:]:
            try:
                if j.isnumeric() == False:
                    raise Exception
                elif int(j)>100 or int(j)<0:
                    raise Exception
            except:
                j = 0
            finally:
                sum += int(j)
        l1.append(sum)
    return l1

readmodule.readdata()
v = makerank()
writemodule.makereport(v)



