def computegrade(Score):
    if Score > .99:
        grade = 'Score must be between 0.0 and 1.0'
    elif Score >= 0.9:
        grade = 'A'
    elif Score >= 0.8:
        grade = 'B'
    elif Score >= 0.7:
        grade = 'C'
    elif Score >= 0.6:
        grade = 'D'
    elif Score < 0.6:
        grade = 'F'
    else:
        grade = 'Score must be between 0.0 and 1.0'
    return grade
