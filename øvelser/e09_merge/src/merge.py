#!/usr/bin/env python3

# Funktion til at merge to lister
def merge(L1, L2):
    L = []  

    i, j = 0, 0  

    while i < len(L1) and j < len(L2):
        if L1[i] < L2[j]:
            L.append(L1[i])  
            i += 1  
        else:
            L.append(L2[j])  
            j += 1  

    while i < len(L1):
        L.append(L1[i])
        i += 1
    
    while j < len(L2):
        L.append(L2[j])
        j += 1
    
    return L 


def main():
    L1 = sorted([1, 3, 5, 7])
    L2 = sorted([2, 4, 6, 8])    
   
    result = merge(L1, L2)

    L1 = sorted([10, 20, 30])
    L2 = sorted([5, 15, 25, 35])
   
    result = merge(L1, L2)

    L1 = sorted([6, 69, 666])
    L2 = sorted([33, 50, 420, 999])
   
    result = merge(L1, L2)
    print(result)  

if __name__ == "__main__":
    main()
