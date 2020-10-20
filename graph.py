class Graph:
    #serialが複数あると仮定したClass
    def __init__(self,N,alarm_limit):
        import matplotlib.pyplot as plt
        from pydub import AudioSegment
        
        self.x=[]
        self.y=[[] for i in range(N)]
        self.N=len(self.y)
        
        self.data_limit=60
        
        self.audio_data = AudioSegment.from_mp3('/home/pi/Desktop/sample.mp3')
        
        self.fig,self.axes=plt.subplots(N)
        self.list_lines=[]
        for i in range(N):
            self.lines, =self.axes[i].plot([],[])
            self.list_lines.append(self.lines)
            self.axes[i].set_facecolor("white")

    
    def show(self,x,y):
        #グラフを見せる用
        import matplotlib.pyplot as plt
        
        self.list_lines=[]
        for i in range(N):
            self.lines, =self.axes[i].plot(x,y[i])
            self.list_lines.append(self.lines)
            self.axes[i].set_facecolor("white")
        
        self.lines.set_data(x,y)
            
        self.ax.set_xlim((min(self.x),max(self.x)))
        self.ax.set_ylim((0,max(10,max(self.y))))        
        
        plt.pause(0.01)

            
    def alarm(self):
        import matplotlib.pyplot as plt  
        from pydub.playback import play
        
        for i in range(N):
            if abs(self.y[0]-self.y[-1])<self.alarmlimit:
                play(self.audio_data)            
                self.ax.set_facecolor("red")
            else:
                self.ax.set_facecolor("white")            
    
temp=Graph(3,[10,10,10])
        
        
