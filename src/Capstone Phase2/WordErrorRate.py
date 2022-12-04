from jiwer import wer
def worderr(reference_sent, translation):
    error = wer(reference_sent, translation)
    print(error)
    return error
