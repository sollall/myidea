#pandas実装どうしよう

import serial
import time
import datetime

import matplotlib.pyplot as plt
from pydub import AudioSegment
from pydub.playback import play
import pandas as pd

import functions


#初期値定義
#数字周り
#print(ser.portstr)



#dfまわり

"""__init__"""
sers=functions.get_ser()
N=len(sers)
x=[]
y=[[] for i in range(len(sers))]
past=""
#音声データ
audio_data = AudioSegment.from_mp3('/home/pi/Desktop/sample.mp3')
#グラフ周り
fig,axes=plt.subplots(N)
for i in range(N):
    axes[i].set_facecolor("white")
    lines, =axes[i].plot(x,y)
#dataframe周り
"""ちょっと待て　columnの名前決めるのめんどい"""



try:
    while True:
        now=str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))[:19]

        if now!=past:
            x.append(now)
            for i in range(N):
                #もし途中でUSBが外れて値を請求できなかったら？→tryで逃げよう
                gram=functions.get_gram(sers[i])
                
                
            past=now
            #print("a")
except KeyboardInterrupt:
    #CTRl+Cで潰すのもありだけど　開始時間を名前にしたcsv作ってそれを更新し続けるほうが安定するのでは？？？　
    #もちろん速さ次第だけど
    print("error")
    df=pd.DataFrame({"time":df_x,"values":df_y})
    df.to_csv("test.csv")
        
            
    
    
    
        
        





