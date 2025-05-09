def calculeaza_varsta_pisicii():
    raspuns = input("Pisica este mai mică de 1 an? (Da/Nu): ").strip().lower()

    if raspuns in ['da', 'yes']:
        conversie = {
            1: "6 luni", 2: "10 luni", 3: "2 ani", 4: "5 ani", 5: "8 ani",
            6: "14 ani", 7: "15 ani", 8: "16 ani", 9: "16 ani",
            10: "17 ani", 11: "17 ani"
        }
        while True:
            try:
                luni = int(input("Câte luni are pisicul? (1-11): "))
                if 1 <= luni <= 11:
                    print(f"Vârsta în ani omenești: {conversie[luni]}")
                    break
                else:
                    print("Introduceți o valoare între 1 și 11.")
            except ValueError:
                print("Introduceți un număr valid.")
    elif raspuns in ['nu', 'no']:
        while True:
            try:
                ani = int(input("Câți ani are pisica? (1-35): "))
                if 1 <= ani < 35:
                    if ani == 1:
                        echivalent = 18
                    elif ani == 2:
                        echivalent = 25
                    elif 3 <= ani <= 15:
                        echivalent = 25 + (ani - 2) * 4
                    else:  # 16+
                        echivalent = 25 + (13 * 4) + (ani - 15) * 3
                    print(f"Pisica are echivalentul a {echivalent} ani omenești.")
                    break
                else:
                    print("Introduceți un număr între 1 și 34.")
            except ValueError:
                print("Introduceți un număr valid.")
    else:
        print("Răspuns invalid. Scrieți Da/Nu sau Yes/No.")

calculeaza_varsta_pisicii()