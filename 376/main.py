from sys import maxsize

def get_nearest_coin(start_pos, coins):
    if not start_pos or not coins:
        return -1
    min_distance = maxsize
    nearest_coin = None
    for c in coins:
        abs_x = abs(start_pos[0] - c[0])
        abs_y = abs(start_pos[1] - c[1])
        sum_of_coordinates = abs_x + abs_y
        if sum_of_coordinates < min_distance:
            nearest_coin = (c[0], c[1])
            min_distance = sum_of_coordinates
    return nearest_coin


if __name__ == '__main__':
    assert (0, 4) == get_nearest_coin((0, 2), [(0, 4), (1, 0), (2, 0), (3, 2)])
