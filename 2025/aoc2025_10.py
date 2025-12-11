# INCOMPLETE SOLUTION


MAX_CLICS = 1000 # max number of recursions_p1

class Machine:
    def __init__(self, pattern: list, buttons: list):
        self.goal = pattern
        self.buttons = buttons
        self.min_clicks = 9999999999

    def update_min_clicks(self, num_clicks):
        self.min_clicks = num_clicks if num_clicks < self.min_clicks else self.min_clicks

    def check_if_goal_is_reached_p1(self, active_pattern) -> bool:
        return ''.join(self.goal) == ''.join(active_pattern)

    def check_if_goal_is_reached_p2(self, active_pattern) -> bool:
        return self.goal == active_pattern

    def check_if_voltage_is_ok(self, active_pattern) -> bool:
        print(f"{self.goal} -> {active_pattern}")
        return all(l >= r for l, r in zip(self.goal , active_pattern))


def prepare_data_p1() -> list[Machine]:
    machines = []
    with open('data.csv') as f:
        for line in f:
            pattern = []
            buttons = []
            elements = line.split(' ')
            for e in elements:
                if e[0] == '[':
                    pattern = [s for s in e.replace('[','').replace(']','').replace(',','')]
                if e[0] == '(':
                    buttons.append([int(s) for s in e.replace('(','').replace(')','').replace(',','')])
            machines.append(Machine(pattern, buttons))
    return machines


def update_active_pattern_p1(machine, button_idx, current_pattern):
    new_pattern = list(current_pattern)
    for e in machine.buttons[button_idx]:
        if new_pattern[e] == '.':
            new_pattern[e] = '#'
        else:
            new_pattern[e] = '.'
    return new_pattern


def recursion_p1(machine, active_pattern, num_clicks, cache):
    state_key = ''.join(active_pattern)
    if state_key in cache and cache[state_key] <= num_clicks:
        return
    cache[state_key] = num_clicks

    if num_clicks >= MAX_CLICS:
        return

    if machine.check_if_goal_is_reached_p1(active_pattern):
        machine.update_min_clicks(num_clicks)
        return

    for b in range(len(machine.buttons)):
        new_pattern = update_active_pattern_p1(machine, b, active_pattern)
        recursion_p1(machine, new_pattern, num_clicks + 1, cache)


def solve_part_one() -> int:
    machines = prepare_data_p1()
    for machine in machines:
        active_pattern = ['.' for _ in range(len(machine.goal))]
        recursion_p1(machine, active_pattern, 0, {})
        print(machine.min_clicks)
    total = 0
    for machine in machines:
        total += machine.min_clicks
    print(total)

######## END PART 1 ########

def prepare_data_p2() -> list[Machine]:
    machines = []
    with open('data.csv') as f:
        for line in f:
            pattern = []
            buttons = []
            elements = line.split(' ')
            for e in elements:
                if e[0] == '{':
                    pattern = [int(s) for s in e.strip().replace('{','').replace('}','').replace(',','')]
                if e[0] == '(':
                    buttons.append([int(s) for s in e.replace('(','').replace(')','').replace(',','')])
            machines.append(Machine(pattern, buttons))
    return machines


def update_active_pattern_p2(machine, button_idx, current_pattern):
    new_pattern = list(current_pattern)
    for e in machine.buttons[button_idx]:
        new_pattern[e] += 1
    print(f"{current_pattern} -> {machine.buttons[button_idx]} -> {new_pattern}")
    return new_pattern


def recursion_p2(machine, active_pattern, num_clicks, cache):
    state_key = str(active_pattern)
    if state_key in cache and cache[state_key] <= num_clicks:
        return
    cache[state_key] = num_clicks
    if num_clicks >= MAX_CLICS:
        return
    if machine.check_if_goal_is_reached_p2(active_pattern):
        print("found!")
        machine.update_min_clicks(num_clicks)
        return
    for b in range(len(machine.buttons)):
        new_pattern = update_active_pattern_p2(machine, b, active_pattern)
        if not machine.check_if_voltage_is_ok(new_pattern):
            print("not ok")
            continue
        recursion_p2(machine, new_pattern, num_clicks + 1, cache)


def solve_part_two() -> int:
    machines = prepare_data_p2()
    for machine in machines:
        active_pattern = [0 for _ in range(len(machine.goal))]
        recursion_p2(machine, active_pattern, 0, {})
        print(machine.min_clicks)
    total = 0
    for machine in machines:
        total += machine.min_clicks
    print(total)


def main():
    # solve_part_one()
    solve_part_two()

if __name__ == "__main__":
    main()
