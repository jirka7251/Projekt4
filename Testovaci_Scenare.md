# Testovací scénáře pro projekt Task Manager v00

Tento dokument obsahuje detailní popis testovacích případů (TC) pro ověření funkčnosti aplikace.

---

## Přehled testovacích scénářů

| ID | Název testu | Popis | Vstupní podmínky | Kroky testu | Očekávaný výsledek | Skutečný výsledek | Stav |
|:---|:---|:---|:---|:---|:---|:---|:---|
| **TC01** | Inicializace menu | Ověření zobrazení hlavního menu | Program je spuštěn. | 1. Spustit program. <br> 2. Ověřit výpis v konzoli. | Zobrazí se možnosti 1-4. | Menu se zobrazilo správně. | **Pass** |
| **TC02** | Přidání úkolu | Pozitivní test uložení dat | Hlavní menu je zobrazeno. | 1. Zadat volbu 1. <br> 2. Zadat název a popis. | Potvrzení o uložení úkolu. | Úkol byl uložen a potvrzen. | **Pass** |
| **TC03** | Prázdný vstup | Negativní test validace | Funkce `pridat_ukol` běží. | 1. Ponechat pole prázdná. <br> 2. Stisknout Enter. | Chybová hláška a opakování výzvy. | Program vyžádal data znovu. | **Pass** |
| **TC04** | Odstranění úkolu | Hraniční případ (poslední prvek) | Seznam obsahuje 1 úkol. | 1. Zadat volbu 3. <br> 2. Zadat číslo 1. | Úkol je smazán, potvrzení v konzoli. | Úkol smazán bez chyb. | **Pass** |
| **TC05** | Neexistující ID | Negativní test odstranění | Funkce `odstranit_ukol` běží. | 1. Zadat neexistující ID (99). | Upozornění na neplatné ID. | Program chybu ošetřil. | **Pass** |

---

## Poznámky k testování
- Testy byly prováděny manuálně v terminálu.
- Aplikace vykazuje stabilitu i při zadávání nečíselných znaků do polí vyžadujících ID.