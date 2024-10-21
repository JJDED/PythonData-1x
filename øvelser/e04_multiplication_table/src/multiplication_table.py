#!/usr/bin/env python3


def main():
    for x in range(1, 11):      # Vandret
        for y in range (1, 11): # Lodret
            print('{:4d}'.format(x*y), end = "") # Sammy
            #print(f"{x*y:4d}", end = "") # Søren
        print()

if __name__ == "__main__":
    main()
