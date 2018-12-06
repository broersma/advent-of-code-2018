import little_helper


def distance(coord, x,y ):
    return abs(coord[0] - x) + abs(coord[1] - y)


def answer(input):
    lines = input.split('\n')

    coords = []
    for line in lines:
        x,y = line.split(', ')
        x = int(x)
        y = int(y)
        coords.append((x,y))

    minx = min(c[0] for c in coords)
    miny = min(c[1] for c in coords)
    maxx = max(c[0] for c in coords)
    maxy = max(c[1] for c in coords)

    req_dist = 10000

    desired_region = set()
    for x in range(minx, maxx):
        for y in range(miny, maxy):
            sum_dist = 0
            for coord in coords:
                sum_dist += distance(coord, x, y)
                if sum_dist >= req_dist:
                    break
            if sum_dist < req_dist:
                desired_region.add((x,y))
    return len(desired_region)


if __name__ == '__main__':
    print(answer(little_helper.get_input(6)))
