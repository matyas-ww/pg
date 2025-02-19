def je_tah_mozny(figurka, cilova_pozice, obsazene_pozice):
    
    typ = figurka["typ"]
    start = figurka["pozice"]

    if not (1 <= cilova_pozice[0] <= 8 and 1 <= cilova_pozice[1] <= 8):
        return False
    
    if cilova_pozice in obsazene_pozice:
        return False
    
    dx = cilova_pozice[0] - start[0]
    dy = cilova_pozice[1] - start[1]

    if typ == "pěšec":
        if dy == 0:  
            if dx == 1 and cilova_pozice not in obsazene_pozice:
                return True
            
            elif start[0] == 2 and dx == 2 and (start[0] + 1, start[1]) not in obsazene_pozice:
                return True
        return False
    
    elif typ == "jezdec":   
        return (abs(dx), abs(dy)) in [(2, 1), (1, 2)]
    
    elif typ == "věž":
        if dx == 0 or dy == 0:
            krok_x = 1 if dx > 0 else -1 if dx < 0 else 0
            krok_y = 1 if dy > 0 else -1 if dy < 0 else 0
            x, y = start
            while (x, y) != cilova_pozice:
                x += krok_x
                y += krok_y
                if (x, y) in obsazene_pozice:
                    return False
            return True
        return False
    
    elif typ == "střelec":
        if abs(dx) == abs(dy):
            krok_x = 1 if dx > 0 else -1
            krok_y = 1 if dy > 0 else -1
            x, y = start
            while (x, y) != cilova_pozice:
                x += krok_x
                y += krok_y
                if (x, y) in obsazene_pozice:
                    return False
            return True
        return False
    
    elif typ == "dáma":
        if dx == 0 or dy == 0:
            krok_x = 1 if dx > 0 else -1 if dx < 0 else 0
            krok_y = 1 if dy > 0 else -1 if dy < 0 else 0
            x, y = start
            while (x, y) != cilova_pozice:
                x += krok_x
                y += krok_y
                if (x, y) in obsazene_pozice:
                    return False
            return True
        elif abs(dx) == abs(dy):
            krok_x = 1 if dx > 0 else -1
            krok_y = 1 if dy > 0 else -1
            x, y = start
            while (x, y) != cilova_pozice:
                x += krok_x
                y += krok_y
                if (x, y) in obsazene_pozice:
                    return False
            return True
        return False
    
    elif typ == "král":      
        return max(abs(dx), abs(dy)) == 1 
    return False


if __name__ == "__main__":
    pesec = {"typ": "pěšec", "pozice": (2, 2)}
    jezdec = {"typ": "jezdec", "pozice": (3, 3)}
    vez = {"typ": "věž", "pozice": (8, 8)}
    strelec = {"typ": "střelec", "pozice": (6, 3)}
    dama = {"typ": "dáma", "pozice": (8, 3)}
    kral = {"typ": "král", "pozice": (1, 4)}
    obsazene_pozice = {(2, 2), (8, 2), (3, 3), (5, 4), (8, 3), (8, 8), (6, 3), (1, 4)}

    print(je_tah_mozny(pesec, (3, 2), obsazene_pozice))  # True
    print(je_tah_mozny(pesec, (4, 2), obsazene_pozice))  # True, při prvním tahu, může pěšec jít o 2 pole dopředu
    print(je_tah_mozny(pesec, (5, 2), obsazene_pozice))  # False, protože pěšec se nemůže hýbat o tři pole vpřed (pokud jeho výchozí pozice není v prvním řádku)
    print(je_tah_mozny(pesec, (1, 2), obsazene_pozice))  # False, protože pěšec nemůže couvat

    print(je_tah_mozny(jezdec, (4, 4), obsazene_pozice))  # False, jezdec se pohybuje ve tvaru písmene L (2 pozice jedním směrem, 1 pozice druhým směrem)
    print(je_tah_mozny(jezdec, (5, 4), obsazene_pozice))  # False, tato pozice je obsazená jinou figurou
    print(je_tah_mozny(jezdec, (1, 2), obsazene_pozice))  # True
    print(je_tah_mozny(jezdec, (9, 3), obsazene_pozice))  # False, je to pozice mimo šachovnici

    print(je_tah_mozny(dama, (8, 1), obsazene_pozice))  # False, dámě v cestě stojí jiná figura
    print(je_tah_mozny(dama, (1, 3), obsazene_pozice))  # False, dámě v cestě stojí jiná figura
    print(je_tah_mozny(dama, (3, 8), obsazene_pozice))  # True