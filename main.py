# Globální seznam pro ukládání úkolů
ukoly = []

def zobrazit_ukoly():
    """Zobrazí všechny uložené úkoly v očíslovaném seznamu."""
    if not ukoly:
        print("\nSeznam úkolů je prázdný.")
    else:
        print("\n--- Aktuální úkoly ---")
        for i, ukol in enumerate(ukoly, 1):
            print(f"{i}. {ukol['nazev']} - {ukol['popis']}")
    print("-" * 22)

def pridat_ukol():
    """Umožní uživateli přidat nový úkol. Kontroluje prázdné vstupy."""
    while True:
        nazev = input("Zadejte název úkolu: ").strip()
        popis = input("Zadejte popis úkolu: ").strip()
        
        if not nazev or not popis:
            print("Chyba: Název i popis úkolu musí být vyplněny!")
            continue
        
        ukoly.append({"nazev": nazev, "popis": popis})
        print(f"Úkol '{nazev}' byl přidán.")
        break

def odstranit_ukol():
    """Zobrazí úkoly a umožní jeden odstranit podle jeho čísla."""
    if not ukoly:
        print("\nSeznam je prázdný, není co odstranit.")
        return

    zobrazit_ukoly()
    while True:
        try:
            volba = int(input("Zadejte číslo úkolu, který chcete odstranit: "))
            if 1 <= volba <= len(ukoly):
                odstraneny = ukoly.pop(volba - 1)
                print(f"Úkol '{odstraneny['nazev']}' byl úspěšně odstraněn.")
                break
            else:
                print(f"Chyba: Úkol s číslem {volba} neexistuje.")
        except ValueError:
            print("Chyba: Zadejte prosím platné číslo (číslici).")

def hlavni_menu():
    """Hlavní ovládací smyčka programu."""
    while True:
        print("\nSprávce úkolů - Hlavní menu")
        print("1. Přidat nový úkol")
        print("2. Zobrazit všechny úkoly")
        print("3. Odstranit úkol")
        print("4. Konec programu")
        
        volba = input("Vyberte možnost (1-4): ").strip()

        if volba == "1":
            pridat_ukol()
        elif volba == "2":
            zobrazit_ukoly()
        elif volba == "3":
            odstranit_ukol()
        elif volba == "4":
            print("Ukončuji program... Na shledanou!")
            break
        else:
            print("Neplatná volba, zadejte prosím číslo od 1 do 4.")

if __name__ == "__main__":
    hlavni_menu()