sarcina 1 
def calculeaza_greutate_ideala():
    try:
        sex = input("Introduceți sexul (M sau F): ").strip().upper()
        if sex not in ['M', 'F']:
            print("Eroare: Sexul trebuie să fie M sau F.")
            return

        inaltime = int(input("Introduceți înălțimea (cm): "))
        if inaltime < 150 or inaltime > 220:
            print("Eroare: Înălțimea trebuie să fie între 150 și 220 cm.")
            return

        varsta = int(input("Introduceți vârsta (ani): "))
        if varsta <= 20 or varsta >= 120:
            print("Eroare: Vârsta trebuie să fie între 21 și 119 ani.")
            return

        greutate_actuala = float(input("Introduceți greutatea actuală (kg): "))
        if greutate_actuala < 45 or greutate_actuala > 300:
            print("Eroare: Greutatea trebuie să fie între 45 kg și 300 kg.")
            return

        # Calcul greutate ideală conform formulei Lorentz
        if sex == 'M':
            greutate_ideala = inaltime - 100 - ((inaltime - 150) / 4 + (varsta - 20) / 4)
        else:  # F
            greutate_ideala = inaltime - 100 - ((inaltime - 150) / 2.5 + (varsta - 20) / 6)

        diferenta = greutate_actuala - greutate_ideala

        print(f"\nGreutatea ideală este: {greutate_ideala:.2f} kg")

        if diferenta > 0:
            print(f"Ai cu {diferenta:.2f} kg peste greutatea ideală. Se recomandă slăbitul.")
        else:
            print(f"Ai cu {-diferenta:.2f} kg sub greutatea ideală. Se recomandă să adaugi în greutate.")

    except ValueError:
        print("Eroare: Ați introdus un tip de date invalid.")

# Apelul funcției pentru a rula când fișierul este executat direct
if __name__ == "__main__":
    calculeaza_greutate_ideala()
