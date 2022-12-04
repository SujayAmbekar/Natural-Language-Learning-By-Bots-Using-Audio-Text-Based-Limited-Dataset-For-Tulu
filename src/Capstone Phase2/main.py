from graph import App
import string
import nltk
import pickle
import audio
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
#    print("Enter 1 to add from dataset. Enter 0 to skip.")
#    if(input()=='1'):
#        f = open("data.csv", "r", encoding='utf-8')
#        add.addFromDataset(f, app)
#        f.close()

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
            print("Accuracy of translation for easy dataset is at" + str("{0:.4f}".format((1-translate.test_tls("dataeasy.csv", app))*100) +"%."))
            print("Accuracy of translation for hard dataset is at" + str("{0:.4f}".format((1-translate.test_tls("datahard.csv", app))*100) +"%."))
            print("Accuracy of translation for complex dataset is at" + str("{0:.4f}".format((1-translate.test_tls("datacomp.csv", app))*100) +"%."))
        if i==3:
            sentence = "Rama and cats have played."
            sentence = input("Enter sentence to be translated.")
            if input("What language input E or T?")=='E':
                print(translate.translateEnglish(sentence, app))
            else:
                print(translate.translateTulu(sentence, app))
    app.close()
