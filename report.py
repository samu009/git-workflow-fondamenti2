APPARATI = {
    "NAV-01": {"nome": "Ricevitore navigazione", "bus": "BUS-A", "stato": "OK"},
    "COM-02": {"nome": "Radio comunicazioni", "bus": "BUS-B", "stato": "ATTENZIONE"},
    "SEN-03": {"nome": "Sensore assetto", "bus": "BUS-A", "stato": "OFFLINE"},
}

def filtra_per_stato(apparati, stato):
    lista_filtrata_stato = [s for s in apparati.values() if s["stato"] == stato]
    return lista_filtrata_stato

def filtra_per_bus(apparati, bus):
    lista_filtrata_bus = [s for s in apparati.values() if s["bus"] == bus]
    return lista_filtrata_bus