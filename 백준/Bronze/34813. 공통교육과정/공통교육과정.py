def main() :
    S = input()
    if S[0] == 'F' :
        print("Foundation")
    elif S[0] == 'C' :
        print("Claves")
    elif S[0] == 'V' :
        print("Veritas")
    else :
        print("Exploration")
        
if __name__ == "__main__" :
    main()