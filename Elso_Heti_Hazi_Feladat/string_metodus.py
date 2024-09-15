#!/usr/bin/env python3

# A program egy stringet bekér, és a szóközöket levágja róla

def main():
    name = input("Name:        ")# Egy bemenet plusz szóközekkel
    name_without_space = name.strip() # Itt levesszük róla a stringeket

    print("Hello " + name_without_space + "!") # Itt majd ki irjuk

if __name__ == "__main__":
    main()