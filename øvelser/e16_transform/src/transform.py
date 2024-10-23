#!/usr/bin/env python3

def transform(s1, s2):
    listS1 = s1.split()
    listS2 = s2.split()
    z = zip(map(int, listS1), map(int, listS2))
    return [i*j for i,j in z]

def main():
    print(transform("1  5 3", "2 6 -1"))
    pass

if __name__ == "__main__":
    main()
