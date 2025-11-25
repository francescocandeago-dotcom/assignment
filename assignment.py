#creazione file json
import json
import os

file = "dati.json"

print(
"╔═══════════════════════════════════════════════════════════════╗\n"
"║          SISTEMA DI TRACCIAMENTO ALUNNI - ITS                 ║\n"
"╚═══════════════════════════════════════════════════════════════╝\n"

"╔═══════════════════════════════════════════════════════════════╗\n"
"║   Seleziona un'opzione:                                       ║\n"
"║   a) Inserisci nuovo alunno                                   ║\n"
"║   b) Visualizza alunni registrati                             ║\n"  
"║   c) Modifica dati alunno                                     ║\n"
"║   d) Elimina alunno                                           ║\n"
"║   e) Assegna compito a studente                               ║\n"
"║   f) Registra valutazione                                     ║\n"
"║   g) Visualizza compiti di uno studente                       ║\n"
"║   h) Visualizza statistiche alunno                            ║\n"
"║   i) Ranking alunni per media voti                            ║\n"
"║   j) Report compiti non completati                            ║\n"
"║   k) Salva dati (backup)                                      ║\n"
"║   l) Carica dati                                              ║\n"
"║   m) Visualizza menu                                          ║\n"
"║   n) Esci                                                     ║\n"
"╚═══════════════════════════════════════════════════════════════╝\n"
)

#comando a
comando = input("inserisci l'opzione che vuoi:")

if comando == "a" or comando == "A":
    nome = input("inserisci un nome:")
    cognome = input("inserisci un cognome:")
    email = input("inserisci un Email:")
    import random
    import string
    import datetime
    #orario
    from datetime import datetime
    ora_attuale = datetime.now()
    print(ora_attuale)
    #matricola
    def genera_matricola(numero):
        return f"MAT{numero:05d}"
    print(genera_matricola(1))
    print(f"✅ Alunno {nome} {cognome} con email:{email} inserito con successo!")
    #inserimento dati nel file
    import json
    import os
    if os.path.exists(file):
        with open(file, "r") as file:
            dati = json.load
    else:
        dati = []
    dati = {
        "nome": nome,
        "cognome" : cognome,
        "email" : email
    }
    try:
        with open("dati.json", "w") as file:
            print(f"✅ dati salvati con successo!")
    except("error")as e:
        print(f"❌ errore")

#comando b
    if comando == "b" or comando == "B":
        with open("dati.json", "r") as file:
            def contenuto():
                nome = file.read()
                cognome = file.read()
                email = file.read()
        print(f"{contenuto}")

#comando c
elif comando == "c" or "C":

    pass