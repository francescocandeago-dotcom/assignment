#creazione file json
import json
import os
from datetime import datetime

#dizionari
alunni = {}
compiti = {}

#percorso del file
percorso_file = "dati.json"

#orario
def orario():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

#validazione matricola
def matricola_univoca(matricola):
    #controlla se la matricola è già nel dizionario
    return matricola not in alunni

#validazione email
def email_valida(email):
    if "@" in email and "." in email:
        return True
    else:
        return False

#id per compiti
def genera_id_compito():
    return str(len(compiti) + 1)

#salvataggio dati
def salva_dati():
    print(
    "╔═══════════════════════════════════════════════════════════════╗\n"
    "║                      SALVATAGGIO DATI                         ║\n"
    "╚═══════════════════════════════════════════════════════════════╝\n"
    )
    #creazione dizionario che contiene le variabili
    data = {"alunni": alunni, "compiti": compiti}
    #apertura file in modalità scrittura
    with open(percorso_file, "w") as file:
        json.dump(data, file, indent=4)
    print("✅ Dati salvati correttamente")

#salvataggio dati nel file
def carica_dati():
    print(
    "╔═══════════════════════════════════════════════════════════════╗\n"
    "║                          CARICA DATI                          ║\n"
    "╚═══════════════════════════════════════════════════════════════╝\n"
    )
    #variabili globali
    global alunni, compiti
    if not os.path.exists(percorso_file):
        print("❌ Nessun file trovato")
        return
    with open(percorso_file, "r") as file:
        data = json.load(file)
        alunni = data.get("alunni", {})
        compiti = data.get("compiti", {})
    print("✅ File caricati correttamente")

##salvataggio dati alunno
def inserisci_alunno():
    print(
    "╔═══════════════════════════════════════════════════════════════╗\n"
    "║                    INSERISCI NUOVO ALUNNO                     ║\n"
    "╚═══════════════════════════════════════════════════════════════╝\n"
    )
    matricola = input("Inserisci la matricola: ").strip()
    #controlla se la matricola esiste
    if not matricola_univoca(matricola):
        print("❌ Matricola già presente")
        return

    #raccolta nuovi dati
    nome = input("Nome: ")
    cognome = input("Cognome: ")
    email = input("Email: ").strip()

    #validazione email
    if not email_valida(email):
        print("❌ Email non valida")
        return

    #inserimento nuovi dati nel dizionario alunni
    alunni[matricola] = {
        "nome": nome,
        "cognome": cognome,
        "email": email,
        "data_inserimento": orario(),
        "data_modifica": orario()
    }
    print("✅ Alunno inserito con successo")

#elenco alunni registrati
def visualizza_alunni():
    print(
    "╔═══════════════════════════════════════════════════════════════╗\n"
    "║                  VISUALIZZA ALUNNI REGISTRATI                 ║\n"
    "╚═══════════════════════════════════════════════════════════════╝\n"
    )
    #controlla se il dizionario alunni è vuoto
    if not alunni:
        print("❌ Nessun alunno registrato")
        return

    print(" Alunni registrati:")
    #stampa i dati dell'alunno
    for matricola, dati in alunni.items(): #alunni.items() restituisce tutte le coppie del dizionario
        print(f" - {matricola}: {dati['nome']} {dati['cognome']} ({dati['email']})")

#modifica dati alunno
def modifica_alunno():
    print(
    "╔═══════════════════════════════════════════════════════════════╗\n"
    "║                    MODIFICA DATI ALUNNO                       ║\n"
    "╚═══════════════════════════════════════════════════════════════╝\n"
    )
    #matricola da modificare
    matricola = input("Matricola da modificare: ").strip()
    #controlla se la matricola esiste
    if matricola not in alunni:
        print("❌ Matricola non trovata")
        return

    nome = input("Nuovo nome (invio per saltare): ")
    cognome = input("Nuovo cognome (invio per saltare): ")
    email = input("Nuova email (invio per saltare): ").strip()

    #validazione email
    if email:
        if not email_valida(email):
            print("❌ Email non valida")
            return
        alunni[matricola]["email"] = email

    #aggiorna i dati
    if nome:
        alunni[matricola]["nome"] = nome
    if cognome:
        alunni[matricola]["cognome"] = cognome
    if email:
        alunni[matricola]["email"] = email

    #modifica orario
    alunni[matricola]["data_modifica"] = orario()
    print("✅ Modifica completata")

#eliminare alunno
def elimina_alunno():
    print(
    "╔═══════════════════════════════════════════════════════════════╗\n"
    "║                        ELIMINA ALUNNO                         ║\n"
    "╚═══════════════════════════════════════════════════════════════╝\n"
    )
    matricola = input("Matricola da eliminare: ").strip()
    #controlla se la matricola esiste
    if matricola not in alunni:
        print("❌ Matricola inesistente")
        return
    #eliminazione dell'alunno
    del alunni[matricola]
    print(" Alunno eliminato")

#assegnazione compito ad alunno
def assegna_compito():
    print(
    "╔═══════════════════════════════════════════════════════════════╗\n"
    "║                    ASSEGNA COMPITO A STUDENTE                 ║\n"
    "╚═══════════════════════════════════════════════════════════════╝\n"
    )
    matricola = input("Matricola studente: ").strip()
    if matricola not in alunni:
        print("❌ Studente non trovato")
        return

    descrizione = input("Descrizione compito: ")
    #generazione ID del compito
    id_compito = genera_id_compito()

    compiti[id_compito] = {
        "descrizione": descrizione,
        "matricola": matricola,
        "stato": "assegnato",
        "data_assegnazione": orario(),
        "voto": None #None stà per non ancora valutato
    }

    print(f"📌 Compito assegnato! ID: {id_compito}")

#inserire un voto
def registra_valutazione():
    print(
    "╔═══════════════════════════════════════════════════════════════╗\n"
    "║                    REGISTRA VALUTAZIONE                       ║\n"
    "╚═══════════════════════════════════════════════════════════════╝\n"
    )
    #richiede l'ID del compito
    id_compito = input("ID compito: ").strip()
    if id_compito not in compiti:
        print("❌ Compito non trovato")
        return

    voto = int(input("Voto (0-10): "))
    #registra il voto nel dizionario
    compiti[id_compito]["voto"] = voto
    #aggiorna lo stato del compito
    compiti[id_compito]["stato"] = "registrato"
    print("✅ Valutazione registrata")

#visualizzazione compiti di uno studente
def visualizza_compiti_studente():
    print(
    "╔═══════════════════════════════════════════════════════════════╗\n"
    "║               VISUALIZZA COMPITI DI UNO STUDENTE              ║\n"
    "╚═══════════════════════════════════════════════════════════════╝\n"
    )
    matricola = input("Matricola studente: ").strip()
    print(" Compiti dello studente:")

    for cid, dati in compiti.items(): #cid è l'ID del compito
        #controlla se il compito appartiene allo studente inserito, se si lo stampa
        if dati["matricola"] == matricola:
            print(f" - ID {cid}: {dati['descrizione']} | Stato: {dati['stato']} | Voto: {dati['voto']}")

#statistiche
def statistiche_studente():
    print(
    "╔═══════════════════════════════════════════════════════════════╗\n"
    "║                  VISUALIZZA STATISTICHE ALUNNO                ║\n"
    "╚═══════════════════════════════════════════════════════════════╝\n"
    )
    matricola = input("Matricola: ").strip()

    voti = []
    assegnati = 0
    completati = 0

    for compito in compiti.values():
        #controlla se il compito è dello studente
        if compito["matricola"] == matricola:
            assegnati += 1
            #se il compito ha un voto
            if compito["voto"] is not None:
                voti.append(compito["voto"])
                completati += 1

    #se non ha compiti
    if assegnati == 0:
        print("❌ Nessun compito assegnato")
        return

    print(" Statistiche studente")

    #statistiche sui voti
    if voti:
        media = sum(voti) / len(voti)
        print("Media voti:", round(media, 2))
        print("Voto massimo:", max(voti))
        print("Voto minimo:", min(voti))
    else:
        print("Nessuna valutazione registrata")

    print("Compiti assegnati:", assegnati)
    print("Compiti completati:", completati)

#ranking studenti
def ranking_studenti():
    print(
    "╔═══════════════════════════════════════════════════════════════╗\n"
    "║                 RANKING ALUNNI PER MEDIA VOTI                 ║\n"
    "╚═══════════════════════════════════════════════════════════════╝\n"
    )
    ranking = {}

    for matricola in alunni:
        somma = 0
        count = 0
        for compito in compiti.values():
            #controllo se il compito è dello studente
            if compito["matricola"] == matricola and compito["voto"] is not None:
                somma += compito["voto"]
                count += 1
        #se lo studente ha altri voti
        if count > 0:
            ranking[matricola] = somma / count

    print(" Ranking studenti:")
    #classifica dal meglio al peggio
    for matricola, media in sorted(ranking.items(), key=lambda x: x[1], reverse=True):
        nome = alunni[matricola]["nome"]
        cognome = alunni[matricola]["cognome"]
        print(f" - {nome} {cognome}: media {media:.2f}")

#compiti non completati
def report_compiti_non_completati():
    print(
    "╔═══════════════════════════════════════════════════════════════╗\n"
    "║                REPORT COMPITI NON COMPLETATI                  ║\n"
    "╚═══════════════════════════════════════════════════════════════╝\n"
    )
    print("❌ Compiti non completati:")
    for cid, compito in compiti.items():
        if compito["stato"] != "registrato":
            print(f" - ID {cid}: {compito['descrizione']} (studente {compito['matricola']})")

#cercare alunni per nome,cognome e matricola
def ricerca_alunno():
    print(
    "╔═══════════════════════════════════════════════════════════════╗\n"
    "║                        RICERCA ALUNNO                         ║\n"
    "╚═══════════════════════════════════════════════════════════════╝\n"
    )

    chiave = input("Inserisci matricola, nome o cognome: ").strip().lower()
    trovato = False

    if not alunni:
        print("❌ Nessun alunno presente nel sistema")
        return

    print("Risultati ricerca:")

    #ricerca i dati prima inseriti nel dizionario
    for matricola, dati in alunni.items():
        nome = dati.get("nome", "").lower()
        cognome = dati.get("cognome", "").lower()
        matricola_lower = matricola.lower()

        #se li trova li stampa
        if chiave == matricola_lower or chiave == nome or chiave == cognome:
            print(f" - {matricola}: {dati.get('nome', '')} {dati.get('cognome', '')} ({dati.get('email', '')})")
            trovato = True

    if not trovato:
        print("❌ Nessun alunno trovato")

#visualizza gli alunni per i loro voti
def filtra_alunni_per_voto():
    print(
    "╔═══════════════════════════════════════════════════════════════╗\n"
    "║                   VISUALIZZA ALUNNI PER VOTO                  ║\n"
    "╚═══════════════════════════════════════════════════════════════╝\n"
    )
    
    try:
        voto_min = float(input("Voto minimo: "))
        voto_max = float(input("Voto massimo: "))
    except ValueError:
        print("❌ Inserire numeri validi")
        return

    print(f"\n📊 Alunni con media voti tra {voto_min} e {voto_max}:")

    trovato = False
    for matricola, dati in alunni.items():

        # calcola media voti
        voti = [c["voto"] for c in compiti.values()
                if c["matricola"] == matricola and c["voto"] is not None]

        #se non ci sono voti
        if not voti:
            continue  

        media = sum(voti) / len(voti)
        if voto_min <= media <= voto_max:
            print(f" - {matricola}: {dati['nome']} {dati['cognome']} | Media: {media:.2f}")
            trovato = True

    if not trovato:
        print("❌ Nessun alunno trovato in questo range")

#menu
def stampa_menu():
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
    "║   o) Ricerca alunno                                           ║\n"
    "║   p) Filtra alunni per range di voti                          ║\n"
    "╚═══════════════════════════════════════════════════════════════╝\n"
    )

def main():
    stampa_menu()
    while True:
        scelta = input("Seleziona opzione: ").lower()
        if scelta == "a": inserisci_alunno()
        elif scelta == "b": visualizza_alunni()
        elif scelta == "c": modifica_alunno()
        elif scelta == "d": elimina_alunno()
        elif scelta == "e": assegna_compito()
        elif scelta == "f": registra_valutazione()
        elif scelta == "g": visualizza_compiti_studente()
        elif scelta == "h": statistiche_studente()
        elif scelta == "i": ranking_studenti()
        elif scelta == "j": report_compiti_non_completati()
        elif scelta == "k": salva_dati()
        elif scelta == "l": carica_dati()
        elif scelta == "m": stampa_menu()
        elif scelta == "o": ricerca_alunno()
        elif scelta == "p": filtra_alunni_per_voto()
        #esce dal programma
        elif scelta == "n":
            print(
    "╔═══════════════════════════════════════════════════════════════╗\n"
    "║                    USCITA DAL PROGRAMMA                       ║\n"
    "╚═══════════════════════════════════════════════════════════════╝\n"
            )
            break
        else:
            print("❌ Opzione non valida")

if __name__ == "__main__":
    main()
