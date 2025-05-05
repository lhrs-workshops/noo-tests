# Testni repozitorij za GitHub Classroom

Ta repozitorij vsebuje **skrite testne skripte**, ki se uporabljajo za **samodejno ocenjevanje** v okviru nalog GitHub Classroom.

Testi so namenjeni uporabi z GitHub Actions, kjer se ob oddaji študentskih rešitev:
- koda prenese,
- testi zaženejo,
- rezultati zapišejo v `grade_summary.json` — vse to **brez razkritja testne logike študentom**.

---

## Struktura repozitorija
- README.md # Navodila
- classroom.yml # Workflow za zagon tests (ne pozabiti spremeniti link v delu testa _Prenesi skrite teste_
- test_template.py # Testi za template projekt
- test_*.py # druge testne datoteke

Vsaka testna datoteka (`test_*.py`) vključuje:
- Teste pravilnosti funkcij
- Preverjanje teoretičnih odgovorov (prek zgoščene vrednosti - hash)
- Točkovanje in izpis rezultatov v `grade_summary.json`

---

## Uporaba v GitHub Classroom (avtomatsko ocenjevanje)

1. V `workflow.yml` datoteki v študentski repozitorij dodaj:

   ```yaml
   - name: Prenesi teste
     run: |
       curl -o tests.py https://raw.githubusercontent.com/IME-UPORABNISKEGA-RACUNA/IME-TEGA-REPOZITORIJA/main/test_projekt1.py

   - name: Zazeni vse teste
     run: pytest tests.py --disable-warnings -v
     continue-on-error: true
   - name: Naloži rezultate
     uses: actions/upload-artifact@v4
     with:
       name: grade-summary
       path: grade_summary.json

  2. Dodajanje novih testnih datotek
   - ```cp test_template.py test_projekt2.py``` (podaj smiselno ime)
   - Preveri import (npr. from student_code import ...)
   - Prilagodi funkcije in pričakovane vrednosti
   - Po potrebi posodobi hash za teoretična vprašanja
   - Posodobi ključe v slovarju results

  3. Izhod testa bo json datoteka in bo prikazana pri uporabniku kot artifact pri oddani nalogi

---

## Opozorilo!!!
Ta repozitorij je trenutno javen, da se olajša dostop do testov. V datoteke ne dodajati kakšnih kritičnih podatkov, kot so tokeni ali podobno!!!


