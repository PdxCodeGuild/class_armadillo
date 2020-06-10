const units = {
    ft: 0.3048,
    m: 1,
    mi: 1609.34,
    km: 1000,
    yd:  0.9144,
    in: 0.0254,

}

let num = prompt("enter a number: ")
let in_unit = prompt('enter a unit of measurement: ')
let out_unit = prompt('enter the unit of measurement youd like to convert i to: ')
let conversion = Math.abs(num * units[in_unit])

let new_conversion = Math.abs(conversion / units[out_unit])

let result = alert(`${num} ${in_unit} is equal to ${new_conversion} ${out_unit}` )
