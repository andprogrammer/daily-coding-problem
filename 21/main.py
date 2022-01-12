def overlap(x, y):
    if not x or not y or len(x) < 2 or len(y) < 2:
        return False
    if (y[1] > x[0] > y[0]) or (y[0] < x[1] < y[1]) or (x[0] < y[0] and x[1] > y[1]) or (x[0] > y[0] and x[1] < y[1]):
        return True
    return False


def min_num_of_rooms(hours):
    if not hours:
        return 0
    rooms = [[hours[0]]]
    for i in range(1, len(hours)):
        curr_hour = hours[i]
        already_added = False
        for r in rooms:
            hour_not_overlap = True
            for j in r:
                if overlap(curr_hour, j):
                    hour_not_overlap = False
            if hour_not_overlap:
                r.append(curr_hour)
                already_added = True
                break
        if not already_added:
            rooms.append([curr_hour])
    return len(rooms)


if __name__ == '__main__':
    assert overlap((30, 75), (0, 50)) == True
    assert overlap((0, 50), (60, 150)) == False
    assert overlap((30, 55), (60, 150)) == False
    hours = [(30, 75), (0, 50), (60, 150)]
    assert min_num_of_rooms(hours) == 2
