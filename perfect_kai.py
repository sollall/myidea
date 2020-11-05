#pandas実装どうしよう

import serial
import time
import datetime

import matplotlib.pyplot as plt
from pydub import AudioSegment
from pydub.playback import play
import pandas as pd

import functions
import simple_graph


#初期値定義
#数字周り
#print(ser.portstr)


#dfまわり

"""__init__"""
sers=functions.get_ser()

#N>=2じゃないとバグるの草
N=len(sers)
N=2#テスト
x=[]
y=[[] for i in range(len(sers))]
past=str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))[:19]
alarm=[0.1,0.1]
#音声データ
audio_data = AudioSegment.from_mp3('/home/pi/Desktop/sample.mp3')
#グラフ周り
fig,axes=plt.subplots(N)
print(len(axes))
for i in range(N):
    axes[i].set_facecolor("white")

#dataframe周り
#temp_x={"Time":[]}
#temp_y={k:[] for k in sers}
df_data={k:[0] for k in (["Time"]+[str(n) for n in range(N)])}
print(df_data)

csv_name=past+".csv"


#テストここから
while True:

    df_data["Time"].append(df_data["Time"][-1]+1)
    df_data["0"].append(df_data["0"][-1]+0.1)
    df_data["1"].append(df_data["1"][-1]+1)
    
    #リストを作っといてそこからデータフレームを構成するほうが早い？
    df=pd.DataFrame(df_data)
    
    simple_graph.display(df_data["Time"][-30:],[df_data["0"][-30:],df_data["1"]][-30:],[3,3],AudioSegment.from_mp3('/home/pi/Desktop/sample.mp3'))
    df.to_csv(csv_name)
#テストここまで


try:
    while True:
        now=str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))[:19]
        
        if now!=past:
            #時間の更新
            x.append(now)
            
            for i in range(N):
                #もし途中でUSBが外れて値を請求できなかったら？→tryで逃げよう
                gram=functions.get_gram(sers[i])
                y[i].append(gram)
            
            measure=[x[-1]]+[y[n][-1] for n in range(N)]
            measure=pd.Series(measure, index=df.columns,name=df.index[-1]+1 if len(df.index)!=0 else 0)
            df=df.append(measure)
            
            #グラフの更新
            if len(x)>30:
                x.pop(0)
                y[0].pop(0)
                y[1].pop(0)
                
            simple_graph.display(x,y,[3,3],AudioSegment.from_mp3('../sample.mp3'))
            
            #csvの保存　毎回保存してたらくそおそくなるきがする
            df.to_csv(csv_name)
            
            #今回は成功　次のloopへ
            past=now
            #print("a")
except KeyboardInterrupt:
    print("error")

