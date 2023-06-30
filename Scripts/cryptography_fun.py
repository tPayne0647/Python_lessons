alphabet = "abcdefghijklmnopqrstuvwxyz"


def caesar_decode(message, offset):
    translated_message = ""

    for character in message:
        if character in alphabet:
            character_value = alphabet.find(character)
            translated_character = alphabet[(character_value + offset) % 26]
            translated_message += translated_character
        else:
            translated_message += character
    return "Decoded message: " + translated_message


def caesar_encode(message, offset):
    translated_message = ""

    for character in message:
        if character in alphabet:
            character_value = alphabet.find(character)
            translated_character = alphabet[(character_value - offset) % 26]
            translated_message += translated_character
        else:
            translated_message += character
    return "Encrypted message: " + translated_message


# BruteForcer
def brute_forcer(message, max_offset):
    for offset in range(1, max_offset + 1):
        decoded_message = caesar_decode(message, offset)
        print(f"Offset {offset}: {decoded_message}")


def vigenere_encode(message, keyword):
    keyword_phrase = ""
    keyword_index = 0

    for character in message:
        if keyword_index >= len(keyword):
            keyword_index = 0
        if character in alphabet:
            keyword_phrase += keyword[keyword_index]
            keyword_index += 1
        else:
            keyword_phrase += character

    encoded_message = ""

    for i in range(len(message)):
        if message[i] in alphabet:
            old_character_index = alphabet.find(message[i])
            offset_index = alphabet.find(keyword_phrase[i])
            new_character = alphabet[(old_character_index - offset_index) % 26]
            encoded_message += new_character
        else:
            encoded_message += message[i]

    return encoded_message


def vigenere_decode(message, keyword):
    keyword_phrase = ""
    keyword_index = 0

    for character in message:
        if keyword_index >= len(keyword):
            keyword_index = 0
        if character in alphabet:
            keyword_phrase += keyword[keyword_index]
            keyword_index += 1
        else:
            keyword_phrase += character

    decoded_message = ""

    for i in range(len(message)):
        if message[i] in alphabet:
            old_character_index = alphabet.find(message[i])
            offset_index = alphabet.find(keyword_phrase[i])
            new_character = alphabet[(old_character_index + offset_index) % 26]
            decoded_message += new_character
        else:
            decoded_message += message[i]

    return decoded_message


# Test Caesar Decoder
print(
    caesar_decode(
        "xuo jxuhu! jxyi yi qd unqcfbu ev q squiqh syfxuh. muhu oek qrbu je tusetu yj? y xefu ie! iudt cu q cuiiqwu rqsa myjx jxu iqcu evviuj!",
        10,
    )
)

# Test Caesar encode/decode
print(caesar_encode("Hey, my name is Tristan. This is a secret message. Can you read it?!", 10))
print(caesar_decode("Huo, co dqcu yi Thyijqd. Txyi yi q iushuj cuiiqwu. Cqd oek huqt yj?!", 10))


# Test Bruteforcer
brute_forcer(
    "vhfinmxkl atox kxgwxkxw tee hy maxlx hew vbiaxkl hulhexmx. px'ee atox mh kxteer lmxi ni hnk ztfx by px ptgm mh dxxi hnk fxlltzxl ltyx.",
    20,
)


# Test Vigenere Decoder
vigenere_message = (
    "txm srom vkda gl lzlgzr qpdb? fepb ejac! ubr imn tapludwy mhfbz cza ruxzal wg zztcgcexxch!"
)
vigenere_keyword = "friends"
print(vigenere_decode(vigenere_message, vigenere_keyword))


# Test Vigenere encode/decode
test_message = "Did my encoder work?! Please tell me you can read this?"
test_message_keyword = "flash"
print(vigenere_encode(test_message, test_message_keyword))
print(
    "\n"
    + vigenere_decode(vigenere_encode(test_message, test_message_keyword), test_message_keyword)
)
