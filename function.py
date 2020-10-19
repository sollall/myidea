import serial
import time
import datetime

def test_time():
    temp=time.time()
    return temp


def get_ser():
    
    sers=[]
    
    count=0
    while True:
        try:
            temp=serial.Serial("/dev/ttyUSB"+str(count), 2400)
        except:
            break
        count+=1
    
    return sers

def get_gram(ser):
    temp=list(ser.readline())
    temp=list(map(int,temp))
    
    ans=temp[4:12]
    
    for i in range(len(ans)):
        if ans[i]>=176:
            ans[i]-=176
        elif ans[i]>=48:
            ans[i]-=48
        else:
            ans[i]="."
        ans[i]=str(ans[i])
        
    print(float("".join(ans)))
    
    return 1#float("".join(ans))
    
    