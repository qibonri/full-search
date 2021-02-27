def delta(d, top_longitude, top_lattitude):
    map_params = {
        "ll": ",".join([top_longitude, top_lattitude]),
        "spn": ",".join([d, d]),
        "l": "map",
        "pt": ",".join([top_longitude, top_lattitude, 'flag'])
    }
    return map_params
