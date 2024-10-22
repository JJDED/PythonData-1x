#!/usr/bin/env python3

def interleave(*lists):
    interleaved_list = []
    
    for group in zip(*lists):
        interleaved_list.extend(group)
    
    return interleaved_list 

def main():
    print(interleave([1, 2, 3], [20, 30, 40], ['a', 'b', 'c']))

if __name__ == "__main__":
    main()
