def helper(directions, curr, curr_itinerary):
    if not directions:
        return True
    for i in range(len(directions)):
        if curr[1] == directions[i][0]:
            new_directions = directions[:i] + directions[i + 1:]
            curr_itinerary.append(curr[1])
            if not new_directions:
                curr_itinerary.append(directions[i][1])
                return curr_itinerary
            else:
                return helper(new_directions, directions[i], curr_itinerary)
    return curr_itinerary if not directions else None


def is_itinerary(directions, starting):
    if not directions:
        return True
    for i in range(len(directions)):
        if directions[i][0] == starting:
            curr_directions = directions[:i] + directions[i + 1:]
            curr_itinerary = [directions[i][0]]
            return helper(curr_directions, directions[i], curr_itinerary)
    return None


if __name__ == '__main__':
    result = is_itinerary([('SFO', 'HKO'), ('YYZ', 'SFO'), ('YUL', 'YYZ'), ('HKO', 'ORD')], 'YUL')
    assert len(result) == len(['YUL', 'YYZ', 'SFO', 'HKO', 'ORD']) and sorted(result) == sorted(
        ['YUL', 'YYZ', 'SFO', 'HKO', 'ORD'])
