import sys
sys.stdin = open('input.txt')

hextobi={'0':'0000','1':'0001','2':'0010','3':'0011','4':'0100',
    '5':'0101','6':'0110','7':'0111','8':'1000','9':'1001','A':'1010',
    'B':'1011','C':'1100','D':'1101','E':'1110','F':'1111'}
 
def 뒤에서부터지우기(bistr):
    global pslist
    global bslist
    frontzerocnt=0
    backonecnt=0
    backzerocnt=0
    frontonecnt=0
     

    idx=len(bistr)-1

    if idx>0:
        while bistr[idx]=='1':
            backonecnt+=1
            idx-=1
 
        while bistr[idx]=='0':
            backzerocnt+=1
            idx-=1
 
        while bistr[idx]=='1':
            frontonecnt+=1
            idx-=1
 
        while bistr[idx]=='0':
            frontzerocnt+=1
            idx-=1
 
        for i in range(min(frontonecnt,backzerocnt,backonecnt), 0, -1):
            if frontonecnt%i==0 and backzerocnt%i==0 and backonecnt%i==0:
                r=i
                break
   
        fo=int(frontonecnt/r)
        bz=int(backzerocnt/r)
        bo=int(backonecnt/r)
 
        if (fo,bz,bo) == (2,1,1):
            bslist.append(0)
        elif (fo,bz,bo) == (2,2,1):
            bslist.append(1)
        elif (fo,bz,bo) == (1,2,2):
            bslist.append(2)
        elif (fo,bz,bo) == (4,1,1):
            bslist.append(3)
        elif (fo,bz,bo) == (1,3,2):
            bslist.append(4)
        elif (fo,bz,bo) == (2,3,1):
            bslist.append(5)
        elif (fo,bz,bo) == (1,1,4):
            bslist.append(6)
        elif (fo,bz,bo) == (3,1,2):
            bslist.append(7)
        elif (fo,bz,bo) == (2,1,3):
            bslist.append(8)
        elif (fo,bz,bo) == (1,1,2):
            bslist.append(9)
 
        if len(bslist) == 8 and (tuple(bslist[::-1]) not in set(pslist)):
            pslist.append(tuple(bslist[::-1]))
            bslist=[]
        elif len(bslist) == 8 and (tuple(bslist[::-1]) in set(pslist)):
            bslist=[]
 
        bistr=bistr[0:idx+1]

 
        return 뒤에서부터지우기(bistr)
 
T=int(input())
for t in range(1,T+1):
    N,M=map(int,input().split())
    psmat=[[] for _ in range(N)]
    for idx in range(N):
        psmat[idx]=input().strip()
    
    pslist=[]
    bslist=[]
    for i in range(N):
        if psmat[i]=='0'*M:
            pass
        else:
            tmplst=psmat[i][:]
            hexlist=list(tmplst)
            for i in range(len(hexlist)):
                hexlist[i]=hextobi[hexlist[i]]
            bistr="".join(hexlist).rstrip('0')
            뒤에서부터지우기(bistr)
 
    result=0
    for i in range(len(pslist)):
        if ((pslist[i][0]+pslist[i][2]+pslist[i][4]+pslist[i][6])*3+(pslist[i][1]+pslist[i][3]+pslist[i][5])+pslist[i][7])%10==0:
            result+=pslist[i][0]+pslist[i][2]+pslist[i][4]+pslist[i][6]+pslist[i][1]+pslist[i][3]+pslist[i][5]+pslist[i][7]
        else:
            pass
     
    print(f'#{t} {result}')