APPARATI = {
    "NAV-01": {"nome": "Ricevitore navigazione", "bus": "BUS-A", "stato": "OK"},
    "COM-02": {"nome": "Radio comunicazioni", "bus": "BUS-B", "stato": "ATTENZIONE"},
    "SEN-03": {"nome": "Sensore assetto", "bus": "BUS-A", "stato": "OFFLINE"},
}


def aggiungi_apparato(id, nome, bus, stato):
    if id in APPARATI:
        print(f"Errore: L'apparato con ID '{id}' esiste già.")
        return
    else if stato not in ["OK", "ATTENZIONE", "OFFLINE"]:
        print(f"Errore: Stato '{stato}' non valido. Deve essere 'OK', 'ATTENZIONE' o 'OFFLINE'.")
        return
    else:
        APPARATI[id] = {"nome": nome, "bus": bus, "stato": stato};


def aggiorna_stato(id, nuovo_stato):
    if id not in APPARATI:
        print(f"Errore: L'apparato con ID '{id}' non esiste.")
        return
    else if nuovo_stato not in ["OK", "ATTENZIONE", "OFFLINE"]:
        print(f"Errore: Stato '{nuovo_stato}' non valido. Deve essere 'OK', 'ATTENZIONE' o 'OFFLINE'.")
        return
    else:
        APPARATI[id]["stato"] = nuovo_stato;




