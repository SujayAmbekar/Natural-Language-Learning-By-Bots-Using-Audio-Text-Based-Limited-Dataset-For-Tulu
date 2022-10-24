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
    eSent = removePunctuation(input("Enter English sentence.\n").lower())
    tSent = removePunctuation(input("Enter Tulu sentence.\n"))
    addWord(eSent, tSent, "Sentence", "None", app)
#    eWords = eSent.split(' ')
#    tWords = tSent.split(' ')
#    for word in eWords:
#        word = removePunctuation(word)

    doc = nlp(eSent)
    eWords = [(token.text, token.tag_) for token in doc]
#    eWords = nltk.pos_tag(eWords)
    tags = [i[1] for i in eWords]
#    open_file = open("engPOS.txt", "wb")
#    pickle.dump([{}, {}], open_file)
#    open_file.close()
    createPOSer(tags, "E")
    #add words and links to graph

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
    print(d, seqs)
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
