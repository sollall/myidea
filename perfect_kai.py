#pandas実装どうしよう

import serial
import time
import datetime

import matplotlib.pyplot as plt
from pydub import AudioSegment
from pydub.playback import play
import pandas as pd

#ser=serial.Serial("/dev/ttyUSB0", 2400)
#print(ser.portstr)

def get_gram():
    st=ser.readline()
    
    lis=list(st)
    ans=list(map(int,lis))
    
    data=st.decode("ASCII", errors="ignore").strip()
    #print(ans)
    ans=ans[4:12]
    
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


#初期値定義
#数字周り
ser=serial.Serial("/dev/ttyUSB0", 2400)
print(ser.portstr)
past=""
x=[]
y=[]
#音声データ
audio_data = AudioSegment.from_mp3('/home/pi/Desktop/sample.mp3')
#グラフ周り
fig,ax=plt.subplots(1,1)
ax.set_facecolor("white")
lines, =ax.plot(x,y)
#dfまわり
df_x=[]
df_y=[]

try:
    while True:
        now=str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))[:19]
        #print("b")
        gram=get_gram()
        #print("c")
        #gram=5.0
        #データの収録
        if now!=past:
            print(now)
            x.append(x[-1]+1 if len(x)!=0 else 0)
            y.append(gram)
            
            df_x.append(now)
            df_y.append(gram+x[-1]*0.1)
            if len(x)>60:
                x.pop(0)
                y.pop(0)
                #ここ関数化したほういいと思う
                if abs(y[-1]-y[0])<=10.0:
                    play(audio_data)
                    ax.set_facecolor("red")
                else:
                    ax.set_facecolor("white")
            #print(x,y)
            lines.set_data(x,y)

            
            ax.set_xlim((min(x),max(x)))
            ax.set_ylim((0,max(10,max(y))))
            
            plt.pause(0.01)
            
            past=now
            #print("a")
except KeyboardInterrupt:
    print("error")
    df=pd.DataFrame({"time":df_x,"values":df_y})
    df.to_csv("test.csv")
        
            
    
    
    
        
        





