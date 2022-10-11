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
    print("Enter 1 to add a sentence. Enter 0 to stop.")
    while(input()=='1'):
        add.addSentence()
        print("Enter 1 to add a sentence. Enter 0 to stop.")

    print("Enter 1 to generate a sentence. Enter 0 to stop.")
    while(input()=='1'):
#        generate.generate_sentence(app)
        print("Enter 1 to generate a sentence. Enter 0 to stop.")

    print("Enter 1 to check accuracy of translation. Enter 0 to stop.")
    while(input()=='1'):
        #print("Accuracy of translation is currently at" + translate.test_tls("testdata.csv", app) +"%.")
        print("Enter 1 to check accuracy of translation. Enter 0 to stop.")

    print("Enter 1 to translate a sentence. Enter 0 to stop.")
    while(input()=='1'):
#       sentence = input("Enter sentence to be translated.")
#       if input("What language input E or T?")=='E':
#           translate.translateEnglish(sentence, app)
#       else:
#           translate.translateTulu(sentence, app)
        print("Enter 1 to translate a sentence. Enter 0 to stop.")

    app.close()
