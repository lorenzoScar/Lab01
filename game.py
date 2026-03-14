from domanda import Domanda
import random

class Game:

    def __init__(self):
        self.domande = []
        self.livelli = {}

    def carica_domande(self, file):

        with open(file, "r") as f:

            while True:

                testo = f.readline().strip()

                if testo == "":
                    break

                livello = int(f.readline().strip())
                corretta = f.readline().strip()

                errate = [
                    f.readline().strip(),
                    f.readline().strip(),
                    f.readline().strip()
                ]

                domanda = Domanda(testo, livello, corretta, errate)

                self.domande.append(domanda)

                f.readline()
        self.ordina_per_livello()

    def ordina_per_livello(self):
        #creo un dizionario 0:domanda1,domanda2 ; 1:domanda3,domanda4

        for d in self.domande:
            if d.livello not in self.livelli:
                self.livelli[d.livello] = []

            self.livelli[d.livello].append(d)

    def aggiorna_punteggio(self, file, nickname, punteggio):

        punteggi = []

        with open(file, "r") as f:
            for riga in f:
                parti = riga.strip().split()

                if len(parti) == 2:
                    nome = parti[0]
                    punti = int(parti[1])
                    punteggi.append((nome, punti))

        punteggi.append((nickname, punteggio))

        punteggi.sort(key=lambda x:x[1], reverse=True)

        with open(file, "w") as f:
            for nome, punti in punteggi:
                f.write(f" {nome} {punti}\n")

    def gioca(self):

        livello = 0;
        punteggio = 0;
        livello_max = max(self.livelli.keys())
        #avendo fatto il dizionario, trovo il max dalle chiavi

        while True:
            domanda = random.choice(self.livelli[livello])

            print(f"\nLivello {livello} {domanda.testo}")

            risposte = domanda.get_risposte_mischiate()

            for i, r in enumerate(risposte, 1):
                print(f"{i}. {r}")

            scelta = int(input("Inserisci la risposta (1, 2, 3, 4): "))

            if risposte[scelta-1] == domanda.corretta:
                print("Risposta corretta!")
                punteggio += 1

                if livello == livello_max:
                    break

                livello += 1

            else:
                indice = risposte.index(domanda.corretta)+1
                print(f"Risposta sbagliata! La risposta corretta era: {indice}")
                break

        return punteggio