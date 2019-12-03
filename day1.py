file = open('./day1-input', 'r')
input = file.read().split('\n')

# Part 1
def module_fuel_calculator (module_mass):
    return (int(module_mass) // 3) - 2

def total_fuel_calculator (masses):
    sum = 0
    for mass in masses:
        sum += module_fuel_calculator(mass)
    return sum

print('Part 1 result: ', total_fuel_calculator(input))

# Part 2

def meta_fuel_calculator (masses):
    sum = 0

    for mass in masses:
        cur_fuel = module_fuel_calculator(mass)
        sum_module_fuel = cur_fuel

        while (module_fuel_calculator(cur_fuel) >= 0):
            cur_fuel = module_fuel_calculator(cur_fuel)
            sum_module_fuel += cur_fuel
        
        sum += sum_module_fuel

    return sum

print('Part 2 result: ', meta_fuel_calculator(input))
        

