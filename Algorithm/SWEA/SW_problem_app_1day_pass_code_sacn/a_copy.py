import sys
sys.stdin = open('input.txt')

hextobi={'0':'0000','1':'0001','2':'0010','3':'0011','4':'0100',
    '5':'0101','6':'0110','7':'0111','8':'1000','9':'1001','A':'1010',
    'B':'1011','C':'1100','D':'1101','E':'1110','F':'1111'}

ratio = [(2,1,1), (2,2,1), (1,2,2), (4,1,1), (1,3,2), (2,3,1), (1,1,4), (3,1,2), (2,1,3), (1,1,2)]


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
                fo=int(frontonecnt/i)
                bz=int(backzerocnt/i)
                bo=int(backonecnt/i)
                break
   

        for i in range(10):
            if (fo,bz,bo) == ratio[i]:
                bslist.append(i)
        print(bslist)
 
        if len(bslist) == 8 and (tuple(bslist[::-1]) not in set(pslist)):
            pslist.append(tuple(bslist[::-1]))
            bslist=[]
        elif len(bslist) == 8 and (tuple(bslist[::-1]) in set(pslist)):
            bslist=[]
 
        bistr=bistr[0:idx+1]

        if idx == -1:
            return
        else:
            return 뒤에서부터지우기(bistr)
 
T=int(input())
for t in range(1,T+1):
    N,M=map(int,input().split())
    psmat = set()
    for idx in range(N):
        a = input().lstrip('0').rstrip('0')
        if a:
            psmat.add(a)
    print(psmat)
    
    pslist=[]
    bslist=[]
    for i in psmat:
        hexlist=list(i)
        for i in range(len(hexlist)):
            hexlist[i]=hextobi[hexlist[i]]
        bistr="".join(hexlist).rstrip('0')
        print(f'bistr : {bistr}')
        뒤에서부터지우기(bistr)

 
    result=0
    for i in range(len(pslist)):
        if (sum(pslist[i][0:7:2])*3 + sum(pslist[i][1:6:2]) + pslist[i][7]) % 10==0:
            result+=sum(pslist[i])
        else:
            pass
     
    print(f'#{t} {result}')