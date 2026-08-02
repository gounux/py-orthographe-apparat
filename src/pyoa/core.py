import lirecouleur.text as lt

from pyoa.phonems import OA_PHONEMS


def encode_orthographe_d_apparat(text: str) -> str:
    oa, processed = "", ""
    phonems = lt.phonemes(text)
    for word in phonems:
        if isinstance(word, str):
            oa += word
            processed += word
            continue
        for ph, char in word:
            if char in ["'"]:
                oa += " "
                processed += char
                continue
            oa_ph = OA_PHONEMS[ph].title() if char[0].isupper() else OA_PHONEMS[ph]
            oa += oa_ph
            processed += char
    return oa
