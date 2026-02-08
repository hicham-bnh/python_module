def ft_count_harvest_recursive(day=1, last_day=None):
    if (last_day is None):
        last_day = int(input("Days until harvest: "))
    if day <= last_day:
        print("Day", day)
        return (ft_count_harvest_recursive(day + 1, last_day))
    else:
        print("Harvest time!")
