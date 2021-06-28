import pickle


def save(est):
    with open('biblio', 'bw') as f:
        pickle.dump(est, f)


def load():
    with open('biblio', 'br') as f:
        temp = pickle.load(f)

    return temp
