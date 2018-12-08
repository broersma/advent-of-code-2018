import little_helper

from collections import defaultdict


def distance(coord, x,y ):
    return abs(coord[0] - x) + abs(coord[1] - y)


def is_finite(coord, coords):
    return coord[0] > min(c[0] for c in coords) and coord[1] > min(c[1] for c in coords) and coord[0] < max(c[0] for c in coords) and coord[1] < max(c[1] for c in coords)


def answer(input):
    lines = input.split('\n')

    coords = []
    for line in lines:
        x,y = line.split(', ')
        x = int(x)
        y = int(y)
        coords.append((x,y))

    minx = min(c[0] for c in coords) - 1
    miny = min(c[1] for c in coords) - 1
    maxx = max(c[0] for c in coords) + 2
    maxy = max(c[1] for c in coords) + 1

    areas = dict()
    
    for x in range(minx, maxx):
        for y in range(miny, maxy):
            min_dist = 10000
            min_dist_area = -1
            for i, coord in enumerate(coords):
                dist = distance(coord, x, y)
                if dist == min_dist:
                     min_dist_area = -1
                elif dist < min_dist:
                    min_dist = dist
                    min_dist_area = i
            areas[(x,y)] = min_dist_area

    area_size = defaultdict(int)
    for area in areas:
        if is_finite(area, coords):
            area_size[areas[area]] +=1

    return max(area_size.values())


if __name__ == '__main__':
    print(answer(little_helper.get_input(6)))
