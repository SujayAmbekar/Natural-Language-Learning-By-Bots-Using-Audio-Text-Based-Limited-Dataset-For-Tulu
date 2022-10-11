def wer(reference_sent, translation):
    r = reference_sent.split()
    t = translation.split()
    cmn = [i for i in r if i in t]
    ins = [i for i in r if i not in t]
    dele = [i for i in t if i not in r]
    return (len(cmn)+len(ins)+len(dele))/len(reference_sent)
