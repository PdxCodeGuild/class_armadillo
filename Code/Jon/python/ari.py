import string


text = '''Seht! seit Jahren der Hamburger Jugendschriften-Ausschuß im
Einverständnis mit den übrigen deutschen Prüfungsausschüssen und mit
vielen andern Männern und Frauen, die es mit der deutschen Jugend gut
meinen, Umschau unter den Schätzen, die unsre Dichter ihrem Volke
geschenkt haben, ob nicht Kleinode darunter seien, deren Schönheit
auch Eurem Auge schon offen liege. Wir haben gar kostbare Stücke
der Art gefunden, ja, manch Eines sieht aus, als sei es eigens für
Kindeshand und Kindesherz erschaffen. Da halten wir es nun nicht nur
für eine unserer schönsten Aufgaben, Euch solche Werke möglichst
bequem zugänglich zu machen, sondern wir sehen darin auch geradezu eine
unabweisbare Pflicht! und ich will den Versuch wagen, Euch wenigstens
ahnen zu lassen, um welch große Sache'''

def count_sentences(text):
    text = text.lower()
    honorifics = ['st.', 'mr.','mrs.', 'rev.', 'dr.', 'jr.', 'sr.', 'a.d.', 'b.c.', 'phd.']
    for honorific in honorifics:
        text = text.replace(honorific, honorific.replace('.', ''))
    return text.count('.') + text.count('?') + text.count('!')


def count_words(text):
    text = list(text.split())
    counter = 0
    for word in text:
        counter += 1
    return counter
    

def count_characters(text):
    counter = 0
    for letter in text:
        if letter in string.ascii_letters:
            counter += 1
    return counter

sentences = count_sentences(text)
words = count_words(text)
characters = count_characters(text)


print(f'{sentences=}')
print(f'{words=}')
print(f'{characters=} ')