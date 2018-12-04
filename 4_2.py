import little_helper

from collections import defaultdict
import re

def answer(input):
    records = []
    current_guard = -1
    for line in input.split("\n"):
        match = re.match(r'\[(\d{4})-(\d\d)-(\d\d) (\d\d):(\d\d)\].*?', line)
        record = {'y': int(match[1]), 'M': int(match[2]), 'd': int(match[3]), 'h': int(match[4]), 'm': int(match[5])}
        match = re.search(r'Guard #(\d+) begins shift', line)
        if match:
            current_guard = int(match[1])
            action = 'begin'
        else:
            current_guard = -1
            if line.endswith('asleep'):
                action = 'sleep'
            else:
                action = 'wake'
        record['g'] = current_guard
        record['a'] = action
        records.append(record)
    
    records = sorted(records, key=lambda r: (r['y'], r['M'], r['d'], r['h'], r['m']))
    for record in records:
        if record['g'] == -1:
            record['g'] = current_guard
        else:
            current_guard = record['g']
        
    asleep = defaultdict(int)
    asleep_minute = defaultdict(int)
    start_sleep = None
    for record in records:
        current_guard = record['g']
        if record['a'] == 'sleep':
            start_sleep = record['m']
        elif record['a'] == 'wake':
            asleep[record['g']] += record['m'] - start_sleep
            for m in range(start_sleep, record['m']):
                if record['g'] == 10:
                    print(m)
                asleep_minute[(record['g'], m)] += 1
            start_sleep = None
    guard = max(asleep, key=asleep.get)
    
    max_sleep_guard = -1
    max_sleep_minute = -1
    max_sleep = -1
    for g, m in asleep_minute:
        if asleep_minute[(g,m)] > max_sleep:
            max_sleep = asleep_minute[(g,m)]
            max_sleep_minute = m
            max_sleep_guard = g
    return max_sleep_guard * max_sleep_minute


if __name__ == '__main__':
    input = little_helper.get_input(4)
    print(answer(input))
