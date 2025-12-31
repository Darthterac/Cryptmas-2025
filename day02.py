import sys

ciphertext = sys.argv[1]

def atbash(argTxt: str) -> str:
    result = []
    for ch in argTxt:
        code = ord(ch)
        #cheated here trying to be cleaver:
        #sum the range ;) a-z|97+122=219-code if lower A-Z|65+90=155-code if upper otherwise raw
        result.append(chr(219 - code if ch.islower() else 155 - code if ch.isupper() else code))
    return ''.join(result)

def main():
    print(atbash(ciphertext))

if __name__ == "__main__":
    main()