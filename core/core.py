class Command(object):
    def open(self, road):
        self.pftc = open(road, mode="r+")
        self.pftcl = self.pftc.read().split(")")
        return 0
    
    def write(self, xy, c):
        f = False
        n = 0
        for i in self.pftcl:
            th = i.split(":")
            if th[0] == xy:
                self.pftcl[n] = xy + ":" + c
                f = True
                break
            n += 1
        if f == False:
            self.pftcl[len(self.pftcl) + 1] = xy + ":" + c
        return 0
        
    def read(self, xy):
        r = -1
        f = False
        for i in self.pftcl:
            th = i.split(":")
            if th[0] == xy:
                r = th[1]
                break
        return r
    
    def save(self):
        wstr = ""
        for i in self.pftcl:
            wstr += i
            wstr += ")"
        self.pftc.seek(0)
        self.pftc.truncate()
        self.pftc.write(wstr)
        return 0
