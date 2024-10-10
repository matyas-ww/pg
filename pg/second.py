def cislo_text(cislo):
    # funkce zkonvertuje cislo do jeho textove reprezentace
    # napr: "25" -> "dvacet pět", omezte se na cisla od 0 do 100
    desitky = {1: "náct",2: "dvacet",3: "Třícet",4: "čtyřicet",5: "padesát",6: "šedesát",7: "sedmdesát",8: "osmdesát",9: "devadesát"}
    jednotky = {1: "jedna",2: "dva",3: "Tři",4: "čtyři",5: "pět",6: "šest",7: "sedm",8: "osm",9: "devět"}
    if len(cislo) > 3:
        return ValueError("cislo je mimo rozsah")
    elif cislo == 100:
        return "sto"
    else:
        rozdelny_string = [i for i in str(cislo)]
        print(rozdelny_string)
        if rozdelny_string[1]:
            pass

            
        


if __name__ == "__main__":
    cislo = input("Zadej číslo: ")
    text = cislo_text(cislo)
   # print(text)