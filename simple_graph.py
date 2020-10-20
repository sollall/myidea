import matplotlib.pyplot as plt
from pydub import AudioSegment
from pydub.playback import play

def display(x,y,alarm_value,audio_data):
    N=len(y)
    
    flag=False
    fig,axes=plt.subplots(N)
    
    flag_alarm=False
    
    for i in range(N):
        #linesが使い回し変数なってるけどいいんか???
        lines, =axes[i].plot(x,y[i])
        lines.set_data(x,y[i])
        
        axes[i].set_xlim((min(x),max(x)))
        axes[i].set_ylim((0,max(10,max(y[i]))))        
        
        print(y[i])
        if abs(y[i][0]-y[i][-1])<alarm_value[i]:
            axes[i].set_facecolor("red")
            flag_alarm=True
        else:
            axes[i].set_facecolor("white")
        
    if flag:
        play(audio_data)
    
    plt.pause(0.01)
    
    return 

fig,axes=plt.subplots(2)
list_lines=[]
for i in range(len(axes)):
    lines, =axes[i].plot([0],[0])
    list_lines.append(lines)
    

x=[1,2,3]
y=[[10,20,30],[10,20,30]]


while True:

    x.append(x[-1]+1)
    y[0].append(y[0][-1]+0.1)
    y[1].append(y[1][-1]+1)
    if len(x)>30:
        x.pop(0)
        y[0].pop(0)
        y[1].pop(0)

    #関数じゃ無理じゃね Class化する？？？
    display(x,y,[3,3],AudioSegment.from_mp3('/home/pi/Desktop/sample.mp3'))
    
    
    
    
    