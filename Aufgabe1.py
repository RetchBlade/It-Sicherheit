# Aufgabe 1:
# Schreiben Sie ein Programm, das eine Textdatei einliest und eine Analyse der Buchstabenhaeufigkeit durchfuehrt.
# Berechnen Sie die Haeufigkeiten der Buchstaben im Text und stellen Sie die Ergebnisse grafisch dar.
# Versuchen Sie anschliessend, den Text mithilfe von Letter Frequency Analysis zu entschluesseln und den Klartext auszugeben.
# Verwenden Sie hierfuer die Datei Aufgabe1.txt. Hinweis: Der Text ist in der Sprache Deutsch.

# Das ganze wurde in Pycharm erstellt, Aufgabe1.txt muss sich im selben Verzeichnis befinden.
# Am sonsten muss man den ganzen Pfad zur Datei im String rein schreiben
# Aufgabe Erledigt von Lorenz Berkmans

import matplotlib.pyplot as plt # Um den Plot, also Grafische Anzeige realisierbar zu machen

def dateiLesen(datei): #liest die datei ein und wirft diese zurueck
    with open('Aufgabe1.txt', encoding='utf-8') as file: # öffne Datei
        text = file.read() # lese datei und speichere Sie in text.
    return text # gib text zurueck

def zaehler(verschluesselterText): # Die Buchstaben mit hilfe eines dict druch den Text gehen und dem dict addieren
    buchstabenHaeufigkeit = {"a": 0, "b": 0, "c": 0, "d": 0, "e": 0, "f": 0, "g": 0, "h": 0,
                             "i": 0, "j": 0, "k": 0, "l": 0, "m": 0, "n": 0, "o": 0, "p": 0,
                             "q": 0, "r": 0, "s": 0, "t": 0, "u": 0, "v": 0, "w": 0, "x": 0,
                             "y": 0, "z": 0}

    for buchstabe in verschluesselterText.lower(): # in lower, weil der dict in kleinbuchstaben steht.
        if buchstabe in buchstabenHaeufigkeit: # Wenn der aktuelle buchstabe in dem dict. ist
            buchstabenHaeufigkeit[buchstabe] += 1 # Addiere +1 zum value


    for buchstabe in buchstabenHaeufigkeit: # Berechne die Häufigkeiten
        buchstabenHaeufigkeit[buchstabe] = buchstabenHaeufigkeit[buchstabe] / len(buchstabenHaeufigkeit) # Berechne die relative Haeufigkeit jedes Buchstabens


    return buchstabenHaeufigkeit # Dict. zurueckgeben

def plot_buchstaben_haeufigkeit(buchstabenHaeufigkeit): #Grafische darstellung
    # Sortiert das dict @buchstabenHaeufigkeit nach den values innerhalb und lässt sie rückwärts druch @revers : True zurueckgeben
    sortiertet_buchstabenHaeufigkeit = dict(sorted(buchstabenHaeufigkeit.items(), key=lambda x: x[1], reverse=True))
    # x fuer die Buchstaben und y fuer die Haeufigkeit
    plt.bar(list(sortiertet_buchstabenHaeufigkeit.keys()), list(sortiertet_buchstabenHaeufigkeit.values()))
    plt.xlabel('Buchstabe') # x-achse beschriften
    plt.ylabel('Haeufigkeit') # y-achse beschriften
    plt.title('Buchstabenhaeufigkeit im Text') # Allgemeiner Title fuer den Plot
    plt.show() # anzeigen lassen

def substitutionen(verschluesselterText, buchstabenHaeufigkeit): # Entschluesslung Vorgang

    # nochmal Sortierte buchstabenhaeufigkeit, da es sonst einen KeyError: 0 erzeugt
    sortierte_buchstabenHaeufigkeit = sorted(buchstabenHaeufigkeit.items(), key=lambda x: x[1], reverse=True)

    maxiBuchstabe = sortierte_buchstabenHaeufigkeit[0][0] # Maximaler Wert der auf am anfang gesetzt wurde nehmen

    # Maximal Buchstabe mit relative haeufigsten Buchstaben Subtrahiert um die Verschiebung der Buchstaben zu ermitteln
    verschiebung = (ord(maxiBuchstabe) - ord("e")) # ord() sorgten fuer den passenden Ascii wert zum char

    entschluesselter_text = "" # Leeren String
    for zeichen in verschluesselterText.lower(): # jeder buchstabe aus dem Text wird klein gemacht, um den Dict und den Austausch zu erleichtern
        if zeichen in buchstabenHaeufigkeit: # Sobald ein Buchstabe dem Alphabet aus dem selbst erzeugten Dict angehoert
            # Entschluesselung des aktuellen Buchstabens mittels der verschiebung
            entschluesselter_text += chr((ord(zeichen) - ord('a') - verschiebung) % 26 + ord('a')) # chr() sorgt dafuer, den Char vom ascii-code darzustellen
        else:
            entschluesselter_text += zeichen # aktuelles element hinzufuegen damit sind die ymlauten und Satzzeichen gemeint

    return entschluesselter_text # Gibt den entschluesselten Text zurueck

def main(): # Ausfuehrung aller Methoden
    datei = "Aufgabe1.txt"  #dateipfad festlegen

    verschluesselterText = dateiLesen(datei) # datei lesen

    buchstabenHaeufigkeit = zaehler(verschluesselterText) # Frequenzanalyse durchfuehren

    plot_buchstaben_haeufigkeit(buchstabenHaeufigkeit) # Grafische Darstellung

    entschluesselter_text = substitutionen(verschluesselterText, buchstabenHaeufigkeit)  # VerschluesselterText entschluesseln

    print(entschluesselter_text) # Klartext anzeigen lassen

if __name__ == "__main__": # Mainfunktion ausführen
    main() #aufrufen von main()
