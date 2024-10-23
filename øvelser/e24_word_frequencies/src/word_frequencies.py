#!/usr/bin/env python3

def word_frequencies(filename):
    wd = {}
    with open(filename, "r", newline="\r\n") as f:
        #for s in f:
        s = f.read()
        words = [w.strip("""!"#$%&'()*,-./:;?@[]_""") for w in s.split()]
        for w in words:
            if w in wd:
                wd[w] += 1
            else:
                wd[w] = 1 

    return wd

def main():
    fname = r"C:\Users\Jamie\Desktop\Projekter\TECH3\Python\PythonData\PythonData-1x\øvelser\e24_word_frequencies\src\alice.txt"
    wd = word_frequencies(fname)

    wd = dict(sorted(wd.items(), key=lambda i: i[1], reverse=True))

    for w, c in list(wd.items())[:5]:
         print(w, c, sep="\t")


if __name__ == "__main__":
    main()
