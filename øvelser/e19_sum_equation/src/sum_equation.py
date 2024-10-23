#!/usr/bin/env python3

def sum_equation(L):
    if len(L) == 0:
        return "0 = 0"
    left = " + ".join([str(n) for n in L])
    right = sum(L)
    return f"{left} = {right}"

def main():
    print(sum_equation([1,5,7]))
    print(sum_equation([0]))
    print(sum_equation([-2, 7, 3.5]))

if __name__ == "__main__":
    main()
