from secrets import choice
import requests

def get_element():
    element_list = []
    selection = input('Would you like to select by (a)tomic number, (c)ategory, or (n)name?:/n')
    if selection.lower() == 'a':
        filter_by = 'number'
    elif selection.lower() == 'c':
        filter_by = 'category'
    elif selection.lower() == 'n':
        filter_by = 'name'

    msg = 'Type in your chosen ' + filter_by
    selection_choice = input(msg)

    for element in elements:
        temp_categories = str(element[filter_by]).split()
        if selection_choice in temp_categories:
            element_list.append(element['name'])

    print(element_list)

def get_element_data():
    DATA_URL = 'https://raw.githubusercontent.com/Bowserinator/Periodic-Table-JSON/master/PeriodicTableJSON.json'

    r = requests.get(DATA_URL)
    if r.status_code != requests.codes.ok:
        print('Error: ', r.status_code)

    raw_data = r.json()
    elements = raw_data['elements']
    element_categories = []
    element_name = []
    element_number = []

    for element in elements:
        element_name.append(element['name'])
        element_number.append('number')
        temp_categories = element['category'].split()
        if temp_categories[0] == 'unknown,' and 'unknown' not in element_categories:
            element_categories.append('unknown')
        elif temp_categories[0] != 'unknown,':
            for category in temp_categories:
                if category not in element_categories:
                    element_categories.append(category)
    element_data = {
        'element_categories' : element_categories,
        'names' : element_name,
        'atomic_number' : element_number,
        'elements' : elements
    }
    return element_data


def get_electron_ring_data(elements):
    electron_ring_values = []
    for element in elements:
        electrons = element['electron_configuration'].split()
        electron_ring = []
        for ring in electrons:
            electron_ring.append(ring[2:])
        electron_ring_values.append(electron_ring)
    return electron_ring_values

my_data = get_element_data()
rings = get_electron_ring_data(my_data['elements'])
print(rings)