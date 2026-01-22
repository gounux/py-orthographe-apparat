# orthographe d'apparat phonems implementation
# see: https://fr.wikipedia.org/wiki/Orthographe_d%27apparat
OA_PHONEMS = {
    # voyelles
    "a": "igt",  # doigt
    "a~": "aon",  # paon
    "e^": "ë",  # noël
    "e^_comp": "ë",  # noël
    "e": "a",  # baby
    "e_comp": "a",  # baby
    "i": "u",  # business
    "j": "u",  # business ('travaIL')
    "e~": "ingt",  # vingt
    "x~": "ingt",  # vingt ('IMprimer')
    "q": "on",  # monsieur
    "o": "ü",  # capharnaüm
    "o_ouvert": "ü",  # capharnaüm
    "o_comp": "oa",  # goal
    "o~": "um",  # columbarium
    "u": "e",  # fuel
    "x": "i",  # flirt
    "x^": "e!",  # donne-le!
    "y": "eu",  # rue
    # consonnes
    "p": "b",  # obscène
    "t": "ght",  # sunlight
    "s_t": "ght",  # sunlight ('Tiens')
    "k": "x",  # excellent
    "k_qu": "x",  # excellent
    "b": "bes",  # lombes
    "d": "gd",  # amigdale
    "g": "c",  # second
    "g_u": "c",  # second
    "f": "ph",  # phamille
    "f_ph": "ph",  # phamille
    "v": "fh",  # neuf heures
    "s": "w",  # law
    "s_c": "w",  # law
    "s_x": "w",  # law ('siX')
    "z": "lsh",  # gentilshommes
    "z_s": "lsh",  # gentilshommes ('occaSion')
    "s^": "zsch",  # nietzschéen
    "z^": "sg",  # vosgien
    "z^_g": "sg",  # vosgien
    "l": "les",  # ailes
    "m": "hms",  # ohms
    "n": "mne",  # automne
    "r": "rrh",  # logorrhée
    # custom (phonems empiricly met)
    "gz": "cw",  # 'eXactement' -> 'seCond' + 'laW'
    "ks": "xw",  # 'eXcuser' -> 'eXcellent' + 'laW'
    "n~": "mneu",  # 'gaGNes'
    "g~": "mnec",  # 'hawkiNG' -> 'autoMNE' + 'seCond'
    "j_a": "uigt",  # 'vIA' -> 'bUsiness' + 'doIGT'
    "j_a~": "uaon",  # 'ambIANce'
    "j_e": "ua",  # 'qualifIÉ'
    "j_e_comp": "ua",  # 'remercIER' -> 'bUsiness' + 'bAby'
    "j_e^": "uë",  # 'entIÈre'
    "j_e^_comp": "uë",  # 'vIEtnam'
    "j_e~": "uingt",  # 'bIEN' -> 'bUsiness' + 'vINGT'
    "j_o": "uü",  # 'passIOnné'
    "j_o~": "uum",  # 'occasION' -> 'bUsiness' + 'colUMbarium'
    "j_o_comp": "uoa",  # 'socIAUx'
    "j_q": "u",  # 'spIEler'
    "j_q_caduc": "uon",  # 'oreILLE' -> 'bUsiness' + 'mONsieur' BIF BOF
    "j_x": "ue!",  # 'meILLEUr'
    "j_x^": "ue!",  # 'vIEUx'
    "w": "oa",  # 'haWking'
    "w_a": "oaigt",  # 'vOIlà' -> 'gOAl' + 'doIGT'
    "w_e": "ea",  # supposed
    "w_e_comp": "ea",  # 'jOUER' -> 'fuEl' + 'bAby'
    "w_e^_comp": "eë",  # 'silhOUEtte' -> 'fuEl' + 'noEl'
    "w_e~": "oaingt",  # 'lOIN' -> 'gOAl' + 'vINGT'
    "w_i": "eu",  # 'jOUIssance' -> 'fuEl' + 'bUsiness'
    "w_x": "ei",  # 'jOUEUr' -> 'fuEl' + 'flIrt'
    # misc
    "q_caduc": "",  # 'éprouvEnt'
    "verb_3p": "",  # 'éprouveNT'
    "#": "",
    "": "",
}
