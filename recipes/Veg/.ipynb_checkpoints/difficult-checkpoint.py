from recipes.Veg import nutrition as n
class difficult:
    v=[]
    r=[]
    rec=""
    nut=""
    ind=0
    def __init__(self,x):
        self.x=x
    def select(self):
        print("Please select from the below ingredients")
        difficult.v=[item for item in input(f"{self.x.I[1],self.x.I[2],self.x.I[3],self.x.I[4],self.x.I[7],self.x.I[8],self.x.I[9],self.x.I[10],self.x.I[11],self.x.I[12],self.x.I[13],self.x.I[14],self.x.I[15],self.x.I[16],self.x.I[18]}:").split()]

    
    def search(self):
        for items in difficult.v:
            for i in self.x.I:
                if items==i:
                    a=self.x[self.x['I'] == i].index.item()
                    difficult.r.append(self.x.R5[a])
                    difficult.r.append(self.x.R6[a])
        print("Choose one dish from below choices")
        difficult.rec=input(f"{difficult.r}:")
        
    def display(self):
        for i in self.x.R5:
                if difficult.rec==i:
                    difficult.ind=self.x[self.x['R5'] == i].index.item()
                    print("Recipe blog link:",self.x.Y5[difficult.ind].split(" ")[0], "\n")
                    print("Youtube video link:",self.x.Y5[difficult.ind].split(" ")[1], "\n")

                    
        for i in self.x.R6:
                if difficult.rec==i:
                    difficult.ind=self.x[self.x['R6'] == i].index.item()
                    print("Recipe blog link:",self.x.Y6[difficult.ind].split(" ")[0], "\n")
                    print("Youtube video link:",self.x.Y6[difficult.ind].split(" ")[1], "\n")
                    
                   
    
class steps(difficult):
    def __init__(self,data):
        difficult.__init__(self,data)
    def sdiff(self):
        self.select()
        self.search()
        self.display()
        print("Do you want to know the calorie count?")
        difficult.nut=input("Yes or No")
        if difficult.nut=="Yes":
            n.ddisplay(self.x,difficult.rec,difficult.ind)
    