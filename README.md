# SORT CONTACTS

Write a sort_contacts function that **takes a dictionary of contacts as a parameter** and **returns a sorted list of those contacts**, where each contact is a tuple.

The contacts dictionary that will be passed into the function has the contact name as its `key`, and the `value` is a *tuple containing the phone number and email* for the contact.

>contacts = {name: (phone, email), name: (phone, email), etc.}

The sort_contacts function should then create a new, **sorted (by last name)** list of tuples representing all of the contact info (one tuple for each contact) that was in the dictionary. It should then return this list to the calling function.

**For example, given a dictionary argument of:**

```json
{
    "Horney, Karen": ( "1-541-656-3010", "karen@psychoanalysis.com" ),
    "Welles, Orson": ( "1-312-720-8888", "orson@notlive.com" ),
    "Freud, Anna": ( "1-541-754-3010", "anna@psychoanalysis.com" )
}
```

**sort_contacts should return this**:

```json
[
    ('Freud, Anna', '1-541-754-3010', 'anna@psychoanalysis.com'),
    ('Horney, Karen', '1-541-656-3010', 'karen@psychoanalysis.com'),
    ('Welles, Orson', '1-312-720-8888', 'orson@notlive.com')
]
```
