




def standardize_units(units):
    unit_lists = [['m', 'meter', 'meters'],
             ['mi', 'mile', 'miles'],
             ['ft', 'feet'],
             ['km', 'kilometer', 'kilometers'],
             ['yd', 'yard', 'yards'],
             ['in', 'inch', 'inches']]
    for unit_list in unit_lists:
        if units in unit_list:
            return unit_list[0]
    return None



def convert(number_in, units_in, units_out):
    conversion = {
        'm': 1.0,
        'mi': 1609.34,
        'ft': 0.3048,
        'km': 1000,
        'yd': 0.9144,
        'in': 0.0254
    }
    return number_in*conversion[units_in]/conversion[units_out]


