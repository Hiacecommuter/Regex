"""
\b matches at a position so-called word boundary. This match is zero length.
There are three different positions that qualify as word boundary:
1. before the first character in the string, if the first character is a word character
2. After the last character in the string, if the last character is a word character
3. Between two characters in the string, where one is a word character and the other is not a word character

\b is whole word only 
pattern = r"\bword\b"

\d is [0-9]
\w is [A-Za-z0-9_]
\s is [ \t\r\n\f]

"""
