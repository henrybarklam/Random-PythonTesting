def gradingStudents(grades):
    lst = grades.split(" ")
    newLst = lst[1:]

    for indG in range(newLst):
        if newLst[indG] > 40:
            if newLst[indG]%5 > 3:
                newLst[indG] = (newLst[indG]//5) * 5 + 5
    for grade in newLst:
        print(grade)
    return newLst