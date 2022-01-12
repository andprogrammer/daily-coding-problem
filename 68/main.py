def get_all_possible_positions(bishop, size):
    curr_x = bishop[0]
    curr_y = bishop[1]
    possible_positions = []
    while curr_x >= 0 and curr_y >= 0:
        possible_positions.append((curr_x, curr_y))
        curr_x -= 1
        curr_y -= 1
    curr_x = bishop[0] - 1
    curr_y = bishop[1] + 1
    while curr_x >= 0 and curr_y < size:
        possible_positions.append((curr_x, curr_y))
        curr_x -= 1
        curr_y += 1
    curr_x = bishop[0] + 1
    curr_y = bishop[1] + 1
    while curr_x < size and curr_y < size:
        possible_positions.append((curr_x, curr_y))
        curr_x += 1
        curr_y += 1
    curr_x = bishop[0] + 1
    curr_y = bishop[1] - 1
    while curr_x < size and curr_y >= 0:
        possible_positions.append((curr_x, curr_y))
        curr_x += 1
        curr_y -= 1
    return possible_positions


def get_intersections(bishops_pos, size):
    if not bishops_pos:
        return 0
    positions = []
    for bishop in bishops_pos:
        positions.append(get_all_possible_positions(bishop, size))
    intersections = 0
    # for i in positions:
    #     print(i)

    for x in range(len(positions) - 1):
        for y in range(x + 1, len(positions)):
            if x != y:
                if list(set(positions[x]) & set(positions[y])):
                    # print(x, y)
                    intersections += 1
    return intersections


if __name__ == '__main__':
    bishops_pos = [(0, 0),
                   (1, 2),
                   (2, 2),
                   (4, 0)]
    size = 5
    print(get_intersections(bishops_pos, size))     # wynik 3 i tak mi sie wydaje ze powinno byc