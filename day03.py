import sys

def caesar(input_text: str, shift: int) -> str:
    result = []
    for ch in input_text:
        code = ord(ch)
        #less numbers, but still numbers :D 
        #after consulting AI about (x*10)%26 I learned (x%26) works in python 
        #because its always positive, what a good attitude x has eh, stay positive!
        if 'a' <= ch <= 'z':
            result.append(chr((code - ord('a') + shift + 26) % 26 + ord('a')))
        elif 'A' <= ch <= 'Z':
            result.append(chr((code - ord('A') + shift + 26) % 26 + ord('A')))
        else:
            result.append(ch)

    return ''.join(result)

def main():
    if len(sys.argv) < 3:
        print("Usage: python day03.py <text> <shift or -shift>") #thats right encrypt and decrypt
        return

    ciphertext = sys.argv[1]
    shift = int(sys.argv[2]) #cheeky little argv what are you doing
    print(caesar(ciphertext, shift))

if __name__ == "__main__":
    main()