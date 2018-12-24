import little_helper

# defaultdict(list), defaultdict(int), deque.rotate/append
from collections import defaultdict, deque
# functools.reduce(function, iterable[, initializer])
from functools import reduce
# islice(seq, [start,] stop [, step])
from itertools import islice, product
import re
import networkx as nx
#from numba import jit
from sys import exit,stdout

import queue

day = 23
if __file__.endswith("_2.py"):
    m = __import__(str(day) + "_1")

def distance(a,b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1]) + abs(a[2] - b[2])
    
def in_range(a, b):
    dist = distance(a,b)
    
    return dist <= a[3]

class Area:
    def __init__(self, nanobot):
        if isinstance(nanobot, set):
            self.bots = nanobot
        else:
            self.bots = set([nanobot])
    
    def contains(self, nanobot):
        """
        >>> a = Area((10,12,12,2))
        >>> a.contains((10,12,12,2))
        True
        >>> a.contains((10,11,12,2))
        False
        """
        return nanobot in self.bots
        
    def overlaps(self, nanobot):
        """
        >>> a = Area((0,0,0,0))
        >>> a.overlaps((0,0,1,0))
        False
        >>> a = Area((0,0,0,1))
        >>> a.overlaps((0,0,1,0))
        True
        >>> a = Area((0,0,0,1))
        >>> a.overlaps((1,1,1,1))
        False
        >>> a = Area((0,0,0,2))
        >>> a.overlaps((1,1,1,1))
        True
        """
        return all(distance(bot, nanobot) <= bot[3]+nanobot[3] for bot in self.bots)
    
    def combine(self, nanobot):
        """
        >>> a = Area((0,0,0,0))
        >>> x = a.combine((0,0,1,0))
        >>> x.bots
        {(0, 0, 0, 0), (0, 0, 1, 0)}
        """
        bots = self.bots
        bots.add(nanobot)
        return Area(bots)
        
    def get_size(self):
        return len(self.bots)
    
    def _get_coordinates(bot):
        """
        >>> list(Area._get_coordinates((0,0,0,0)))
        [(0, 0, 0, 0)]
        >>> set(Area._get_coordinates((0,0,0,1))) == set([(0,0,0,0), (0,1,0,0), (0,-1,0,0), (-1,0,0,0), (1,0,0,0), (0,0,-1,0), (0,0,1,0)])
        True
        """
        for (x, y, z) in product(range(bot[0]-bot[3], bot[0]+bot[3]+1), range(bot[1]-bot[3], bot[1]+bot[3]+1), range(bot[2]-bot[3], bot[2]+bot[3]+1)):
            if in_range(bot, (x,y,z,0)):
                yield (x,y,z,0)
    
    def get_coordinates(self):
        """
        >>> a = Area((0,0,0,0))
        >>> x = a.combine((0,0,1,0))
        >>> set(x.get_coordinates())
        set()
        >>> a = Area((0,0,0,1))
        >>> x = a.combine((0,0,1,1))
        >>> set(x.get_coordinates()) == {(0,0,0,0), (0,0,1,0)}
        True
        >>> a = Area((0,0,0,1))
        >>> x = a.combine((0,0,1,2))
        >>> set(x.get_coordinates()) > {(0,0,-1,0), (0,0,0,0), (0,0,1,0), (0,1,0,0),(-1,0,0,0) }
        True
        """
        return reduce(set.intersection, (set(Area._get_coordinates(bot)) for bot in self.bots))
        
    def __str__(self):
        return str(len(self.bots))
def answer1(bots):
    q = queue.Queue()
    for bot in bots:
        q.put(Area(bot))
    
    max_size = 0
    max_area = None
    while not q.empty():
        a = q.get()
        for bot in bots:
            if not a.contains(bot) and a.overlaps(bot):
                q.put(a.combine(bot))
        if a.get_size() > max_size:
            max_size = a.get_size()
            max_area = a
    return len(max_area.bots)
    #return min(distance(c, (0,0,0)) for c in max_area.get_coordinates())

def overlap(bot1, bot2):
    return distance(bot1, bot2) <= bot1[3]+bot2[3]
    
def get_max_clique(bots, optimize=True):
    if optimize:
        return [19, 66, 169, 173, 181, 245, 277, 405, 460, 468, 538, 541, 544, 551, 657, 660, 694, 700, 735, 744, 763, 861, 863, 918, 946, 960, 971, 977, 103, 191, 201, 216, 296, 304, 333, 358, 365, 367, 393, 434, 442, 487, 514, 547, 553, 554, 558, 569, 600, 652, 669, 671, 708, 746, 760, 808, 821, 871, 926, 969, 22, 51, 52, 95, 137, 471, 658, 703, 785, 900, 10, 146, 311, 459, 536, 698, 733, 759, 852, 404, 561, 454, 653, 788, 842, 227, 288, 635, 834, 954, 3, 20, 26, 27, 35, 84, 97, 186, 220, 267, 268, 356, 402, 426, 495, 529, 540, 630, 638, 714, 717, 753, 770, 787, 844, 851, 858, 882, 934, 950, 952, 965, 980, 194, 804, 932, 185, 223, 251, 407, 419, 428, 462, 479, 485, 590, 606, 632, 666, 747, 784, 799, 889, 893, 903, 924, 951, 973, 110, 156, 188, 324, 349, 435, 486, 582, 687, 704, 765, 810, 985, 5, 21, 90, 165, 253, 262, 263, 274, 390, 397, 430, 492, 502, 510, 533, 539, 583, 599, 603, 730, 750, 776, 798, 920, 923, 930, 968, 994, 4, 170, 178, 242, 287, 321, 371, 427, 563, 692, 722, 755, 777, 816, 975, 46, 55, 108, 187, 237, 239, 323, 329, 345, 376, 398, 401, 457, 490, 501, 515, 542, 579, 602, 762, 794, 818, 849, 891, 953, 981, 984, 48, 124, 346, 362, 369, 991, 998, 56, 81, 197, 229, 232, 244, 246, 258, 420, 436, 458, 508, 548, 586, 613, 615, 616, 643, 768, 848, 925, 995, 13, 24, 39, 60, 62, 74, 89, 129, 142, 166, 215, 226, 231, 247, 281, 298, 322, 325, 339, 340, 355, 361, 363, 373, 375, 389, 392, 413, 425, 432, 441, 475, 504, 517, 524, 537, 564, 568, 581, 607, 611, 634, 651, 672, 712, 727, 758, 793, 809, 811, 817, 835, 840, 854, 856, 876, 886, 894, 896, 902, 929, 937, 967, 972, 990, 0, 7, 11, 23, 28, 33, 34, 42, 45, 49, 59, 64, 65, 67, 80, 85, 86, 94, 100, 102, 104, 112, 119, 128, 132, 134, 140, 144, 147, 164, 168, 171, 172, 175, 179, 182, 192, 205, 208, 213, 217, 238, 241, 243, 255, 257, 259, 260, 266, 270, 275, 297, 302, 308, 309, 312, 315, 330, 331, 334, 341, 348, 352, 353, 359, 366, 370, 372, 381, 382, 383, 384, 387, 399, 400, 406, 414, 424, 431, 438, 439, 440, 444, 447, 449, 455, 464, 465, 467, 470, 474, 478, 480, 481, 483, 519, 522, 523, 525, 531, 549, 557, 560, 562, 577, 585, 593, 596, 610, 619, 623, 624, 631, 633, 637, 641, 644, 647, 650, 659, 662, 673, 674, 675, 678, 680, 682, 686, 702, 711, 728, 732, 734, 743, 769, 774, 778, 779, 789, 796, 803, 805, 806, 812, 813, 815, 822, 823, 828, 836, 855, 865, 866, 868, 870, 874, 877, 878, 879, 880, 887, 890, 892, 895, 897, 899, 901, 904, 910, 911, 912, 913, 921, 927, 933, 941, 944, 955, 974, 979, 2, 6, 8, 9, 12, 14, 15, 16, 17, 18, 25, 29, 30, 31, 32, 36, 37, 38, 40, 41, 43, 44, 47, 50, 53, 54, 57, 58, 61, 63, 68, 69, 70, 71, 72, 73, 75, 76, 77, 78, 79, 82, 83, 88, 91, 92, 93, 96, 98, 99, 101, 105, 106, 107, 109, 111, 113, 114, 115, 116, 117, 118, 120, 121, 122, 123, 125, 127, 131, 133, 135, 136, 138, 139, 141, 143, 145, 148, 149, 150, 151, 152, 153, 154, 155, 158, 159, 160, 161, 162, 163, 167, 174, 176, 177, 180, 183, 184, 189, 190, 193, 195, 196, 198, 199, 200, 202, 203, 204, 209, 210, 211, 214, 218, 219, 221, 222, 224, 225, 228, 230, 233, 234, 235, 236, 240, 248, 249, 250, 252, 254, 512, 513, 516, 518, 520, 521, 526, 527, 528, 530, 534, 535, 543, 545, 546, 550, 552, 556, 559, 565, 566, 567, 570, 571, 572, 573, 574, 575, 576, 578, 580, 584, 587, 588, 589, 591, 592, 594, 595, 597, 598, 601, 604, 605, 608, 609, 612, 614, 617, 618, 620, 621, 622, 625, 626, 627, 628, 629, 636, 639, 640, 642, 646, 648, 649, 654, 655, 656, 661, 663, 664, 665, 667, 668, 670, 676, 677, 679, 681, 683, 684, 685, 688, 689, 690, 691, 693, 695, 696, 697, 699, 701, 705, 706, 707, 709, 710, 713, 715, 716, 718, 719, 721, 723, 724, 725, 726, 729, 731, 736, 738, 739, 740, 741, 742, 745, 749, 751, 752, 754, 756, 757, 761, 764, 766, 767, 256, 771, 261, 773, 775, 264, 265, 780, 269, 781, 782, 271, 783, 272, 273, 786, 276, 278, 790, 279, 792, 280, 282, 795, 283, 284, 285, 797, 286, 800, 289, 801, 290, 802, 291, 292, 293, 294, 295, 807, 299, 301, 814, 303, 305, 306, 307, 319, 831, 830, 819, 820, 310, 824, 313, 825, 314, 826, 827, 316, 829, 317, 318, 320, 832, 833, 837, 326, 839, 327, 328, 841, 843, 332, 845, 846, 847, 335, 336, 337, 338, 850, 853, 342, 343, 344, 857, 347, 859, 860, 862, 350, 351, 864, 354, 867, 357, 869, 360, 872, 873, 875, 364, 368, 881, 883, 885, 374, 377, 378, 379, 380, 385, 386, 898, 388, 391, 905, 394, 906, 395, 907, 908, 909, 914, 915, 403, 916, 917, 919, 409, 922, 410, 411, 412, 415, 416, 928, 417, 418, 931, 421, 422, 423, 935, 936, 938, 939, 940, 429, 942, 943, 445, 433, 945, 947, 948, 437, 949, 443, 956, 957, 958, 446, 959, 448, 961, 962, 450, 451, 963, 964, 452, 453, 966, 456, 970, 461, 463, 976, 466, 978, 469, 983, 472, 473, 986, 987, 476, 988, 477, 989, 993, 482, 484, 996, 997, 999, 488, 489, 491, 493, 494, 496, 497, 498, 499, 500, 503, 505, 506, 507, 509, 511]

    overlaps = defaultdict(list)
        
    bot_ids = range(len(bots))
    
    for bot1 in bot_ids:
        for bot2 in bot_ids:
            if bot1 != bot2 and overlap(bots[bot1], bots[bot2]):
                overlaps[bot1].append(bot2)
    
    G = nx.Graph()
    for bot_id1 in overlaps:
        for bot_id2 in overlaps[bot_id1]:
            G.add_edge(bot_id1, bot_id2)
    
    return max(nx.find_cliques(G), key=lambda c: len(c))


def answer(input):
    lines = input.split('\n')
    bots = []
    for line in lines:
        if line == "":
            break
        m = re.search(r"pos=<(-?\d+),(-?\d+),(-?\d+)>, r=(\d+)",line)
        x,y,z,r = (int(w) for w in m.groups())
        bots.append((x,y,z,r))
    
    max_clique =  get_max_clique(bots)
    
    events_x = get_events(bots, max_clique, 0)
    events_y = get_events(bots, max_clique, 1)
    events_z = get_events(bots, max_clique, 2)
    len_max_clique = len(max_clique)
    
    for bot_id2 in max_clique:
        print(bot_id2, sum(1 if overlap(bots[bot_id], bots[bot_id]) else 0 for bot_id in max_clique))
    return 
    potentially_overlapping_x = set()
    for event_x in events_x:
        x = event_x[0]
        add_x = event_x[1]
        bot_x = event_x[2]
        if add_x:
            potentially_overlapping_x.add(bot_x)
        
        if len(potentially_overlapping_x) == len_max_clique:
            potentially_overlapping_y = set()
            for event_y in events_y:
                y = event_y[0]
                add_y = event_y[1]
                bot_y = event_y[2]
                if add_y:
                    potentially_overlapping_y.add(bot_y)
                
                if len(potentially_overlapping_y) == len_max_clique:
                    potentially_overlapping_z = set()
                    for event_z in events_z:
                        z = event_z[0]
                        add_z = event_z[1]
                        bot_z = event_z[2]
                        if add_z:
                            potentially_overlapping_z.add(bot_z)
                        
                        if len(potentially_overlapping_z) == len_max_clique:
                            for dz in range(bots[bot_z][3]*2+1):
                                point = (x, y, z+dz, 0)
                                if all(overlap(point, bots[bot_id]) for bot_id in max_clique):
                                    print(point, "yes!", distance(point, (0,0,0)))
                                    stdout.flush()
                        if not add_z:
                            potentially_overlapping_z.remove(bot_z)
                if not add_y:
                    potentially_overlapping_y.remove(bot_y)
        if not add_x:
            potentially_overlapping_x.remove(bot_x)

def get_events(bots, bot_ids, axis):
    """
    >>> bots = [(0,0,0,1), (5,0,0,3)]
    >>> get_events(bots, [0, 1], 0)
    [(-1, True, 0), (1, False, 0), (2, True, 1), (8, False, 1)]
    >>> get_events(bots, [0, 1], 1)
    [(-3, True, 1), (-1, True, 0), (1, False, 0), (3, False, 1)]
    >>> bots = [(0,0,0,0)]
    >>> get_events(bots, [0], 1)
    [(0, True, 0), (0, False, 0)]
    """
    events = []
    for bot_id in bot_ids:
        bot = bots[bot_id]
        events.append((bot[axis] + bot[3], False, bot_id))
        events.append((bot[axis] - bot[3], True, bot_id))
    return sorted(events, key=lambda e: (e[0], not e[1]))

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('level', type=int, default=-1, nargs='?')
    args = parser.parse_args()
    level = args.level

    input = little_helper.get_input(day)
    the_answer = answer(input)

    if level == -1:
        print(the_answer)
    else:
        print("Submitting", the_answer, "for day", day,"star", level)
        print(little_helper.submit(the_answer, level, day))
