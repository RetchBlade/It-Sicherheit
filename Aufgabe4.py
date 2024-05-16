# Aufgabe 4:
# Gegeben sind zwei Dateien Aufgabe4_1.txt und Aufgabe4_2.txt welche einen HEX-String
# enthalten eines Deutschen in One Time Pad (OTP) verschluesselten Satzes.
# Implementieren Sie ein Programm, das Ihnen dabei hilft die zwei HEX-Strings wieder vollstaendig zu
# entschluesselt und den urspruenglichen Klartext wiederherzustellen.
# Hinweis: Die Klartexte sowie der Schluessel sind gleich lang. Fuer beide Klartexte wurde der
# identische Schluessel verwendet. Die Texte beinhalten Woerter welche sich auch in diesem
# Dokument wiederfinden. Alle Woerter im Klartext wurden in CAPS geschrieben.

def leseDateien(datei_1, datei_2): # lesen der Datei direkt fuer beide Dateien
    with open(datei_1, encoding='utf-8') as file1: # erste datei
        datei1 = file1.read()
    with open(datei_2, encoding='utf-8') as file2: # zweite Datei
        datei2 = file2.read()
    return datei1, datei2 # soll beides zurueckgeben
def konverterToByte(hexText_1, hexText_2): # es soll von hexa zu Byte konveritieren
    bytesText1,bytesText2 = bytes.fromhex(hexText_1), bytes.fromhex(hexText_2) # fromhex dient zu umwandlung
    return bytesText1, bytesText2 #soll beides zurueckgeben

def entschluesseln(bytesText, schuessel):
    if len(bytesText) != len(schuessel): # wenn beide laengen nicht gleich sind
        # Wegen dem Hinweis in der Aufgabe
        print("Info: Key muss gleich lang sein, wie der Text, deswegen wurde es abgebrochen")
        exit()  # bricht an dieser Stelle ab

    entschluesselterText = "" # leerer String um den Klartext da reinzuschreiben
    zaehler = 0 # zaehler fuer den Index des Schluessels

    for bit in bytesText: # geht jeden bit durch
        schluesselzeichen = schuessel[zaehler % len(schuessel)] # ermittelt den schluesselzeichen fuer das aktuelle
        ascii_schluesselzeichen = ord(schluesselzeichen) # umwandlung zu ascii
        ascii_xor =  bit ^ ascii_schluesselzeichen # XOR Anwendung
        entschluesselterZeichen = chr(ascii_xor) # Umwandlung aus dem Ascii zum zeichen
        entschluesselterText += entschluesselterZeichen # addieren des Zeichens
        zaehler += 1 # aufstieg des zaehlers
    return entschluesselterText # gib Klartext zurueck

def main(): # fuhert alle methoden aus
    datei1, datei2 = "Aufgabe4_1.txt", "Aufgabe4_2.txt" # dateipfad anlegen
    hexText1, hexText2 = leseDateien(datei1, datei2) # lesen und speichern von beiden

    print("\nHexa Version:")
    print(hexText1, hexText1) # Hexa Version von beiden ausgeben

    bytesText1, bytesText2 = konverterToByte(hexText1, hexText2) # Die Konvertierung vornehmen
    print("\nString in Bytes Version:")
    print(bytesText1, bytesText2) # Byte darstellung von beiden

    print("\nMit XOR Version: ")
    key = "EinSchluessel" # durch bruteforce ermittelter key
    print("Benutzender Key: ", key)
    klartext1 = entschluesseln(bytesText1, key) # Klartext anzeige fuer die erste txt
    print("\nKlartext von ersten Txt: ", klartext1)
    klartext2 = entschluesseln(bytesText2, key) # Klartext anzeige fuer die zweite txt
    print("Klartext von zweiten Txt: ", klartext2)

if __name__ == "__main__": # ausfuheren der Main funktion
    main()