class Dataframe:
    
    def __init__(self):
        self.x=[]
        self.y=[]
        
    def add(self,time,value):
        self.x.append(time)
        self.y.append(value)
        
    def make_csv(self):
        import pandas as pd
        print("おつかれなす")
        self.df=pd.DataFrame({"time":self.x,"values":self.y})
        self.df.to_csv("名前募集中.csv")
        
        