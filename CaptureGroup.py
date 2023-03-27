# grouping and capturing

#15 \b asset position at word boundary
"""
Three different positions qualify for word boundaries :
► Before the first character in the string, if the first character is a word character.
► Between two characters in the string, where one is a word character and the other is not a word character.
► After the last character in the string, if the last character is a word character.
"""

#16 Parenthesis () around a regular expression can group that part of regex togeter
#   Any subpattern inside a pair of parentheses will be captured as a group.
pattern16_1 = r"^(IMG\d+\.png)$" # captures image file names
pattern16_2 = r"^(IMG\d+)\.png$" # captures the part inside the parenthesis

text = 'abcdefg'
pattern16_31 = r"(\w)\w" # ['a', 'c', 'e']
pattern16_32 = r"\w(\w)" # ['b', 'd', 'f']
pattern16_33 = r"()\w\w" # ['', '', '']
pattern16_34 = r"(\w\w)" # ['ab', 'cd', 'ef']
pattern16_35 = r"(\w)(\w)" # [('a', 'b'), ('c', 'd'), ('e', 'f')]

# (?:), non-capturing group
pattern16_36 = r"(?:\w)\w" # ['ab', 'cd', 'ef']
pattern16_37 = r"\w(?:\w)" # ['ab', 'cd', 'ef']
pattern16_38 = r"(?:)\w\w" # ['ab', 'cd', 'ef']
pattern16_39 = r"(?:\w\w)" # ['ab', 'cd', 'ef']
pattern16_310 = r"(?:\w)(\w)" #  ['b', 'd', 'f']
pattern16_311 = r"(\w)(?:\w)" #  ['a', 'c', 'e']

#17 |, alternations 
#   (Bob|Kevin|Stuart) will match either Bob or Kevin or Stuart.
#   ([a-f]|[A-F]) will match one of the class
