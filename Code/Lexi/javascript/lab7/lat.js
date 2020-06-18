function format_lat_long(latitude, longitude) {
    let r = '';
    if (latitude < 0) {
        r += (-latitude)+'S';
    } else{
        r += latitude+'N';
    }
    r += ',';
    if (longitude < 0) {
        r += (-longitude)+'W';
    } else{
        r += longitude+'E';
    }
    return r;
}