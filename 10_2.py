import little_helper

day = 10
if __file__.endswith("_2"):
    m = __import__(day + "_1")
    
def show(lights, min_x, max_x, min_y, max_y):
    
    for y in range(min_y, max_y+1):
        for x in range(min_x, max_x+1):
            if [x,y] in (light.position for light in lights):
                print('#', end='')
            else:
                print('.', end='')
        print()

def area(lights):
    min_x = min(light.position[0] for light in lights)
    max_x = max(light.position[0] for light in lights)
    min_y = min(light.position[1] for light in lights)
    max_y = max(light.position[1] for light in lights)
    
    return (max_x - min_x) * (max_y - min_y)

def move(lights):
    for light in lights:
        light.move()
        
def reverse(lights):
    for light in lights:
        light.reverse()
        
class Light:
    def __init__(self, position, velocity):
        self.position = position
        self.velocity = velocity
    
    def move(self):
        self.position[0] += self.velocity[0]
        self.position[1] += self.velocity[1]
    
    def reverse(self):
        self.position[0] -= self.velocity[0]
        self.position[1] -= self.velocity[1]
        
def answer(input):
    lines = input.split('\n')
    lights = []
    for line in lines:
        match = re.match(r'position=<(.*?),(.*?)> velocity=<(.*?),(.*?)>', line)
        position_x = int(match[1])
        position_y = int(match[2])
        velocity_x = int(match[3])
        velocity_y = int(match[4])
        position = [position_x,position_y]
        velocity = [velocity_x,velocity_y]
        lights.append(Light(position, velocity))
    
    min_area = area(lights)
    seconds = 0
    while True:
        move(lights)
        current_area = area(lights)
        if current_area > min_area:
            reverse(lights)
            return seconds
        else:
            min_area = current_area
        seconds += 1

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
