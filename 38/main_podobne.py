# moje rozwiazanie do tego:
# https://www.geeksforgeeks.org/find-itinerary-from-a-given-list-of-tickets/

def helper(directions, curr):
    if not directions:
        return True
    for i in range(0, len(directions)):
        if curr[1] == directions[i][0]:
            new_directions = directions[:i] + directions[i + 1:]
            return True if not new_directions else helper(new_directions, directions[i])
    return not directions


def is_itinerary(directions):
    if not directions:
        return True
    for i in range(0, len(directions)):
        curr_directions = directions[:i] + directions[i + 1:]
        if helper(curr_directions, directions[i]):
            return True
    return False


if __name__ == '__main__':
    assert is_itinerary([['c', 'a'], ['b', 'c'], ['a', 'd']])
    assert not is_itinerary([['c', 'a'], ['b', 'c'], ['a', 'd'], ['e', 'f']])
    assert is_itinerary([['c', 'a'], ['b', 'c'], ['a', 'd'], ['d', 'b']])
