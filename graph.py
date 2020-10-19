class Graph:
    
    def __init__(self):
        import matplotlib.pyplot as plt
        
        self.x=[]
        self.y=[]
        
        self.lelimit=60
        self.alarmlimit=10
        
        self.audio_data = AudioSegment.from_mp3('/home/pi/Desktop/sample.mp3')
        
        self.fig,self.ax=plt.subplots(1,1)
        self.ax.set_facecolor("white")
        self.lines, = self.ax.plot(self.x,self.y)
        

    
    def show(self):
        #グラフを見せる用
        import matplotlib.pyplot as plt
        
        self.lines.set_data(x,y)
            
        self.ax.set_xlim((min(self.x),max(self.x)))
        self.ax.set_ylim((0,max(10,max(self.y))))        
        
        plt.pause(0.01)

    def add(self,value):      
        #表示する値をlistに入れていく
        self.x.append(self.x[-1]+1 if len(self.x)!=0 else 0)
        self.y.append(value)
        if len(self.x)>self.lenlimit:
            self.x.pop(0)
            self.y.pop(0)
            
    def alarm(self):
        import matplotlib.pyplot as plt  
        from pydub.playback import play
        
        if abs(self.y[0]-self.y[-1])<self.alarmlimit:
            play(self.audio_data)            
            self.ax.set_facecolor("red")
        else:
            self.ax.set_facecolor("white")            
    
        
        
        
