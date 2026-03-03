# Algorithmic-Credit-Card-Validator

Un script Python simplu, robust și eficient pentru validarea numerelor de carduri de credit. Acest proiect implementează **Algoritmul Luhn** (cunoscut și sub denumirea de algoritmul *Modulus 10*), o formulă de sumă de control utilizată la nivel global pentru a valida o varietate de numere de identificare, în special numerele cardurilor bancare, pentru a preveni erorile accidentale de tastare.

## 🚀 Caracteristici

* **Procesare Flexibilă a Inputului:** Funcția `verify_card_number` filtrează automat caracterele non-numerice. Indiferent dacă numărul cardului este introdus legat (`4111111111111111`), separat prin spații (`1234 5678 9012 3456`) sau delimitat de cratime (`4111-1111-1111-1111`), scriptul va extrage și procesa corect doar cifrele.
* **Zero Dependențe:** Codul este scris exclusiv folosind elemente *built-in* din Python. Nu necesită instalarea unor pachete sau biblioteci externe.
* **Evaluare Rapidă:** Utilizează operații matematice de bază și structuri de date native pentru a returna instant un verdict clar (`VALID!` sau `INVALID!`).

## 🧠 Cum funcționează Algoritmul Luhn în acest script?

Pentru a stabili dacă un număr este valid, scriptul urmează acești pași logici direct pe lista de cifre extrase:
1. Parcurge lista de cifre de la dreapta la stânga.
2. Dublează valoarea fiecărei a doua cifre, începând cu penultima.
3. Dacă rezultatul dublării depășește valoarea de 9, scade 9 din rezultat (acest lucru este echivalent matematic cu adunarea cifrelor produsului, de ex: `7 * 2 = 14`, iar `14 - 9 = 5`).
4. Adună toate cifrele (atât cele dublate/ajustate, cât și cele rămase intacte).
5. Dacă suma totală este perfect divizibilă cu 10 (adică `suma % 10 == 0`), atunci numărul cardului este **VALID!**.

## 🛠️ Cerințe și Rulare

Acest proiect necesită doar **Python 3.x** instalat pe sistemul tău.

1. Clonează acest repository sau descarcă fișierul `credit_card_validator.py`.
2. Deschide un terminal sau un command prompt.
3. Navighează în folderul unde se află fișierul și rulează comanda:

```bash
python credit_card_validator.py
```

## 💻 Exemplu de Cod și Utilizare

Poți folosi acest script fie prin rularea lui directă, fie importând funcția în propriul tău proiect:

```python
# Exemplu de apelare a funcției

print(verify_card_number("453914889"))             # Cifră de test aleatorie
print(verify_card_number("4111-1111-1111-1111"))   # Format cu cratime
print(verify_card_number("1234 5678 9012 3456"))   # Format cu spații
```

**Output așteptat:**
```text
INVALID!
VALID!
INVALID!
```

## 🤝 Contribuții

Contribuțiile sunt binevenite! Dacă ai idei pentru a extinde acest script (de exemplu, adăugarea suportului pentru identificarea emitentului cardului – Visa, Mastercard, American Express etc.), simte-te liber să faci un *fork* al acestui repository și să deschizi un *Pull Request*.
