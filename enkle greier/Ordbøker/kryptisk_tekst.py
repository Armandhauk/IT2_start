krypter = { "a": "c", "b": "d", "c": "e", "d": "f", "e": "g", "f": "h", "g": "i", "h": "j", "i": "k", "j": "l", "k": "m",
            "l": "n", "m": "o", "n": "p", "o": "q", "p": "r", "q": "s", "r": "t", "s": "u", "t": "v",
            "u": "w", "v": "x", "w": "y", "x": "z", "y": "æ", "z": "ø", "æ": "å", "ø": "a", "å": "b"
}
tekst="armand"
print(f"{krypter["a"]}{krypter["r"]}{krypter["m"]}{krypter["a"]}{krypter["n"]}{krypter["d"]}")