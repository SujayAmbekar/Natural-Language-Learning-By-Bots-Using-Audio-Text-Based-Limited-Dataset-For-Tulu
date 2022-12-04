import random
import pickle
import graph
import add

def closestToZero(d2k, cv):
    d = {}
    for i in cv:
        d[i] = abs(d2k[i])
    if len(d)==0:
        return "END"
    m = min(d.values())
    ans = []
    for i in d:
        if d[i]==m:
            ans.append(i)
    a = random.choice(ans)
    return a

def findpath(f):
#    open_file = open("tuluPOS.txt", "wb")
#    pickle.dump([{}, {}], open_file)
#    open_file.close()
    open_file = open(f, "rb")
    fi = pickle.load(open_file)
    open_file.close()
    d1 = fi[0]
    d2 = fi[1]
    res = []
    cv = set()
    curr = random.choice(d1['L0'])
    while(curr=="END"):
        curr = random.choice(d1['L0'])
    res.append(curr)
    if curr in d2.keys():
        d2k = d2[curr] #dict of possible next pos
        d1k = d1['L1'] #list of pos in next level
        cv = set(d1k).intersection(set(d2k.keys()))
    for i in range(1, len(d1.keys())-1):
        curr = closestToZero(d2k, cv)
        if (curr=="END"):
            break
        res.append(curr)
        d2k = d2[curr]
        d1k = d1['L'+str(i+1)]
        cv = set(d1k).intersection(set(d2k.keys()))
    return res

def update_prob(poslist, val, app):
    if val=="correct":
        add.createPOSer(poslist, app)
    if val=="incorrect":
        add.createPOSer(poslist, app, -1)

def generate_sentence(app):
    poslist = findpath("tuluPOS.txt")
    flag=0
    print(poslist)
    ans=[]
    for i in poslist:
        ans.append(app.find_same_type(i))
        if i in ['WRB', 'WP', 'WDT', 'WP$', 'RB']:
            flag=1
    x  =' '.join(ans)
    if not flag:
        x=x+'.'
    if flag:
        x=x+'?'
#    w = input("Is this sentence correct in terms of semantics? Y/N/X")
#    if w=="Y":
#        add.createPOSer(poslist, app)
#    elif w=="N":
#        add.createPOSer(poslist, app, -1)
    return (x, poslist)
