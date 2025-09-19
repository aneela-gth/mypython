class  GrandFather:
    def init(self, gname, gworth):
        self.gname = gname
        self.gworth = gworth
        print(f"{self.gname} is the Grandfather")
        def gassets(self):
          print(f"{self.gname}'s assets are worth {self.gworth} cr")
class Father(GrandFather):
    def init(self, gname, gworth, pname, pworth):
        super().init(gname, gworth)
        self.pname = pname
        self.pworth = pworth
        print(f"{self.pname} is came reference by {self.gname}")
        def passets(self):
         print(f"{self.pname}'s assets are worth {self.pworth} cr")
class Child(Father):
    def init(self, gname, gworth, pname, pworth, cname):
        super().init(gname, gworth, pname, pworth)
        self.cname = cname
        print(f"{self.cname} is came reference by {self.pname}")
        def cassets(self, cworth):
         self.cworth = cworth
        print(f"{self.cname}'s assets are worth {self.cworth} cr")
    def totalAssets(self):
        print(f"Total assets inherited by {self.cname}: {self.gworth+self.pworth+self.cworth} cr")
sithara = Child("Krishna", 300, "Mahesh Babu", 200, "Sithara")
sithara.cassets(100)
sithara.totalAssets()
sithara.gassets()