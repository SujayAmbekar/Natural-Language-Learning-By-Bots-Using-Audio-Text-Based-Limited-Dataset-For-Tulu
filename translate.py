import audio
from WordErrorRate import wer

def translateTulu(text, app):
    wordList = removePunctuation(text).split(" ")
    tl = []
    for word in wordList:
        translations = tlw(word, app)

def translateEnglish(text, app):
    wordList = nltk.pos_tag(removePunctuation(text))
    tl = []
    for word in wordList:
        translations = tle(word, app)
        print(translations[0])

def tle(eword, pos, app):
    #refine for multi translation case
    print(app.translateEnglish(eWord, pos))
    return app.translateEnglish(eword, pos)

def tlt(tword, app):
    #refine for multi translation case
    print(app.translateTulu(tWord))
    return app.translateTulu(tWord)

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

def test_tls(f, app):
    a = []
    f = open("data.csv", "r", encoding='utf-8')
    for line in f:
        z = line.split(',')
        tl = translateTulu(z[0])
        a.append(wer(z[1], tl))
    f.close()
    accu = sum(a)/len(a)
    return accu
