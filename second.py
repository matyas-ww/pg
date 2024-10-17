def cislo_text(cislo):
    # funkce zkonvertuje cislo do jeho textove reprezentace
    # napr: "25" -> "dvacet pět", omezte se na cisla od 0 do 100
    desitky = {1: "náct",2: "dvacet",3: "třicet",4: "čtyřicet",5: "padesát",6: "šedesát",7: "sedmdesát",8: "osmdesát",9: "devadesát"}
    jednotky = {1: "jedna",2: "dva",3: "tři",4: "čtyři",5: "pět",6: "šest",7: "sedm",8: "osm",9: "devět"}
    jednotky_2 = {1: "jede",2: "dva",3: "tři",4: "čtr",5: "pat",6: "šest",7: "sedm",8: "osm",9: "devate"}

    if len(cislo) > 3:
        return ValueError("cislo je mimo rozsah")
    elif cislo == "100":
        return "sto"
    elif cislo == "10":
        return "deset"
    elif cislo == "0":
        return "nula"
    else:
        rozdelny_string = [i for i in str(cislo)]
        # print(rozdelny_string)
        if len(cislo) < 2:
            return jednotky[int(cislo)]
        else:
            if rozdelny_string[0] == "1":
                return jednotky_2[int(rozdelny_string[1])] + desitky[int(rozdelny_string[0])]
            else:
                if rozdelny_string[1] == "0":
                    return desitky[int(rozdelny_string[0])]
                else:
                    return desitky[int(rozdelny_string[0])] + " " + jednotky[int(rozdelny_string[1])]
                
            

            
        


if __name__ == "__main__":
    cislo = input("Zadej číslo: ")
    text = cislo_text(cislo)
    print(text)



#bolestgit push -u origin master
# ffffdgertre
