
name = input("what is your name? ")
date = input("what is today\'s date? ")

noun1 = input("enter a noun: ")
noun2 = input("enter a place: ")
noun3 = input("enter a noun: ")
#noun4 = input("enter a noun: ")
#noun5 = input("enter a noun: ")
verb1 = input("enter a verb, past tense: ")
#verb2 = input("enter a verb: ")
#verb3 = input("enter a verb: ")
#verb4 = input("enter a verb: ")
#verb5 = input("enter a verb: ")
adjective1 = input("enter an adjective: ")
adjective2 = input("enter an adjective: ")
#adjective3 = input("enter an adjective: ")
#adverb1 = input("enter an adverb: ")
#adverb2 = input("enter an adverb: ")

story_template = f"Once upon a time, the {adjective1} {noun1} {verb1} to {noun2}. While there, it came across a {adjective2} \
{noun3}"

print(f"Your name is {name.title()}")
print(f"Today\'s date is {date}")
print(story_template)
