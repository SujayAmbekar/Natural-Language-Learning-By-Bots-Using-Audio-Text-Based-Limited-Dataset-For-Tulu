from graph import App

def addWord():
    engW = input("Enter the English word.\n").lower()
    tuluW = input("Enter the Tulu word.\n")
    wType = input("Enter the word type.\n")
    if (app.find_word(engW)==0):
        app.create_node(engW, "English")
    if (app.find_word(tuluW)==0):
        app.create_node(tuluW, "Tulu")
    if (app.find_link(engW, tuluW)==0):
        app.create_link(engW, tuluW, wType)

def addFromDataset(data):
    for line in data:
        word = line.split(',')
        engW = word[0].strip().lower()
        tuluW = word[1].strip()
        wType = word[2].strip()
        if (app.find_word(engW)==0):
            app.create_node(engW, "English")
        if (app.find_word(tuluW)==0):
            app.create_node(tuluW, "Tulu")
        print("Successfully added words")
        if (app.find_link(engW, tuluW)==0):
            app.create_link(engW, tuluW, wType)
        print("Successfully created link")

def addSentence():
    eSent = input("Enter English sentence.\n")
    tSent = input("Enter Tulu sentence.\n")
    eWords = eSent.split(' ')
    tWords = tSent.split(' ')

    #For next section, add words if not seen, add translations, no floating nodes.
    for engW in eWords:
        engW = engW.lower()
        for i in range(len(engW)):
            if engW[i] in ['.',',','?','!','%',':',';']:
                engW[i] = ''
        if (app.find_word(engW)==0):
            app.create_node(engW, "English")
            print("What is the translation of the word " + engW + "?")
            tuluW = input()
            if (app.find_word(tuluW)==0):
                app.create_node(tuluW, "Tulu")
            if (app.find_link(engW, tuluW)==0):
                app.create_link(engW, tuluW, wType)

    for tuluW in tWords:
        for i in range(len(tuluW)):
            if tuluW[i] in ['.',',','?','!','%',':',';']:
                tuluW[i] = ''
        if (app.find_word(tuluW)==0):
            app.create_node(tuluW, "Tulu")
            print("What is the translation of the word " + tuluW + "?")
            engW = input()
            engW = engW.lower()
            if (app.find_word(engW)==0):
                app.create_node(engW, "English")
            if (app.find_link(engW, tuluW)==0):
                app.create_link(engW, tuluW, wType)

#Add sentences to the graph.
    if (app.find_word(eSent)==0):
        app.create_node(eSent, "English")
    if (app.find_word(tSent)==0):
        app.create_node(tSent, "Tulu")
    if (app.find_link(eSent, tSent)==0):
        app.create_link(eSent, tSent, "Sentence")

def addCommunity():
    
    return 0

def makeSentence():

    return 0


if __name__ == "__main__":
    print("Started app.")
    uri = "neo4j+s://2eadc3dc.databases.neo4j.io"
    user = "neo4j"
    password = "Wvkgl4wC8yQD8HrHJCrUWhAbs1RJ4EkWYfT8BsIGDIo"
    app = App(uri, user, password)

#Adding from dataset to graph.
    f = open("dict.txt", "r", encoding='utf-8')
    addFromDataset(f)
    f.close()

#Input interface.
    print("Enter 1 to add words. Enter 0 to exit.")
    while(input()=='1'):
        addWord()
        print("Enter 1 to add words. Enter 0 to exit.")

    app.close()
