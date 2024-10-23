#!/usr/bin/env python3

class Prepend(object):
    # Add the methods of the class here
    def __init__(self, begynd):
        self.begynd = begynd

    def write (self, tekst):
        print(self.begynd + tekst)
        
def main():
    p = Prepend("xxx ")
    p.write("Hello")
    

if __name__ == "__main__":
    main()
