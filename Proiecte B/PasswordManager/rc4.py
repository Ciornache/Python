import math 


def encrypt(key:str, P:list, op:str) -> str:


    S = [i for i in range(0, 256)]
    K = [ord(c) for c in key]


    T:list = (K * int(len(S) / len(K)))
    T += (K[0:len(S) % len(K)])

    # Generate a permutation of the S array

    j = 0   
    for i in range(0, 256):
        j = (j + S[i] + T[i]) % 256
        S[i], S[j] = S[j], S[i]

    # Generate the KeyStream

    KeyStream = []
    i = j = k = 0
    while k < len(P):
        j = (j + S[i]) % 256
        i = (i + 1) % 256
        S[i], S[j] = S[j], S[i]
        KeyStream.append(S[(S[i] + S[j]) % 256])
        k = k + 1

    return [p ^ KeyStream[i] for (i, p) in enumerate(P)]




def main() -> None:
    pass

if __name__ == '__main__':
    main()