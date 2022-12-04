import audio
from WordErrorRate import worderr
import string
from graph import App
import nltk
from spacy import load
import pickle
nlp = load("en_core_web_sm")

def removePunctuation(sentence):
    x = sentence.replace("'", "")
    y = x.translate(str.maketrans('', '', string.punctuation))
    y = y.lower()
    return y.strip()

def translateTulu(text, app):
    text = removePunctuation(text)
    #First check if sentence exists.
    w = tlt(text, app)
    for i in w:
        return i[0]
    #Else translate ngram by ngram. If word has no translation, return same word.
    wordList = text.split(" ")
    t = []
    poslist = []
    i = 0
    while i<len(wordList):
        if x:=tlt(" ".join(wordList[i:i+3]), app): #if trigram exists
            t.append(x[0][0])
            poslist.append(x[0][1])
            i=i+3
        elif x:=tlt(" ".join(wordList[i:i+2]), app): #if bigram exists
            t.append(x[0][0])
            poslist.append(x[0][1])
            i = i+2
        elif x:=tlt(wordList[i], app): #if translation exists
            t.append(x[0][0])
            poslist.append(x[0][1])
            i = i+1
        else: #if no translation exists
            t.append(wordList[i])
            poslist.append('X')
            i = i+1
    try:
        path = translate_path("tuluPOS.txt", poslist)
    except:
        path = poslist
    if path==poslist:
        return(" ".join(t))
    toRet = " ".join(t)
    try:
        toRet = " ".join(sorted(t, poslist, path))
    except:
        print("No path reshuffling.")
    return toRet

def translateEnglish(text, app):
    #wordList = nltk.pos_tag(removePunctuation(text).split())
    w = tle(removePunctuation(text), "Sentence", app)
    if len(w):
        return w[0]

    text = removePunctuation(text)
    doc = nlp(text)
    s = text.split()
    wordList = [(token.text, token.tag_) for token in doc]

    t = []
    poslist = []
    i = 0
    while i<len(wordList):
        if x:=tlngram(" ".join(s[i:i+3]), app): #if trigram exists
            t.append(x[0][0])
            poslist.append(x[0][1])
            i=i+3
        elif x:=tlngram(" ".join(s[i:i+2]), app): #if bigram exists
            t.append(x[0][0])
            poslist.append(x[0][1])
            i = i+2
        elif x:=tle(wordList[i][0], wordList[i][1], app): #if translation exists
            t.append(x[0])
            poslist.append(wordList[i][1])
            i = i+1
        elif x:=tlngram(wordList[i][0], app): #if translation WITHOUT pos exists
            t.append(x[0][0])
            poslist.append(x[0][1])
            i = i+1
        else: #if no translation exists
            t.append(wordList[i][0])
            poslist.append(wordList[i][1])
            i = i+1
    try:
        path = translate_path("engPOS.txt", poslist)
    except:
        path = poslist
    if path==poslist:
        return(" ".join(t))
    toRet = " ".join(t)
    try:
        toRet = " ".join(sorted(t, poslist, path))
    except:
        print("No path reshuffling.")
    return toRet

def sorted(w, orig, destination):
    sortedList = []
    while (len(orig)>0):
        indToApp = orig.index(destination[0])
        sortedList.append(w[indToApp])
        orig.pop(orig.index(destination[0]))
        destination.pop(0)
        w.pop(w.index(sortedList[-1]))
    return sortedList

def tle(eword, pos, app):
    return app.translate_english(eword, pos)

def tlngram(eword, app):
    return app.translate_ngram(eword)

def tlt(tword, app):
    return app.translate_tulu(tword)

def translate_path(f, inp):
    print(inp)
    open_file = open(f, "rb")
    fi = pickle.load(open_file)
    open_file.close()
    d1 = fi[0]
    d2 = fi[1]
    if len(d1)<len(inp) or len(inp)>=6:
        return inp
    d1local = dict()
    d2local = dict()
    inpset = set(inp)
    inpset.add('END')
    for i in range(len(inp)+1):
        ind = 'L'+str(i)
        d1local[ind] = set(d1[ind]).intersection(inpset)
    for i in inp:
        if i in d2.keys():
            d2local[i] = d2[i].copy()
            for j in d2[i]:
                if (j not in inpset):
                    d2local[i].pop(j)
        else:
            continue
    res = []
    for i in d1local['L0']:
        res.append([i])
    lastele = list(d1local['L0'])
    #{'L0': {'NNP', 'VB'}, 'L1': {'TO'}, 'L2': {'VB'}, 'L3': {'END'}}
    #{'NNP': {'TO': 1}, 'VB': {'END': 0}, 'TO': {'VB': 1}}
    for i in range(1, len(inp)+1):
        if (len(set(lastele))==1) and (lastele[-1]=='END'):
            break
        newres = []
        for j in range(len(res)):
            if res[j][-1]=='END':
                continue
            for k in d2local[lastele[j]]: #for every element transitioning to
                if k in d1local['L'+str(i)]:
                    t = res[j]
                    t.append(k)
                    newres.append(t)
        res = newres
        lastele = [ele[-1] for ele in res]
    reswts = [0]*len(res)
    for i in res:
        for j in range(len(i)-1):
            reswts[res.index(i)] += d2local[i[j]][i[j+1]]
    if len(res)==0:
        return inp
    m = reswts.index(max(reswts))
    return res[m][:-1]


def test_tls(filename, app):
    a = []
    f = open(filename, "r", encoding='utf-8')
    #file containing english tulu sentence pairs
    for line in f:
        z = line.split(',')
        tl = translateTulu(z[1], app)
        print(tl)
        en = removePunctuation(z[2])
        a.append(worderr(en, tl))
    f.close()
    accu = round(sum(a)/len(a), 4)
    return accu
