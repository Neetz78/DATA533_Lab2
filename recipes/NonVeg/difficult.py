from recipes.NonVeg import nutrition as n
class difficult:
    v=[]
    r=[]
    rec=""
    ind=0
    nut=""
    def __init__(self,x):
        self.x=x
    def select(self):
        print("Please select from the below ingredients")
        difficult.v=[item for item in input(f"{self.x.I[5],self.x.I[0],self.x.I[6],self.x.I[17],self.x.I[18],self.x.I[7]}:").split()]

    
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
            n.display(self.x,difficult.ind)
