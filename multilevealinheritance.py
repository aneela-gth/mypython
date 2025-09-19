class gparentActor:
    def __init__(self,gpname,gpworth):
        self.gpname=gpname
        self.gpworth=gpworth
        print(f"{self.gpname}is the grandparent")
        def gpassets(self):
            print(f"{self.gpname}'s assets are  worth{self.gpworth}cr.")
class parentAcoter(gparentActor):
    def __init__(self, gpname,gpworth,pname,pworth):
        super().__init__(gpname,gpworth)
        self.pname=pname
        self.pworth=pworth
        print(f"{self.pname} is the parent,reference from grandparent {self.pname}")
        def passetes(self,worth):
            self.pworth=worth
            print(f"{self.pname}'sassets are worth {self.pworth}cr")
class chiledAcotor(parentAcoter):
    def __init__(self,gpname,gpworth, pname,pworth,cname):
        super().__init__(gpname,gpworth,pname,pworth)
        self.cname=cname
        self.cworth=0
        print(f"{self.cname}is the child of{self.gpname}and grandchild of{self,gpname}.")
    def cassetes(self,cworth):
        self.cworth=cworth
        print(f"{self.cname}'s assets are worth of{self.cname}cr.")
    def totealassets(self):
        total=self.gpworth+self.pworth+self.cworth
        print(f"total assetes inherited by{self.cname}:{total}cr.")
sithara=chiledAcotor("krishan", 100,"maheshbabu",200,"sithara")
sithara.cassetes(94)



