# Given a String S, reverse the string without reversing its individual words. Words are separated by dots.

# Example 1:

# Input:
# S = i.like.this.program.very.much
# Output: much.very.program.this.like.i
# Explanation: After reversing the whole
# string(not individual words), the input
# string becomes
# much.very.program.this.like.i
# Example 2:

# Input:
# S = pqr.mno
# Output: mno.pqr
# Explanation: After reversing the whole
# string , the input string becomes
# mno.pqr

def reverse_words_in_string(S):
    words = S.split('.')
    words.reverse()    
    reversed_string = '.'.join(words)
    
    return reversed_string
