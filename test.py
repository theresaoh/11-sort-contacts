from sort_contacts import sort_contacts

test_cases = [
    {
        "input": {"Horney, Karen": ("1-541-656-3010", "karen@psychoanalysis.com"),
                  "Welles, Orson": ("1-312-720-8888", "orson@notlive.com"),
                  "Freud, Anna": ("1-541-754-3010", "anna@psychoanalysis.com")},
        "output": [('Freud, Anna', '1-541-754-3010','anna@psychoanalysis.com'),
                   ('Horney, Karen', '1-541-656-3010', 'karen@psychoanalysis.com'),
                   ('Welles, Orson', '1-312-720-8888', 'orson@notlive.com')],
    },
    {
        "input": {"Summitt, Pat": ("1-865-355-4320", "pat@greatcoaches.com"),
                  "Rudolph, Wilma": ("1-410-5313-584", "wilma@olympians.com")},
        "output": [('Rudolph, Wilma', '1-410-5313-584', 'wilma@olympians.com'),
                   ('Summitt, Pat', '1-865-355-4320', 'pat@greatcoaches.com')],
    },
    {
        "input": {"Dinesen, Isak": ("1-718-939-2548", "isak@storytellers.com")},
        "output": [('Dinesen, Isak', '1-718-939-2548', 'isak@storytellers.com')],
    },
    {
        "input": {"Rimbaud, Arthur": ("1-636-555-5555", "arthur@notlive.com"),
                  "Swinton, Tilda": ("1-917-222-2222", "tilda@greatActors.com"),
                  "Almodovar, Pedro": ("1-990-622-3892", "pedro@filmbuffs.com"),
                  "Kandinsky, Wassily": ("1-333-555-9999", "kandinsky@painters.com")},
        "output": [('Almodovar, Pedro', '1-990-622-3892', 'pedro@filmbuffs.com'),
                   ('Kandinsky, Wassily', '1-333-555-9999', 'kandinsky@painters.com'),
                   ('Rimbaud, Arthur', '1-636-555-5555', 'arthur@notlive.com'),
                   ('Swinton, Tilda', '1-917-222-2222', 'tilda@greatActors.com')],
    },
]

def test_assignment():
    for test_case in test_cases:
        assignment_response = sort_contacts(test_case['input'])
        assert assignment_response == test_case[
            'output'], f"""
For
\nInput:    {test_case['input']}
\nExpected: {test_case['output']}
\nGot:      {assignment_response}\n"""
