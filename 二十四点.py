#二十四点
from easygui import enterbox,msgbox
def apd(num):
    if num not in answer:
        if len(shuru)!=len(set(shuru)) or len(shuru)==len(set(kk)):
            
            answer.append(num)
        #print(num)
aa=0
kk=list()
answer=list()
try:
    shuru=list(map(int, enterbox('Four numbers?','四个数','').split(' ')))
except:
    msgbox('Write numbers please!','error','')
    exit()
temped=str()
for i in shuru:
    dylt=shuru.copy()
    dylt.remove(i)
    for x in dylt:
        delt=dylt.copy()
        delt.remove(x)
        for y in delt:
            dslt=delt.copy()
            dslt.remove(y)
            z=dslt[0]
            for a in [1,2,3,4]:
                for b in [1,2,3,4]:
                    for c in [1,2,3,4]:
                        try:
                            if a==1:
                                temped=('{}+{}'.format(str(i),str(x)))
                                kk.append(i)
                                kk.append(x)
                            elif a==2:
                                temped=('{}-{}'.format(str(i),str(x)))
                                kk.append(i)
                                kk.append(x)
                            elif a==3:
                                temped=('{}*{}'.format(str(i),str(x)))
                                kk.append(i)
                                kk.append(x)
                            elif a==4:
                                temped=('{}/{}'.format(str(i),str(x)))
                                kk.append(i)
                                kk.append(x)
                            if b==1:
                                temped=('{}+{}'.format(temped,str(y)))
                                kk.append(y)
                            elif b==2:
                                temped=('{}-{}'.format(temped,str(y)))
                                kk.append(y)
                            elif b==3:
                                temped=('{}*{}'.format(temped,str(y)))
                                kk.append(y)
                            elif b==4:
                                temped=('{}/{}'.format(temped,str(y)))
                                kk.append(y)
                            if c==1:
                                temped=('{}+{}'.format(temped,str(z)))
                                kk.append(z)
                            elif c==2:
                                temped=('{}-{}'.format(temped,str(z)))
                                kk.append(z)
                            elif c==3:
                                temped=('{}*{}'.format(temped,str(z)))
                                kk.append(z)
                            elif c==4:
                                temped=('{}/{}'.format(temped,str(z)))
                                kk.append(z)
                        except ZeroDivisionError:
                            continue
                        if sum(kk)!=sum(shuru):
                            kk.clear()
                            continue

                        try:
                            if eval('((({}){}){})'.format(temped[0:3],temped[3:5],temped[5:7]))==24:
                                apd('{}[({}){}]{}{}'.format('{',temped[0:3],temped[3:5],temped[5:7],'}'))
                                aa=1    
                            if eval('{}({}){}'.format(temped[0:2],temped[2:5],temped[5:]))==24.0:
                                apd('{}({}){}'.format(temped[0:2],temped[2:5],temped[5:]))
                                aa=1
                            if eval('{}({})'.format(temped[0:4],temped[4:]))==24.0:
                                apd('{}({})'.format(temped[0:4],temped[4:]))
                                aa=1
                            if eval('{}({})'.format(temped[0:2],temped[2:]))==24.0:
                                apd('{}({})'.format(temped[0:2],temped[2:]))
                                aa=1
                            if eval('({}){}({})'.format(temped[0:3],temped[3:4],temped[4:]))==24.0:
                                apd('({}){}({})'.format(temped[0:3],temped[3:4],temped[4:]))
                                aa=1
                            if eval(temped)==24.0:
                                apd(temped)
                                aa=1
                            if eval('({}({})){}'.format(temped[0:2],temped[2:5],temped[5:]))==24.0:
                                apd('[({}{}){}]'.format(temped[0:2],temped[2:5],temped[5:]))
                                aa=1
                            if abs(eval('{}({})'.format(temped[0:2],temped[2:7]))-24)<0.0000000001:
                                apd('[{}({})]'.format(temped[0:2],temped[2:7]))
                                aa=1
                            
#                            if eval('{}({}({}))').format(temped[0:2],temped[2:5],temped[5:]))==24.0:
                                
                        except Exception as r:
                            continue
                        kk.clear()
                        cs=0
if aa!=1:
    print('no')
if answer != []:
    msgbox(answer)
    
#if len(shuru[0])==1 and len(shuru[2])==1 and len(shuru[3])==1 and len(shuru[4])==1:
#                            if len(kk)!=len(set(kk)):
#                                kk.clear()
#                                continue
                            
                                    