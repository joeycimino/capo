grade = input("Enter a number grade:")
try:
    grade = int(grade)
    if 93 <= grade <= 100:
        print("Grade: A")
    elif 85 <= grade < 93:
        print("Grade: B")
    elif 74 <= grade < 85:
        print("Grade: C")
    elif 63 <= grade < 74:
        print("Grade: D")
    elif grade <= 62:
        print("Grade: F")
except:
    if type(grade) != int:
        print("Enter a number grade.")
        
    
