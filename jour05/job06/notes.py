def round_notes(notes):
    rounded_notes = []
    for note in notes:
        if note < 40:
            rounded_notes.append(note)
        else:
            multiple = 5 * (note // 5 + 1)
            if note + 3 >= multiple:
                rounded_notes.append(multiple)
            else:
                rounded_notes.append(note)
    return rounded_notes

notes = [38, 45, 82, 83.5, 84, 46]
notes_arrondies = round_notes(notes)
print(notes_arrondies)