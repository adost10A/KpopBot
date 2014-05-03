class Kpop:
    def __init__(self,artist = '',members = []):
        self.artist = artist
        self.members = members
    def getMembers(self):
        return self.members
    def getArtists(self):
        return self.artist
        
map = open('Kpop.txt','r')
log = map.readlines()
KpopDict = {}

for logs in log:
    pice = logs[:-1].split('\t')
    KpopDict[pice[0]] = pice[1]
def getMembers(Name):
    for keys in KpopDict:
        if keys == Name:
            return KpopDict[Name]
def getName(Group):
    for keys in KpopDict.keys():
        pass
print KpopDict.keys()
CallList = []
for i in KpopDict:
    x = str('!') + i
    CallList.append(x)
Dic = dict(zip(CallList,KpopDict.values()))

