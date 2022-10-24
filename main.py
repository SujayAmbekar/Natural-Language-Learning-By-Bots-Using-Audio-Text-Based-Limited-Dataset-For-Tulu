from graph import App
import string
import nltk
import pickle

import add
import generate
import translate

if __name__ == "__main__":
    print("Started app.")
    uri = "neo4j+s://2eadc3dc.databases.neo4j.io"
    user = "neo4j"
    password = "Wvkgl4wC8yQD8HrHJCrUWhAbs1RJ4EkWYfT8BsIGDIo"
    app = App(uri, user, password)
#Adding from dataset to graph.
    print("Enter 1 to add from dataset. Enter 0 to skip.")
    if(input()=='1'):
        f = open("data.csv", "r", encoding='utf-8')
        add.addFromDataset(f, app)
        f.close()

#Input interface.
    i=10
    while(i):
        print("Enter 1 to add a sentence.\nEnter 2 to generate a sentence.\nEnter 3 to translate a sentence.\nEnter 4 to check accuracy of translation.\nEnter 0 to stop.")
        i=int(input())
        if i==1:
            add.addSentence(app)
        if i==2:
            generate.generate_sentence(app)
        if i==4:
            print("Accuracy of translation is currently at" + translate.test_tls(app) +"%.")
        if i==3:
            sentence = input("Enter sentence to be translated.")
    #       if input("What language input E or T?")=='E':
            translate.translateEnglish(sentence, app)
    #       else:
    #           translate.translateTulu(sentence, app)

#    translate.translateTulu("puchchae mara", app)
#    translate.translateEnglish("big cat inside tree", app)
    app.close()
