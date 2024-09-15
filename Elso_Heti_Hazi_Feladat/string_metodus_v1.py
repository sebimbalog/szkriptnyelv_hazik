#!/usr/bin/env python3

# A program bekér egy nevet, és megkeresi benne, hányszor található meg áltatunk
# megadott betű

def main():
    name = input("Kérlek adja meg a nevét: ") # itt található az első input
    letter_finder = input("Itt adja meg kérem, melyik betüt keresi: ") # itt kell megadni melyik stringet keressük

    getted_word = name.count(letter_finder) # itt futattjuk a count függvényt, 
                            #, hogy megkapjuk a keresett betű megtalált helyeit 

    getted_word_string = str(getted_word)

    print("Ennyiszer találtuk meg benne meg a nevet: " + getted_word_string) # itt csak simán kiiratjuk a megoldást

#és itt megirjuk a következőt
if __name__ == "__main__":
    main()