import audio
from WordErrorRate import wer
import string
from graph import App
import nltk

def removePunctuation(sentence):
    x = sentence.replace("'", "")
    y = x.translate(str.maketrans('', '', string.punctuation))
    y = y.lower()
    return y

def translateTulu(text, app):
    wordList = removePunctuation(text).split(" ")
    tl = []
    for word in wordList:
        translations = tlt(word, app)
        tl.append(translations[0])
    return(" ".join(tl))

def translateEnglish(text, app):
    wordList = nltk.pos_tag(removePunctuation(text).split())
    tl = []
    for word in wordList:
        translations = tle(word[0], word[1], app)
        tl.append(translations[0])
    return(" ".join(tl))

def tle(eword, pos, app):
    #refine for multi translation case
    return app.translate_english(eword, pos)

def tlt(tword, app):
    #refine for multi translation case
    return app.translate_tulu(tword)

def translate_path(f, sent):
    trans = []
    tagged = nltk.pos_tag(nltk.word_tokenise(engSent))
    t = [i[1] for i in tagged]
    for word in tagged:
        trans.append(tl(word), word[1])
    #d = pickle.load(open('mypickle.pickle'))
    #get word type sequence from d
    print(' '.join(trans)+'.')
    return

def test_tls(app):
    a = []
    f = open("testdata.csv", "r", encoding='utf-8')
    #file containing english tulu sentence pairs
    for line in f:
        z = line.split(',')
        tl = translateTulu(z[0])
        a.append(wer(z[1], tl))
    f.close()
    accu = sum(a)/len(a)
    return accu
