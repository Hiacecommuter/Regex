# numbered capturing group


# named capturing groups and named backreferences (Python only)
# (?P<name>group), (?P=name), name must be an alphanumeric sequence starting with a letter
pattern_gb = r"<(?P<tag>[A-Z][A-Z0-9]*)\b[^>]*>.*?</(?P=tag)>"
#Though the syntax for the named backreference uses parentheses, it’s just a backreference that doesn’t do any capturing or grouping


#18 \group#, references the # of capturing group

#19 Backreferences to failed groups
pattern_19 = r"(b?)o\1"

#20 Branch reset group , (?|(a)|(b)|(c))\1
# the regex has only a single capturing with #1 that is shared by all three alternatives
# (a)|(b)|(c) has three capturing groups 1-a, 2-b, 3-c
# (?|abc|(d)(e)(f)|g(h)i) has three capturing groups. 
#     When this regex matches abc, all three groups are empty. 
#     When def is matched, $1 holds d, $2 holds e and $3 holds f. 
#     When ghi is matched, $1 holds h while the other two are empty.
# (x)(?|abc|(d)(e)(f)|g(h)i)(y) defines five capturing groups. 
#     (x) is group 1, (d) and (h) are group 2, (e) is group 3, (f) is group 4, and (y) is group 5.

#21 regex_1(?=regex_2), positive look ahead
#   regex_2 is excluded from the match. (Not consume matches of regex_2)

#22 regex_2(?!regex_2), negative look ahead
#   regex_1 is not to be immediately followed by regex_2 (Not consume matches of regex_2)

#23 (?<=regex_2)regex_1, positive look behind (Not consume matches of regex_2)

#24 (?<!regex_2)regex_1, negative look behind (Not consume matches of regex_2)
