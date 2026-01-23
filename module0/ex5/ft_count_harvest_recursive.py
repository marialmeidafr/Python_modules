def ft_count_harvest_recursive():
    max_days = int(input("Days until harvest: "))

    def count_days(days):
        if days > max_days:
            return
        print("Day", days)
        count_days(days + 1)
    count_days(1)
    print("Harvest time!")
