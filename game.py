import random

#city zones and possible items
zones = {
    "Central Park": ["power cell", "short circuit", "battery pack"],
    "Industrial Area": ["power cell", "short circuit"],
    "Residential Zone": ["battery pack", "short circuit"],
    "Downtown": ["power cell", "battery pack"]
}

#Robot properties
battery = 100
collected_power_cells = 0
total_power_cells = 5

#move zone function
def move_to_zone(zone):
    global battery
    if zone in zones:
        item = random.choice(zones[zone])
        print(f'\nYou have moved to {zone} and found a {item}')
        print('Map: ')
        if zone == 'Central Park':
            print('_________________________________')
            print('|Central Park:  |Residential:   |')
            print('|       !       |               |')
            print('|               |               |')
            print('|---------------|---------------|')
            print('|Industrial:    |Downtown:      |')
            print('|               |               |')
            print('|_______________|_______________|')
        elif zone == 'Industrial Area':
            print('_________________________________')
            print('|Central Park:  |Residential:   |')
            print('|               |               |')
            print('|               |               |')
            print('|---------------|---------------|')
            print('|Industrial:    |Downtown:      |')
            print('|        !      |               |')
            print('|_______________|_______________|')
        elif zone == 'Residential Zone':
            print('_________________________________')
            print('|Central Park:  |Residential:   |')
            print('|               |       !       |')
            print('|               |               |')
            print('|---------------|---------------|')
            print('|Industrial:    |Downtown:      |')
            print('|               |               |')
            print('|_______________|_______________|')
        elif zone == 'Downtown':
            print('_________________________________')
            print('|Central Park:  |Residential:   |')
            print('|               |               |')
            print('|               |               |')
            print('|---------------|---------------|')
            print('|Industrial:    |Downtown:      |')
            print('|               |       !       |')
            print('|_______________|_______________|')
        if battery >= 10:
            battery -= 10
        else: battery = 0
        return item
    else:
        print(f'\n{zone} is an invalid zone, please enter another value')
        return None

#collect items function
def collect_item(item):
    global battery, collected_power_cells
    if item == 'power cell':
        collected_power_cells += 1
        print(f'you have collected a power cell. {total_power_cells - collected_power_cells} more power cells to collect.') 
    if item == 'short circuit':
        if battery >= 30:
            battery -= 30
        else: battery = 0
        print(f'you have found a short circuit. battery drained by 30%')
    if item == 'battery pack':
        if battery <= 70:
            battery += 30
        else: battery = 100
        print(f'you found a battery pack. Battery charged by 30%')
    
#display inventory function
def display_inventory():
    print(f'Inventory: {collected_power_cells} power cells')

#game loop
while battery > 0 and collected_power_cells < total_power_cells:
    print('\nMove to a zone and collect 5 power cells before running out of battery to win. Each travel costs 10 percent of the robot battery')
    print(f'Robot Battery : {battery}%')
    print(f'Available zones: {list(zones.keys())}')
    
    zone = input('Enter a zone: ')
    item = move_to_zone(zone)
    collect_item(item)
    display_inventory()
    if battery == 0:
        print('Your battery has run out. Game over')
if collected_power_cells == total_power_cells:
    print('Congratulations, You Win!')
    
