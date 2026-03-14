import random
class Domanda:
    #def __init__(self, testo="", diff=None, corretta="", opzioni[]):
    def __init__(self, testo, livello, corretta, errate):
        self.testo = testo
        self.livello = livello
        self.corretta = corretta
        self.errate = errate

    #creo una classe domanda con il testo, il livello,
    # la risposta corretta e quelle errate, so dove è quella corretta
    # perché me lo dice il testo, poi le mischierò

    #def opzioni_random(self):
    #    random.shuffle(self.opzioni)
    #    return self.opzioni

    def get_risposte_mischiate(self):
        risposte = [self.corretta] + self.errate
        random.shuffle(risposte)
        return risposte