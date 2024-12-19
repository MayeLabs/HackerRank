# Input: Read year, the year to test.
# Output: return a Boolean value (True/False).
# Example: 1990 -> False

def is_leap(year):
    leap = False
    
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                leap = True
    return leap

year = int(input())
print(is_leap(year))