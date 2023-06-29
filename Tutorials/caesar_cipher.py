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
    return translated_message


def crypt_this(message, offset):
    translated_message = ""

    for character in message:
        if character in alphabet:
            character_value = alphabet.find(character)
            translated_character = alphabet[(character_value - offset) % 26]
            translated_message += translated_character
        else:
            translated_message += character
    return translated_message


# print(caesar_decode("xuo jxuhu! jxyi yi qd unqcfbu ev q squiqh syfxuh. muhu oek qrbu je tusetu yj? y xefu ie! iudt cu q cuiiqwu rqsa myjx jxu iqcu evviuj!", 10))

# print(crypt_this("Hey, my name is Tristan. This is a secret message. Can you read it?!", 10))

# print(caesar_decode("Huo, co dqcu yi Thyijqd. Txyi yi q iushuj cuiiqwu. Cqd oek huqt yj?!", 10))

# print(caesar_decode("jxu evviuj veh jxu iusedt cuiiqwu yi vekhjuud.", 10))
# print(caesar_decode("bqdradyuzs ygxfubxq omqemd oubtqde fa oapq kagd yqeemsqe ue qhqz yadq eqogdq!", 14))


# BruteForcer
def brute_forcer(message, max_offset):
    for offset in range(1, max_offset + 1):
        decoded_message = caesar_decode(message, offset)
        print(f"Offset {offset}: {decoded_message}")


brute_forcer(
    "vhfinmxkl atox kxgwxkxw tee hy maxlx hew vbiaxkl hulhexmx. px'ee atox mh kxteer lmxi ni hnk ztfx by px ptgm mh dxxi hnk fxlltzxl ltyx.",
    20,
)
