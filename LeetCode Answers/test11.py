def format_duration(seconds):
    if seconds // 60 == 0 or seconds // 3600 == 0 or seconds // 86400 == 0 or seconds // 31536000 == 0:
        print(single(seconds))

    return


def single(seconds):
    seconds_in_year = 60 * 60 * 24 * 365
    seconds_in_day = 60 * 60 * 24
    seconds_in_hour = 60 * 60
    seconds_in_minute = 60
    years = seconds // seconds_in_year
    days = (seconds - (years * seconds_in_year)) // seconds_in_day
    hours = (seconds - ((years * seconds_in_year) + (days * seconds_in_day))) // seconds_in_hour
    minutes = (seconds - (years * seconds_in_year) - (days * seconds_in_day) - (
                hours * seconds_in_hour)) // seconds_in_minute
    l_seconds = (seconds - (years * seconds_in_year) - (days * seconds_in_day) - (hours * seconds_in_hour) - (
                minutes * seconds_in_minute))
    cnt_lst = [years, days, hours,minutes,l_seconds]
    print(cnt_lst)
    return cnt_lst

def sentenceMaker(listWords):
    tWords = ["years" , "days", "hours", "minutes", "seconds"]
    newList = []
    for ind in range(len(listWords)):
        if listWords[ind] != 0:
            if listWords[ind] != 1:
                newList.append(str(listWords[ind]) + " " + tWords[ind])

            else:
                newList.append(str(listWords[ind] + " " + tWords[ind][:-1]))
        else:
            newList.append(str(listWords[0]))
    print(newList)
    newW = " ".join(newList)
    if newList[-1] == '0' and :
        return "now"
    if len(newList) >4:
        newerW = " ".join(newList[:-2])
        newerW += "and "
        newerW += newList[-2] + " " + newList[-1]
        return newerW
    elif len(newList) == 4:
        print(newList)
        newSent = newList[0] + ", " + newList[1] + ", " + newList[2] + " and " + newList[3]
        return newSent

    return newW



print(sentenceMaker(single(0)))

print(3600 * 24 * 365)
