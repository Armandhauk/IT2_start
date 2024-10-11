krypter = {
 "a": "c", "b": "d", "c": "e", "d": "f", "e": "g",
 "f": "h", "g": "i", "h": "j", "i": "k", "j": "l",
 "k": "m", "l": "n", "m": "o", "n": "p", "o": "q",
 "p": "r", "q": "s", "r": "t", "s": "u", "t": "v",
 "u": "w", "v": "x", "w": "y", "x": "z", "y": "æ",
 "z": "ø", "æ": "å", "ø": "a", "å": "b", " ": "."
}

ukryptert = "dekryptert beskjed"
kryptert = ""

for bokstav in ukryptert:
    kryptert += krypter[bokstav]

print(kryptert)
dekryptert = ""

dekrypter = {
 "c": "a", "d": "b", "e": "c", "f": "d", "g": "e",
 "h": "f", "i": "g", "j": "h", "k": "i", "l": "j",
 "m": "k", "n": "l", "o": "m", "p": "n", "q": "o",
 "r": "p", "s": "q", "t": "r", "u": "s", "v": "t",
 "w": "u", "x": "v", "y": "w", "z": "x", "æ": "y",
 "ø": "z", "å": "æ", "a": "ø", "b": "å", ".": " "
}

for bokstav in kryptert:
 dekryptert += dekrypter[bokstav]

print(dekryptert)