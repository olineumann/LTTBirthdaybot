import datetime as dt


questions = [
'''
Was ist größer als Gott
und bösartiger als der Teufel?
Die armen haben es!
Die Glücklichen brauchen es!
Und wenn Du es isst, stirbst Du!
''',
'''
Auf einer kleinen Insel leben genau 100 Personen, von denen ein Teil immer die Wahrheit sagt und der andere Teil immer lügt.
Ein Forscher kommt auf die Insel und fragt jeden Einwohner nach der Anzahl der Lügner.
Der erste sagt: "Es gibt einen Lügner auf der Insel", der zweite sagt: "Es gibt zwei Lügner", u.s.w., bis zum letzten, der erklärt: "Es gibt 100 Lügner".
    
Wie viele Lügner leben auf der Insel?
''',
'''
Was will jeder werden, aber keiner sein?
''',
'''
Wenn man es braucht,
wirft man es weg!
wenn man es nicht braucht,
holt man es wieder zurück!

Was ist das?
'''
]

hints = [
'''
Diese  Rätselaufgabe wurde mal an Kindergärten und
Universitäten gestellt. 85 Prozent der Kindergartenkinder
wussten die Antwort sofort, aber nur 17 Prozent der
Studenten.
''',
'''
Wenn jeder was anderes sagt ...
''',
'''
Vielleicht will man's ja gar nicht so bald werden.
''',
'''
Wenn man es braucht,
wirft man es weg!
wenn man es nicht braucht,
holt man es wieder zurück!

Was ist das?
'''
]

answers = [
'nichts',
'99',
'alt',
'anker'
]

explanations = [
'',
'''
Es sind 99 Lügner!
Da jeder eine andere Zahl sagt,
aber nur eine davon stimmen kann,
haben alle anderen gelogen.
''',
'',
''
]

date = '01.01.2121'
start_date = dt.datetime.strptime(date, '%d.%m.%Y')

replies = {
    'help': 'Das ist dein Geburtstags Bot. Starte ihn mit /start und lass dir die aktuelle Aufgabe mit /quest erzählen. Falls du einmal nicht weiter kommt benutze /hint.',
    'on_start': 'Hallo Reisender! Wir freuen uns schon auf ein spannendes Abenteuer.',
    'no_context': 'Bevor die Reise beginnt musst du diese erst beginnen. Benutze dafür /start.',
    'first_quest': 'Deine erste Frage folgt auch zugleich!',
    'next_quest': 'Deine nächste Frage folgt zugleich!',
    'journey_not_started': f'Leider hat die Reise noch nicht begonnen. Warte bis zum {date}, dann geht es los!',
    'force_starting': 'Ohje... Da ist wohl ein Meister am Werk.',
    'no_quests_left': 'Leider ist die Reise schon vorbei. Wir hoffen es hat dir gefallen!',
    'right': 'Glückwunsch Reisender! Das war richtig!',
    'wrong': 'Das ist leider falsch... Probiere es ruhig weiter!',
    'wants_solve': 'Schade, dass du es nicht geschafft hast. Lass es mich lösen.'
}