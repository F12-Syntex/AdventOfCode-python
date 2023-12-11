t1 = '01:01:57'
t2 = '01:25:34'

def timeCalc(t1, t2):
    t1 = t1.split(':')
    t2 = t2.split(':')
    t1 = [int(i) for i in t1]
    t2 = [int(i) for i in t2]
    t1 = t1[0]*3600 + t1[1]*60 + t1[2]
    t2 = t2[0]*3600 + t2[1]*60 + t2[2]
    t3 = t2 - t1
    t3 = str(t3//3600) + ':' + str(t3%3600//60) + ':' + str(t3%60)
    return t3

print(timeCalc(t1, t2))