class medium:
    v=[]
    r=[]
    rec=""
    def __init__(self,x):
        self.x=x
    def select(self):
        print("Please select from the below ingredients")
        medium.v=[item for item in input(f"{self.x.I[1],self.x.I[2],self.x.I[3],self.x.I[4],self.x.I[7],self.x.I[8],self.x.I[9],self.x.I[10],self.x.I[11],self.x.I[12],self.x.I[13],self.x.I[14],self.x.I[15],self.x.I[16],self.x.I[18]}:").split()]

    
    def search(self):
        for items in medium.v:
            for i in self.x.I:
                if items==i:
                    a=self.x[self.x['I'] == i].index.item()
                    medium.r.append(self.x.R3[a])
                    medium.r.append(self.x.R4[a])
        print("Choose one dish from below choices")
        medium.rec=input(f"{medium.r}:")
        
    def display(self):
        for i in self.x.R3:
                if medium.rec==i:
                    ind=self.x[self.x['R3'] == i].index.item()
                    print("Recipe blog link:",self.x.Y3[ind].split(" ")[0], "\n")
                    print("Youtube video link:",self.x.Y3[ind].split(" ")[1], "\n")

                    
        for i in self.x.R4:
                if medium.rec==i:
                    ind=self.x[self.x['R4'] == i].index.item()
                    print("Recipe blog link:",self.x.Y4[ind].split(" ")[0], "\n")
                    print("Youtube video link:",self.x.Y4[ind].split(" ")[1], "\n")
                    
                   
    
    