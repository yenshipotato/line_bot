import datetime

slut_normal = [30, 31, 30, 31, 30, 32, 31, 27, 32, 30, 31, 30]
slut_leap = [30, 31, 30, 31, 30, 32, 31, 28, 32, 30, 31, 30]

years = 2022


def strtslut(s: str):
    s = s[s.index("_")+2:]
    list = s.split('/')
    return str(to_slut(int(list[0]), int(list[1]), int(list[2])))


def to_slut(Y: int, M: int, D: int):

    date_original = datetime.date(Y, M, D)
    date_leap = (datetime.date(Y, 3, 1).strftime("%j") == "061")

    day_count = int(date_original.strftime("%j"))

    if date_leap:
        day_list = slut_leap
        print("leap")
    else:
        day_list = slut_normal

    for m in range(0, 12):
        if day_count <= day_list[m]:
            days_slut = day_count
            months_slut = m+1
            return(Y, months_slut, days_slut)
        else:
            day_count -= day_list[m]


if __name__ == "__main__":
    s = ("slut_ 2022/2/23")

    print(strtslut(s))
