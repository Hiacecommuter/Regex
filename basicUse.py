r"" # no need to use escape for \
"" # need to use escape for \

#1 basic string matching
pattern1 = r"wikipedia"

#2 regex reserved characters : ., +, *, ?, ^, $, (, ), [, ], {, }, |, \.
#  dot . matches anything(expect for a lewline)
pattern2 = r"^...\....\....\....$"

#3 digit \d and non digit \D

#4 whitespace \s and non whitespace \S

#5 word character \w (alphanumeric characters a-z A-Z 0-9 underscores _) and non word character \W

#6 start of a string ^, end of a strng %

# character class

#7 character class [], match one of several characters placed inside the []
pattern7 = r'[aeiou]'

#8 negated character class {^], matches any characters that is not in [^] (exclude)
pattern8 = r"[aeiou]'

#9 a set of character [-] (inclusive), a caret means negation  [^ - ] (not in the range)
pattern9 = r'[a-z][1-9][^a-z][^A-Z][A-Z]'

# repetitions 

#10 {x}, matches exactly x repetitions of character, character class, or groups
pattern10 = r'[A-Za-z02468]{40}[13579\s]{5}'

#11 {x, y}, matches between x and y (inclusive) repetitions of  character, character class, or groups
pattern11 = r'\d{1,2}[A-Za-z]{3,}[.0123]{0,3}'
#{0, } is same as *, {1,} is same as +

#12 *, matches zero or more repetitions

#13 +, matches one or more repetitions

#14 $, the $ boundary matcher matches an occurence of a character, character class, or group at end of a line

#extra1 ?, makes the preceding token in the regular expression optional. (same as {0, 1})
#   ( )?, makes several tokens optional
pattern_e1 = r"colou?r" # colour and color
pattern_e12 = r"Nov(ember)?" # Nov and November




