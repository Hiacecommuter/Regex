#Greedy: try to march more
pattern_g1 = r"Feb 23(rd)?" 
string_g1 = "Today is Feb 23rd, 2003" 
#The match is always "Feb 23rd"

pattern_g2 = r"<.+>" 
string_g2 = "This is a <EM>first</EM>" # match all of it other than 2 separate results

"""
<.+>, <EM>first</EM> test
1 start match from "<" 
2 . continues to matchn until end of the string (including >, <, and > ), greedy
3 > not match, regex engine backtracks from t, then s, e, t, " "
4 > found, return a match
"""

#Laziness, ?
# put ? after +, *, {}, and ? itself to make them lazy

"""
<.+?>
1  start match from "<"
2  match . once (minimum times)
3  match >, fail, match . again, repeat
"""

"""
Let’s apply the regular expression colou?r to the string The colonel likes the color green.
The first token in the regex is the literal c. 
The first position where it matches successfully is the c in colonel. 
The engine continues, and finds that o matches o, l matches l and another o matches o. 
Then the engine checks whether u matches n. 
This fails. 
However, the question mark tells the regex engine that failing to match u is acceptable. 
Therefore, the engine skips ahead to the next regex token: r. 
But this fails to match n as well. 
Now, the engine can only conclude that the entire regular expression cannot be matched starting at the c in colonel. 
Therefore, the engine starts again trying to match c to the first o in colonel.
After a series of failures, c matches the c in color, and o, l and o match the following characters. 
Now the engine checks whether u matches r. 
This fails. Again: no problem. 
The question mark allows the engine to continue with r. 
This matches r and the engine reports that the regex successfully matched color in our string.
"""
