sentence = input()


def aver(sent):

    for sym in ['!', '?', ';', '.', '"', "'"]:
        sent = sent.replace(sym, '')

    words = sent.split()
    return sum(len(word) for word in words) / len(words) if words else 0


print(aver(sentence))