from typing import List, Dict, Optional

# --- KONSTANTY ---
SEPARATOR: str = "-" * 30
MENU_TEXT: str = """
SPRÁVCE ÚKOLŮ - HLAVNÍ MENU
1. Přidat nový úkol
2. Zobrazit všechny úkoly
3. Odstranit úkol
4. Konec programu
"""

# Globální úložiště úkolů
ukoly: List[Dict[str, str]] = []

def validovat_index(vstup_str: str) -> Optional[int]:
    """
    Ověří, zda je uživatelský vstup platným číslem úkolu.
    Vrací index (od 0) nebo None v případě neplatnosti.
    """
    try:
        index = int(vstup_str)
        if 1 <= index <= len(ukoly):
            return index - 1
        return None
    except ValueError:
        return None

def zobrazit_ukoly() -> None:
    """Zobrazí přehled všech uložených úkolů."""
    if not ukoly:
        print("\nOznámení: Seznam úkolů je aktuálně prázdný.")
    else:
        print("\n--- SEZNAM AKTUÁLNÍCH ÚKOLŮ ---")
        for i, ukol in enumerate(ukoly, 1):
            print(f"{i}. {ukol['nazev']} | Popis: {ukol['popis']}")
    print(SEPARATOR)

def pridat_ukol() -> None:
    """Umožní uživateli vytvořit nový úkol s validací vstupů."""
    while True:
        nazev = input("Zadejte název úkolu: ").strip()
        popis = input("Zadejte popis úkolu: ").strip()
        
        if not nazev or not popis:
            print("Upozornění: Název i popis úkolu jsou povinná pole. Zadejte je prosím znovu.")
            continue
        
        ukoly.append({"nazev": nazev, "popis": popis})
        print(f"Potvrzení: Úkol '{nazev}' byl úspěšně zařazen do seznamu.")
        break

def odstranit_ukol() -> None:
    """Odstraní zvolený úkol na základě pořadového čísla."""
    if not ukoly:
        print("\nInformace: Seznam je prázdný, neexistují žádné úkoly k odstranění.")
        return

    zobrazit_ukoly()
    while True:
        vstup = input("Zadejte číslo úkolu pro trvalé odstranění: ")
        index = validovat_index(vstup)
        
        if index is not None:
            odstraneny = ukoly.pop(index)
            print(f"Potvrzení: Úkol '{odstraneny['nazev']}' byl úspěšně odstraněn.")
            break
        else:
            print("Chyba: Zadané číslo neodpovídá žádnému úkolu v seznamu. Zkuste to znovu.")

def hlavni_menu() -> None:
    """Hlavní řídicí logika programu."""
    while True:
        print(MENU_TEXT)
        volba = input("Zvolte akci (1-4): ").strip()

        if volba == "1":
            pridat_ukol()
        elif volba == "2":
            zobrazit_ukoly()
        elif volba == "3":
            odstranit_ukol()
        elif volba == "4":
            print("Ukončuji aplikaci... Program byl korektně ukončen.")
            break
        else:
            print("Neplatná volba. Zadejte prosím číselnou hodnotu v rozsahu 1 až 4.")

if __name__ == "__main__":
    hlavni_menu()