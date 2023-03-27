# match a tag without attribute
pattern_ht1 = r"<[A-Za-z][A-Za-z0-9]*> "

# match one tag only
pattern_ht2 = r"<.+?>"
pattern_ht3 = r"<[^>]+>" # better, reduce the backtracking
