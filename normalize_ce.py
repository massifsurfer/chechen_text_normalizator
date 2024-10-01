import re
import unicodedata

def normalize_ce(text, eliminate_nonchechen_diacritics=True):
    def remove_accents(input_str):
        nfkd_form = unicodedata.normalize('NFKD', input_str)
        bad_diacritic_codes = [768, 769, 770, 771, 772, 778, 780]
        cleaned = u"".join([
            c for c in nfkd_form if ord(c) not in bad_diacritic_codes])
        return unicodedata.normalize('NFKC', cleaned)

    letter_latin = {
        'A': 'А',
        'a': 'а',
        'Y': 'У',
        'O': 'О',
        'o': 'о',
        'B': 'В',
        'E': 'Е',
        'e': 'е',
        'C': 'С',
        'c': 'с',
        'M': 'М',
        'X': 'Х',
        'x': 'х',
        'H': 'Н',
        'T': 'Т',
        'K': 'К',
        'k': 'к',
        'P': 'Р',
        'p': 'р',
        'y': 'у',
        'l': 'Ӏ',
        '1': 'Ӏ',
        'I': 'Ӏ',
        'i': 'Ӏ',
    }
    if eliminate_nonchechen_diacritics:
        text = remove_accents(text)

    small_outdated_palochka = "ӏ"
    standard_palochka = 'Ӏ'
    text = text.replace(small_outdated_palochka, standard_palochka)


    for latin, cyrillic in letter_latin.items():
        text = re.sub(f"{latin}(?=[а-яА-ЯӀ])|(?<=[а-яА-ЯӀ]){latin}", cyrillic, text)
    
    return text
