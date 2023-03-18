#数独

#input
sd2=[[5,3,'',4,'','',8,'',1],
    [8,'','','','','',6,'',''],
    ['','','',3,'',8,'',5,2],
    [7,'',1,'',4,'',5,'',''],
    ['','','',5,'',2,'','',''],
    ['','',5,'',8,'',3,'',7],
    [6,7,'',9,'',4,'','',''],
    ['','',2,'','','','','',5],
    [1,'',4,'','',7,'',6,8]]     #数独二级题

sd=[['',9,'','','','','',4,7],
    [2,'',4,7,'',8,9,'',3],
    ['',7,'','',2,'','',1,''],
    ['',8,'',3,'',2,'',9,''],
    ['','',1,'','','',3,'',''],
    ['',3,'',8,'',5,'',7,''],
    ['',5,'','',3,'','',6,''],
    [1,'',7,4,'',9,5,'',2],
    ['',2,'','','','','',8,'']]

#原始格式操作

def mkkn(shudu):#将未知数('')转换为[1,2,3,4,5,6,7,8,9]
    sdmy=[[],[],[],[],[],[],[],[],[]]
    hs=-1
    for i in shudu:
        ls=-1
        hs+=1
        for k in i:
            ls+=1
            if str(shudu[hs][ls]).isdigit ():#判断是否为数字
                sdmy[hs].append(shudu[hs][ls])
            if shudu[hs][ls]==str():
                sdmy[hs].append([1,2,3,4,5,6,7,8,9])
    return sdmy

def pckn(shudu):     #排除列/行内唯一
    sdmy=shudu.copy()
    hs=-1
    for i in shudu.copy():
        ls=-1
        hs+=1
        for k in i:
            ls+=1
            if type(k)==list:
                for y in k.copy():
                    if y in i:
                        sdmy[hs][ls].remove(y)
                    else:    
                        nhs=[0,1,2,3,4,5,6,7,8]
                        nhs.remove(hs)
                        for z in nhs:
                            if type(shudu[z][ls])==list:
                                continue
                            if y==shudu[z][ls]:
                                sdmy[hs][ls].remove(y)
    return sdmy

def pcdx(shudu):      #唯余
    sdu=shudu.copy()
    for i in sdu:
        for y in i:
            if type(y)==list:
                if len(y)==1:
                    tpi=sdu.index(i)
                    tpy=i.index(y)
                    sdu[tpi][tpy]=y[0]
    return sdu

def qdk(shudu):#列表展开（单个列表）
    for i in shudu:
        if type(i)== list:
            for z in i.copy():
                shudu.insert(shudu.index(i),z)
            shudu.remove(i)
    return shudu

def hnwy(shudu):#行内唯余
    for i in shudu:
        for k in i:
            if type(k) == list:
                for z in k:
                    if qdk(i.copy()).count(z)==1:
                        shudu[shudu.index(i)][shudu[shudu.index(i)].index(k)]=z
                        break
    return shudu

def lnwy(shudu):#列内唯余
    cs=0
    yh=list()
    for i in shudu:
        syhs=[0,1,2,3,4,5,6,7,8]
        syhs.remove(shudu.index(i))
        for k in i:
            ls=shudu[shudu.index(i)].index(k)
            if type(k) == list:
                for z in syhs:
                    if type(shudu[z][ls]) == int:
                        yh.append(shudu[z][ls])
                    if type(shudu[z][ls]) == list:
                        for y in shudu[z][ls]:
                            yh.append(y)
                for n in k:
                    if n not in yh:
                        shudu[shudu.index(i)][ls]=n
    return shudu

def mklist(shudu,ls):
    lie=list()
    for i in shudu:
        lie.append(i[ls])
    return lie


def hzcdelbpc(shudu):#行&列中长度二列表排除
    for i in shudu:
        hs=shudu.index(i)
        for y in i:
            dls=shudu[hs].index(y)
            if type(y) == list:
                if len(y) == 2:
                    temp=shudu[hs].copy()#行中长度二列表排除
                    temp.remove(y)
                    if y in temp:
                        temp.remove(y)
                        for k in temp:
                            ls=shudu[hs].index(k)
                            if type(k) == list:
                                for h in k:
                                        if y[0] == h:
                                            shudu[hs][ls].remove(y[0])
                                        elif y[1] == h:
                                            shudu[hs][ls].remove(y[1])
                    tempp=mklist(shudu,dls)#列中长度二列表排除
                    temppp=tempp.copy()
                    temppp.remove(y)
                    if y in temppp:
                        temppp.remove(y)
                        for l in temppp:
                            hss=tempp.index(l)
                            if type(l) == list:
                                for m in l:
                                    if len(y) == 2:
                                        if y[1] == m:
                                            shudu[hss][dls].remove(y[1])
                                        if y[0] == m:
                                            shudu[hs][dls].remove(y[0])                
    return shudu

'''
def hzcdslbpc(shudu):
    for i in shudu:
        hs=shudu.index(i)
        for y in i:
            ls=shudu[hs].index(y)
            if type(y) == list:
                if len(y) == 3:
'''                    

#九宫格格式操作

def buildjgg(shudu):      #建立九宫格
    jgg=list()
    for i in [0,3,6]:
        jgg.append([shudu[i][0],shudu[i][1],shudu[i][2],shudu[i+1][0],shudu[i+1][1],shudu[i+1][2],shudu[i+2][0],shudu[i+2][1],shudu[i+2][2]])
        jgg.append([shudu[i][3],shudu[i][4],shudu[i][5],shudu[i+1][3],shudu[i+1][4],shudu[i+1][5],shudu[i+2][3],shudu[i+2][4],shudu[i+2][5]])
        jgg.append([shudu[i][6],shudu[i][7],shudu[i][8],shudu[i+1][6],shudu[i+1][7],shudu[i+1][8],shudu[i+2][6],shudu[i+2][7],shudu[i+2][8]])
    return jgg

def buildeh(shudu):#把九宫格转换为原始格式
    eh=list()
    for i in [0,3,6]:
        eh.append([shudu[i][0],shudu[i][1],shudu[i][2],shudu[i+1][0],shudu[i+1][1],shudu[i+1][2],shudu[i+2][0],shudu[i+2][1],shudu[i+2][2]])
        eh.append([shudu[i][3],shudu[i][4],shudu[i][5],shudu[i+1][3],shudu[i+1][4],shudu[i+1][5],shudu[i+2][3],shudu[i+2][4],shudu[i+2][5]])
        eh.append([shudu[i][6],shudu[i][7],shudu[i][8],shudu[i+1][6],shudu[i+1][7],shudu[i+1][8],shudu[i+2][6],shudu[i+2][7],shudu[i+2][8]])
    return eh

def pcjggkn(jgg):#排除宫内唯一
    for i in jgg:
        gs=jgg.index(i)
        for k in i:
            ges=i.index(k)
            if type(k)==list:
                for y in k:
                    if y in i:
                        jgg[gs][ges].remove(y)

def ing(shudu,sd_list1,sd_list2):
    jgg=buildjgg(shudu)
    f=0
    for i in jgg:
        if sd_list1 in i and sd_list2 in i:
            f=1
            return True
    if f == 0:
        return False

def inl(shudu,sd_list1,sd_list2):
    
#输出

def shuchu(shudu):
    for i in shudu:
        print(i)
        print('\n')
    #print(x)
    return None



shudu=mkkn(sd)
for i in range(20):
    shudu=pckn(shudu)
    shudu=hnwy(shudu)
    shudu=lnwy(shudu)
    shudu=pcdx(shudu)



'''数独备份
[[5, 3, [6, 7, 9], 4, [2, 6, 7, 9], [6, 9], 8, [2, 7, 9], 1], [8, [1, 2, 4, 9], [3, 7, 9], [1, 7], [1, 2, 7, 9], 5, 6, [1, 2, 3, 4, 7, 9], [4, 9]], [[4, 9], [1, 4, 6, 9], [6, 7, 9], 3, [1, 6, 7, 9], 8, [1, 4, 7], 5, 2], [7, [2, 6, 8, 9], 1, [6, 8], 4, [3, 6, 9], 5, [2, 3, 8, 9], [6, 9]], [[3, 4, 9], [1, 4, 6, 8, 9], [3, 6, 7, 9], 5, [1, 6, 7, 9], 2, [1, 4, 7], [1, 3, 4, 7, 8, 9], [4, 6, 9]], [[2, 4, 9], [1, 2, 4, 6, 9], 5, [1, 6], 8, [1, 6, 9], 3, [1, 2, 4, 9], 7], [6, 7, 8, 9, 5, 4, [1, 2], [1, 2], 3], [[3, 4, 9], [1, 4, 6, 8, 9], 2, [1, 6, 7, 8], [1, 6, 7, 9], [1, 3, 6, 9], [1, 4, 7], [1, 3, 4, 7, 8, 9], 5], [1, 5, 4, 2, 3, 7, 9, 6, 8]]
'''

#回收站

'''
def pcjggdx(shudu):       #排除宫内唯一
    for i in shudu:
        cs=0
        for y in i:
            if type(y) == int:
                cs+=1
            if cs == 8 :
                for z in i:
                    if type(z) == list:
                        shudutp=shudu[shudu.index(i)].remove()
                        shudu[shudu.index(i)].sort()
                        print(z)
                        for k in range(1,10):
                            if k not in i:
                                shudu[shudu.index(i)][shudu[shudu.index(i)].index(z)]=k
                                break
    return shudu
    '''

'''
sd=[['','',9,'','',1,6,2,''],
    [5,7,'','',2,8,'',3,''],
    [3,'','',7,'','','','',4],
    [8,9,'','',7,'',4,'',''],
    ['',6,'',4,'',3,'',9,''],
    ['','',1,'',9,6,'',7,6],
    [6,'','','','',7,'','',8],
    ['',4,'',1,3,'','',6,5],
    ['',2,7,6,'','',9,'','']]
'''
'''
def 
                            

xsd=mkkn(sd)
'''

#nnsd=pckn(xsd.copy())
#x=list()
'''
for i in nnsd:
    for y in i:
        if type(y)==list:
            x.append(len(y))
#shuchu(nnnsd)
'''
'''
k=[[],[],[],[],[],[],[],[]]
for y in range(8):
    for i in range(9):
        k[y].append('')
k.insert(0,[[1,2],2,3,4,5,6,7,8,9])
pcjggdx(k)
'''

'''
shudu=mkkn(sd)
shudu=pcdx(shudu)

for i in range(20):
    shudu=pckn(shudu)
    shudu=hnwy(shudu)
    shudu=lnwy(shudu)
    shudu=pcdx(shudu)
shuchu(shudu)
'''
