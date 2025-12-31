import sys

ciphertext = sys.argv[1]


def rot13(input_str: str) -> str:
    result = []

    for ch in input_str:
        code = ord(ch)

        # a-z
        if 97 <= code <= 122:
            result.append(chr(((code - 97 + 13) % 26) + 97))

        # A-Z
        elif 65 <= code <= 90:
            result.append(chr(((code - 65 + 13) % 26) + 65))

        else:
            result.append(ch)

    return "".join(result)


def main():
    print(rot13(ciphertext))


if __name__ == "__main__":
    main()
