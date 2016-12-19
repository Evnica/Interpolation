from interpolation.csvconverter import CsvConverter
from interpolation.iohelper import Writer


csv_converter = CsvConverter('../wetter.csv')
h = csv_converter(1, 2, 3, 4, 13, 15, 14)

writer = Writer('../tests/output/input_all.json')
# writer.initial_to_json_1phenomena(csv_converter, 2)
writer.initial_to_json(csv_converter)

lat_values = [(lat - csv_converter.lat_min) / (csv_converter.lat_max - csv_converter.lat_min)
              for lat in csv_converter.lat_values]
lon_values = [(lon - csv_converter.lon_min) / (csv_converter.lon_max - csv_converter.lon_min)
              for lon in csv_converter.lon_values]
alt_values = [(alt - csv_converter.alt_min) / (csv_converter.alt_max - csv_converter.alt_min)
              for alt in csv_converter.alt_values]

csv_converter.lat_values = lat_values
csv_converter.lon_values = lon_values
csv_converter.alt_values = alt_values

writer_norm = Writer('output/input_norm.json')
writer_norm.initial_to_json(csv_converter)

print('Ready')
