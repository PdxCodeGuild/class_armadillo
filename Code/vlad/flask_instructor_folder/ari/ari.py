import re
import string

def count_sentences(text):
    text = text.lower()

    # remove common abbreviations
    # this would not work for something like "he is the best."
    abbreviations = ['st.', 'mr.', 'ms.', 'mrs.', 'rev.', 'dr.', 'a.d.', 'b.c.', 'jr.', 'sr.', 'b.c.e.', 'c.e.', 'phd.']
    for abbreviation in abbreviations:
        text = text.replace(abbreviation, abbreviation.replace('.', ''))

    return text.count('.') + text.count('?') + text.count('!')


def count_words(text):
    results = re.findall(r"[\w']+", text)
    return len(results)


def count_characters(text):
    counter = 0
    for char in text:
        if char in string.ascii_letters:
            counter += 1
    return counter


def calculate_ari(text):
    sentences = count_sentences(text)
    words = count_words(text)
    characters = count_characters(text)

    ari = 4.71*(characters/words) + 0.5*(words/sentences) - 21.43
    ari = round(ari) # round to the nearest whole number
    if ari < 1:
        ari = 1
    elif ari > 14:
        ari = 14

    ari_scale = {
        1: {'ages':   '5-6', 'grade_level': 'Kindergarten'},
        2: {'ages':   '6-7', 'grade_level':    '1st Grade'},
        3: {'ages':   '7-8', 'grade_level':    '2nd Grade'},
        4: {'ages':   '8-9', 'grade_level':    '3rd Grade'},
        5: {'ages':  '9-10', 'grade_level':    '4th Grade'},
        6: {'ages': '10-11', 'grade_level':    '5th Grade'},
        7: {'ages': '11-12', 'grade_level':    '6th Grade'},
        8: {'ages': '12-13', 'grade_level':    '7th Grade'},
        9: {'ages': '13-14', 'grade_level':    '8th Grade'},
        10: {'ages': '14-15', 'grade_level':    '9th Grade'},
        11: {'ages': '15-16', 'grade_level':   '10th Grade'},
        12: {'ages': '16-17', 'grade_level':   '11th Grade'},
        13: {'ages': '17-18', 'grade_level':   '12th Grade'},
        14: {'ages': '18-22', 'grade_level':      'College'}
    }

    return f'The ARI for the given text is {ari}, which corresponds to ages {ari_scale[ari]["ages"]} which is {ari_scale[ari]["grade_level"]}'


# if we run ari.py directly, this code will run
# but if we import it into another module, it won't
if __name__ == '__main__':

    text = '''Marguerite St. Juste was Irish on her mother's side, who was born of
    the Desmonds of Desmondstown in the County Kerry. Marguerite's father
    was a French Comte, whose grandfather had been one of the victims of
    the guillotine.
    Little Marguerite lived with an uncle, who was really only that
    relation by marriage; his name was the Reverend John Mansfield. He had
    a large living in a large town about fifty miles from London, and he
    adopted Marguerite shortly after the death of her parents. This tragedy
    happened when she was very young, almost a baby. She did not in the
    least remember her father, whose dancing black eyes and merry ways had
    endeared him to all who knew him. Nor did she recall a single fact with
    regard to her mother--one of those famous Desmonds, who had joined the
    rebels in the great insurrection of '97, and whose people still lived
    and prospered and were gay and merry of the merry on their somewhat
    tattered and worn-out country estate.
    Marguerite adored "Uncle Jack," as she called her supposed uncle. She
    had a knack of turning this grave and esteemed gentleman, so to speak,
    round her little finger. It was the Rev. John and his wife Priscilla
    who taught little Marguerite all she knew. She adored her uncle; she
    did not like his wife. A sterner or stricter woman than Priscilla
    Mansfield it would be hard to find. Her husband, it is true, considered
    her admirable, for she discovered whenever his parishioners tried to
    impose upon him, and kept the women of his parish well up to the mark.'''

    print(calculate_ari(text))
