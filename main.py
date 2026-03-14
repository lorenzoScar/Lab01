from game import Game

gioco = Game()

gioco.carica_domande("domande.txt")

punteggio = gioco.gioca()

print(f"\nHai totalizzato {punteggio} punti!")

nickname = input("Inserisci il tuo nickname ")

gioco.aggiorna_punteggio("punti.txt", nickname, punteggio)