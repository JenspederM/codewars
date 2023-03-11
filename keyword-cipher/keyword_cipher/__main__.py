import string


def keyword_cipher(msg, keyword):
    lower_alphabet = string.ascii_lowercase
    lower_msg = msg.lower()
    lower_keyword = keyword.lower()

    unique_kw = ""
    for char in lower_keyword:
        if char not in unique_kw:
            unique_kw += char

    cipher_alphabet = unique_kw + "".join(
        char for char in lower_alphabet if char not in unique_kw
    )

    cipher = dict(zip(lower_alphabet, cipher_alphabet))

    msg = "".join(
        cipher[char] if char in lower_alphabet else char for char in lower_msg
    )

    return msg


if __name__ == "__main__":
    tests = [
        (("Welcome home", "secret"), "wticljt dljt"),
        (("hello", "wednesday"), "bshhk"),
        (("HELLO", "wednesday"), "bshhk"),
        (("HeLlO", "wednesday"), "bshhk"),
        (("WELCOME HOME", "gridlocked"), "wlfimhl kmhl"),
        (("alpha bravo charlie", "delta"), "djofd eqdvn lfdqjga"),
        (("Home Base", "seven"), "dlja esqa"),
        (("basecamp", "covert"), "ocprvcil"),
        (("one two three", "rails"), "mks twm tdpss"),
        (("Test", "unbuntu"), "raqr"),
    ]

    for args, expected in tests:
        print(f"keyword_cipher({args}) == {expected}")
        assert keyword_cipher(*args) == expected
