import string
import nltk
import pickle
import spacy
nlp = spacy.load("en_core_web_sm")

def addWord(engW, tuluW, wType, gender, app):
    if (app.find_word(engW)==0):
        app.create_node(engW, "English")
    if (app.find_word(tuluW)==0):
        app.create_node(tuluW, "Tulu")
    if (app.find_link(engW, tuluW)==0):
        app.create_link(engW, tuluW, wType, gender)

def addFromDataset(data, app):
    for line in data:
        word = line.split(',')
        engW = word[0].strip().lower()
        tuluW = word[1].strip()
        wType = word[2].strip()
        gender = word[3].strip()
        addWord(engW, tuluW, wType, gender, app)

def removePunctuation(sentence):
    x = sentence.replace("'", "")
    y = x.translate(str.maketrans('', '', string.punctuation))
    y = y.lower()
    return y

def addSentence(app):
    eSent = input("Enter English sentence.\n")
    tSent = input("Enter Tulu sentence.\n")
    addSent(eSent, tSent, app)

def getinfo(engw, pos, app):
    tw = input("What does "+engw+" translate to in the given sentence if POS is "+pos+" ?").lower()
    gender = input("What is the gender? Enter masculine/feminine/neuter/NULL. ")
    addWord(engw, tw, pos, gender, app)

def getinfot(tw, app):
    engw = input("What does "+tw+" translate to in the given sentence?").lower()
    gender = input("What is the gender? Enter masculine/feminine/neuter/NULL. ")
    e = nlp(engw)
    pos = e[0].tag_
    addWord(engw, tw, pos, gender, app)

def addSent(eSent, tSent, app):
    eSent = removePunctuation(eSent)
    tSent = removePunctuation(tSent)
    addWord(eSent, tSent, "Sentence", "None", app)
    eWords = eSent.split(' ')
    tWords = tSent.split(' ')
    doc = nlp(eSent)
    eWord = [(token.text, token.tag_) for token in doc]
#    eWords = nltk.pos_tag(eWords)
    tags = [i[1] for i in eWord]
    for i in eWord:
        if app.find_word(i[0]):
            if app.translate_english(i[0], i[1]) in tWords:
                continue
        else:
            getinfo(i[0], i[1], app)
    for i in tWords:
        if app.find_word(i):
            if app.translate_tulu(i) in eWords:
                continue
        else:
            getinfot(i, app)
    ttags = []
    for i in tWords:
        print(i)
        print(app.translate_tulu(i))
        ttags.append(app.translate_tulu(i)[0][1])
    print(ttags)
#    open_file = open("engPOS.txt", "wb")
#    pickle.dump([{}, {}], open_file)
#    open_file.close()
    createPOSer(tags, "E")
    createPOSer(ttags, "T")

def createPOSer(tags, language, weight=1):
    if language == "E":
        fi = open("engPOS.txt", "rb")
        f = pickle.load(fi)
        fi.close()
    else:
        fi = open("tuluPOS.txt", "rb")
        f = pickle.load(fi)
        fi.close()
    d = f[0]
    seqs = f[1]
    #d = {'L1':[noun, pronoun, article], 'L2':['adj','noun']}
    if "START" not in seqs.keys():
        seqs["START"] = dict()
    seqs["START"][tags[0]] = 0
    if tags[-1] not in seqs.keys():
        seqs[tags[-1]] = dict()
    seqs[tags[-1]]["END"] = 0
    #seqs = {noun:{prp: 3, vb: 4}, }
    for i in range(len(tags)):
        ind = "L"+str(i)
        if ind in d.keys():
            if tags[i] not in d[ind]:
                d[ind].append(tags[i])
        else:
            d[ind] = [tags[i]]
        if i==len(tags)-1:
            break
        #seqs = {'NN': {'PRP': 1}, 'PRP': {'VBP': 1}, 'VBP': {'JJ': 1}}
        if tags[i] in seqs.keys():
            if tags[i+1] in seqs[tags[i]].keys():
                seqs[tags[i]][tags[i+1]] += weight
            else:
                seqs[tags[i]][tags[i+1]] = weight
        else:
            seqs[tags[i]] = dict()
            seqs[tags[i]][tags[i+1]] = weight
    if language == "E":
        fi = open("engPOS.txt", "wb")
        pickle.dump([d, seqs], fi)
        fi.close()
    else:
        fi = open("tuluPOS.txt", "wb")
        pickle.dump([d, seqs], fi)
        fi.close()
