import little_helper

from collections import defaultdict

def contains(claim, x, y):
    return claim[0] <= x < claim[0] + claim[2] and claim[1] <= y < claim[1] + claim[3]

def answer(input):
    """
    >>> answer("#1 @ 1,3: 4x4\\n#2 @ 3,1: 4x4\\n#3 @ 5,5: 2x2")
    3
    """
    claims = []
    for claim in input.split("\n"):
        id = claim.split(" @ ")[0][1:]
        b = claim.split(" @ ")[1]
        r = b.split(": ")
        x, y = r[0].split(",")
        w, h = r[1].split("x")
        claims.append((int(x),int(y),int(w),int(h),int(id)))
    
    taken = defaultdict(int)
    for ca in claims:
        has_overlaps = False
        for x in range(ca[0], ca[0]+ca[2]):
            for y in range(ca[1], ca[1]+ca[3]):
                taken[(x,y)] += 1

    for ca in claims:
        has_overlaps = False
        for x in range(ca[0], ca[0]+ca[2]):
            for y in range(ca[1], ca[1]+ca[3]):
                if taken[(x,y)] > 1:
                    has_overlaps = True
        if not has_overlaps:
            return ca[4]


if __name__ == '__main__':
    input = little_helper.get_input(3)
    print(answer(input))