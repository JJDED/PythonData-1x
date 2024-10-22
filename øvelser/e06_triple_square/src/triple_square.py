#!/usr/bin/env python3

def triple(n):
    return n * 3

def square(n):
    return n ** 2

#def main():
#    for i in range(1, 11):  # Loop through 1 to 10
#        print(f"triple({i})=={triple(i)} square({i})=={square(i)}")

def main():
    for i in range(1, 11): 
        t = triple(i)
        s = square(i)
        
        if s > t:
            break
        
        print(f"triple({i})=={t} square({i})=={s}")

if __name__ == "__main__":
    main()
