

def convert_unit(value, unit_in, unit_out):
    conversion_rates = {
        "feet": {"meters": 0.3048},
        "inches": {"meters": 0.0254},
        "kilometers": {"meters": 1000},
        "meters":
                {
                    "feet": 3.2808399,
                    "inches": 0.0254,
                    "kilometers": 0.001,
                    "meters": 1,
                    "miles": 0.000621371192,
                    "yards": 1.0936133                             
                },
        "miles": {"meters": 1609.344},
        "yards": {"meters": 0.9144}
    }

    meters = conversion_rates[unit_in]["meters"] * value
    new_value = meters * conversion_rates["meters"][unit_out]

    return new_value

print(convert_unit(100,'kilometers','inches'))