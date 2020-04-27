"""
Given a 32-bit signed integer, reverse digits of an integer.

Variable | Value
x        | some given Int

Restated
    - Return reveresed Int

Questions
    - Can the given Int be a negative

Assumptions
    - The given Int can be a negative

Thinking Out Loud
    Make x a string the reverse it then make it an Int again
    return that
"""

def reverse(x):
    x = abs(x)
    y = -1 if x <0 else 1

    x = int(str(x)[::-1])
    return x*y

print(reverse(568))