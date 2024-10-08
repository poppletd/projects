
name = input("what is your name? ")
date = input("what is today\'s date? ")

adjective1 = input("enter an adjective: ")
noun1 = input("enter a noun: ")
verb1 = input("enter a verb, past tense: ")
noun2 = input("enter a place: ")
adjective2 = input("enter an adjective: ")
noun3 = input("enter a noun: ")
adverb1 = input("enter an adverb: ")
verb2 = input("enter a verb ending in ing: ")
verb3 = input("enter a verb, past tense: ")
adjective3 = input("enter an adjective: ")
noun4 = input("enter a place: ")
adverb2 = input("enter an adverb: ")
verb4 = input("enter a verb, past tense: ")
noun5 = input("enter a place: ")
verb5 = input("enter a verb, past tense: ")

story_template = f"Once upon a time, the {adjective1} {noun1} {verb1} to {noun2}. While there, it came across a {adjective2} \
{noun3} {adverb1} {verb2}. The {noun1} and the {noun3} {verb3} to a {adjective3} {noun4}, there they /
{adverb2} {verb4} and had lots of fun. Finally, the {noun1} returned to {noun5} and {verb5}. "

print(f"Your name is {name.title()}")
print(f"Today\'s date is {date}")
print(story_template)

