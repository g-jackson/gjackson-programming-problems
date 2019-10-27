testinputs = [
  "[1518-11-01 00:00] Guard #10 begins shift",
  "[1518-11-01 00:05] falls asleep",
  "[1518-11-01 00:25] wakes up",
  "[1518-11-01 00:30] falls asleep",
  "[1518-11-01 00:55] wakes up",
  "[1518-11-01 23:58] Guard #99 begins shift",
  "[1518-11-02 00:40] falls asleep",
  "[1518-11-02 00:50] wakes up",
  "[1518-11-03 00:05] Guard #10 begins shift",
  "[1518-11-03 00:24] falls asleep",
  "[1518-11-03 00:29] wakes up",
  "[1518-11-04 00:02] Guard #99 begins shift",
  "[1518-11-04 00:36] falls asleep",
  "[1518-11-04 00:46] wakes up",
  "[1518-11-05 00:03] Guard #99 begins shift",
  "[1518-11-05 00:45] falls asleep",
  "[1518-11-05 00:55] wakes up"
]

def a(inputs):
    guards = {}
    for input in inputs:
        print(input)
        timestamp = int(input.split(']')[0][1:].split(' ')[-1].split(":")[1])
        #print(timestamp)
        if input.split(' ')[2] == "Guard":
            # New day, new guard
            guard_id = int(input.split(' ')[3][1:])
            # Add guard if new
            if guard_id not in guards:
                guards[guard_id] = [0]*60
            new_day = True
            asleep = False
        else:
            new_day = False

        if not new_day and not asleep:
            asleep = True
            sleep_time = timestamp
        elif not new_day and asleep:
            print(guard_id, sleep_time, timestamp)
            for i in range(sleep_time, timestamp):
                guards[guard_id][i] += 1
            asleep = False
            
    highest_sleep = 0
    sleepiest = 0
    for guard in guards:
        print(guard, guards[guard], sum(guards[guard]), guards[guard].index(max(guards[guard])))
        
        if sum(guards[guard]) > highest_sleep:
            sleepiest = guard
            highest_sleep = sum(guards[guard])
    print(sleepiest)
    result = sleepiest * guards[sleepiest].index(max(guards[sleepiest]))
    return result

def b(inputs):
    guards = {}
    for input in inputs:
        #print(input)
        timestamp = int(input.split(']')[0][1:].split(' ')[-1].split(":")[1])
        #print(timestamp)
        if input.split(' ')[2] == "Guard":
            # New day, new guard
            guard_id = int(input.split(' ')[3][1:])
            # Add guard if new
            if guard_id not in guards:
                guards[guard_id] = [0]*60
            new_day = True
            asleep = False
        else:
            new_day = False

        if not new_day and not asleep:
            asleep = True
            sleep_time = timestamp
        elif not new_day and asleep:
            print(guard_id, sleep_time, timestamp)
            for i in range(sleep_time, timestamp):
                guards[guard_id][i] += 1
            asleep = False
            
    highest_sleep_minute = 0
    highest_sleep_guard = 0
    for guard in guards:
        #print(guard, guards[guard], sum(guards[guard]), guards[guard].index(max(guards[guard])))
        
        if max(guards[guard]) > highest_sleep_minute:
            highest_sleep_guard = guard
            highest_sleep_minute = max(guards[guard])
    # print(highest_sleep_guard, highest_sleep_minute, max(guards[highest_sleep_guard]))
    result = highest_sleep_guard * guards[highest_sleep_guard].index(max(guards[highest_sleep_guard]))
    return result


with open('inputs/04in.txt', 'r') as infile:
    inputs = infile.read()
inputs = inputs.split("\n")
inputs.sort()


#print(a(inputs))
print(b(inputs))
