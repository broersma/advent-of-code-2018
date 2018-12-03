import little_helper

def contains(claim, x, y):
    return claim[0] <= x < claim[0] + claim[2] and claim[1] <= y < claim[1] + claim[3]

def answer(input):
    """
    >>> answer("#1 @ 1,3: 4x4\\n#2 @ 3,1: 4x4\\n#3 @ 5,5: 2x2")
    4
    """
    claims = []
    for claim in input.split("\n"):
        b = claim.split(" @ ")[1]
        r = b.split(": ")
        x, y = r[0].split(",")
        w, h = r[1].split("x")
        claims.append((int(x),int(y),int(w),int(h)))
    
    taken = set()
    overlaps = set()
    for i, ca in enumerate(claims):
        for x in range(ca[0], ca[0]+ca[2]):
            for y in range(ca[1], ca[1]+ca[3]):
                if (x,y) in taken:
                    overlaps.add((x,y))
                taken.add((x,y))

    return len(overlaps)


if __name__ == '__main__':
    input = little_helper.get_input(3)
    print(answer(input))