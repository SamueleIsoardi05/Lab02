def carica_da_file(file_path):
    """Carica le foto dal file, creando un nuovo anno ogni volta che compare per la prima volta"""
    # TODO
    try:
        with open(file_path, 'r', encoding='utf-8') as csvfile:
            album = []
            csvfile.readline()
            for row in csvfile:
                campi = row.rstrip("\n").split(',')
                foto = {
                    "codice": campi[0],
                    "titolo": campi[1],
                    "autore": campi[2],
                    "mese": int(campi[3]),
                    "anno": int(campi[4]),
                }
                #crea un dizionario per ogi singola foto del file csv



                for elemento in album:
                    if elemento[0] == foto["anno"]:
                        elemento[1].append(foto)
                        break
                else:
                    album.append([foto["anno"], [foto]])
                #crea una lista di liste di dizionari, dove la chiave è l'anno, seguito poi da tutte le altre informazioni delle foto



            return album
    except FileNotFoundError:
        print("Errore nel caricamento del file.")
        return None


def aggiungi_foto(album, codice, titolo, autore, mese, anno, file_path):
    """Aggiunge una foto all'album, creando l'anno al volo se non è ancora presente"""
    # TODO
    foto={"codice": codice,
          "titolo": titolo,
          "autore": autore,
          "mese": mese,
          "anno": anno,
          }

    for f in album:
        if f[0] == anno:
            f[1].append(foto)
            break
    else:
        album.append([anno,[foto]])

        #è uguale alla funzione precedente ma le informazioni sulle foto sono scritte dall'utente
    return foto


def cerca_foto(album, codice):
    """Cerca una foto nell'album dato il codice"""
    # TODO
    for j in album:#sfoglia per anno
        lista_foto=j[1]
        for foto in lista_foto:#sfoglia per codice
            if foto["codice"] == codice:
                return f"{foto['codice']}, {foto['titolo']}, {foto['autore']}, {foto['mese']}, {foto['anno']}"


def elenco_foto_anno_per_titolo(album, anno):
    """Ordina i titoli delle foto di un dato anno in ordine alfabetico"""
    # TODO
    for j in album:#sfoglia per anno
        if j[0] == anno:
            lista_foto=j[1]
            foto_per_anno = sorted(lista_foto, key=lambda x: x["titolo"])#ordina le foto di quell'anno in ordine alfabetico
            return [foto["titolo"] for foto in foto_per_anno]


def main():
    album = []
    file_path = "album_fotografico.csv"

    while True:
        print("\n--- MENU ALBUM FOTOGRAFICO ---")
        print("1. Carica album da file")
        print("2. Aggiungi una nuova foto")
        print("3. Cerca una foto per codice")
        print("4. Elenco foto di un anno (ordinato per titolo)")
        print("5. Esci")

        scelta = input("Scegli un'opzione >> ").strip()

        if scelta == "1":
            while True:
                file_path = input("Inserisci il path del file da caricare: ").strip()
                album = carica_da_file(file_path)
                if album is not None:
                    break

        elif scelta == "2":
            if not album:
                print("Prima carica l'album da file.")
                continue

            codice = input("Codice della foto: ").strip()
            titolo = input("Titolo: ").strip()
            autore = input("Autore: ").strip()
            try:
                mese = int(input("Mese (1-12): ").strip())
                anno = int(input("Anno: ").strip())
            except ValueError:
                print("Errore: inserire valori numerici validi per mese e anno.")
                continue

            foto = aggiungi_foto(album, codice, titolo, autore, mese, anno, file_path)
            if foto:
                print(f"Foto aggiunta con successo!")
            else:
                print("Non è stato possibile aggiungere la foto.")

        elif scelta == "3":
            if not album:
                print("L'album è vuoto.")
                continue

            codice = input("Inserisci il codice della foto da cercare: ").strip()
            risultato = cerca_foto(album, codice)
            if risultato:
                print(f"Foto trovata: {risultato}")
            else:
                print("Foto non trovata.")

        elif scelta == "4":
            if not album:
                print("L'album è vuoto.")
                continue

            try:
                anno = int(input("Inserisci l'anno da consultare: ").strip())
            except ValueError:
                print("Errore: inserire un valore numerico valido.")
                continue

            titoli = elenco_foto_anno_per_titolo(album, anno)
            if titoli is not None:
                print(f'\nFoto del {anno}:')
                print("\n".join([f"- {titolo}" for titolo in titoli]))
            else:
                print(f"Nessuna foto trovata per l'anno {anno}.")

        elif scelta == "5":
            print("Uscita dal programma...")
            break
        else:
            print("Opzione non valida. Riprova.")

if __name__ == "__main__":
    main()
