def add_time(start, duration, *args):
    new_time = ""
    l = len(args)
    days_list = ["SUNDAY", "MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY"]
    start_list_am_pm = start.split()
    start_list = start_list_am_pm[0].split(":")
    if start_list_am_pm[1] == "PM":
        start_time_in_min = (int(start_list[0]) + 12) * 60 + int(start_list[1])
    else:
        start_time_in_min = int(start_list[0]) * 60 + int(start_list[1])
    duration_list = duration.split(":")
    duration_min = int(duration_list[0]) * 60 + int(duration_list[1])
    total_time_min = start_time_in_min + duration_min
    total_hrs = total_time_min % 720
    am_pm = total_time_min // 720
    total_days = total_time_min / 1440
    total_days_rounded = int(total_days)
    hh = int(total_hrs / 60)
    if hh == 0:
        hh = hh + 12
    mm = total_hrs % 60
    if mm < 10:
        mm = "0" + str(mm)
    else:
        mm = str(mm)
    new_time_list = [str(hh), ":", mm]
    if am_pm % 2 != 0:
        new_time_list.append("PM")
    else:
        new_time_list.append("AM")
    if l > 0:
        days = args[0]
        which_day = int(total_days % 7)
        index_days = days_list.index(days.upper())
        which_day = which_day + index_days
        if which_day >= 7:
            which_day = which_day - 7
        day_name = days_list[which_day]
        new_time_list.append(day_name.capitalize())

    if total_days_rounded > 1:
        days_later = str(total_days_rounded) + " days later"
        new_time_list.append(days_later)
        if l > 0:
            new_time = "{0}{1}{2}{3} {4}, {5} ({6})".format(new_time, new_time_list[0], new_time_list[1],
                                                            new_time_list[2],
                                                            new_time_list[3], new_time_list[4], new_time_list[5])
        else:
            new_time = "{0}{1}{2}{3} {4} ({5})".format(new_time, new_time_list[0], new_time_list[1],
                                                       new_time_list[2],
                                                       new_time_list[3], new_time_list[4])
    elif total_days_rounded == 1:
        days_later = "next day"
        new_time_list.append(days_later)
        if l > 0:
            new_time = "{0}{1}{2}{3} {4}, {5} ({6})".format(new_time, new_time_list[0], new_time_list[1],
                                                            new_time_list[2],
                                                            new_time_list[3], new_time_list[4], new_time_list[5])
        else:
            new_time = "{0}{1}{2}{3} {4} ({5})".format(new_time, new_time_list[0], new_time_list[1],
                                                       new_time_list[2],
                                                       new_time_list[3], new_time_list[4])
    elif total_days_rounded == 0:
        if l > 0:
            new_time = "{0}{1}{2}{3} {4}, {5}".format(new_time, new_time_list[0], new_time_list[1],
                                                      new_time_list[2],
                                                      new_time_list[3], new_time_list[4])
        else:
            new_time = "{0}{1}{2}{3} {4}".format(new_time, new_time_list[0], new_time_list[1],
                                                 new_time_list[2],
                                                 new_time_list[3])

    else:
        new_time = new_time + new_time_list[0] + new_time_list[1] + new_time_list[2] + " " + new_time_list[3]
    return new_time


s = "3:30 PM"
d = "2:12"
print(add_time(s, d, "Monday"))
