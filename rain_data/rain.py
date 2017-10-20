from datetime import datetime
from pprint import pprint

if __name__ == '__main__':
    with open('sample.rain') as f:
        raw_rain_data = f.readlines()
        raw_rain_data = [line.strip() for line in raw_rain_data]

    for index, line in enumerate(raw_rain_data):
        if set(line) == set('-'):
            raw_rain_data = raw_rain_data[index + 1::]
            break

    data_points = list()

    for data_point in raw_rain_data:
        data = data_point.split(' ')
        data = [item for item in data if item is not '']
        # print(data)

        if '-' in data:
            # print(f'Invalid rain data for {data[0]}!')
            continue

        data_points.append((data[0], int(data[1])))

    # print(max(data_points, key=lambda d: d[1]))

# Advanced
    rainfall = dict()

    for data_point in data_points:
        year = datetime.strptime(data_point[0], '%d-%b-%Y').year
        if rainfall.get(year):
            rainfall[year].append(data_point)
        else:
            rainfall[year] = [data_point]
    # print(rainfall.keys())


    for year, data_point in rainfall.items():
        rain_total = sum(year[1] for year in data_point)
        rainfall[year] = rain_total
        print(rain_total)
    rainiest_year = max(rainfall.items(), key=lambda x: x[1])
    print(rainiest_year)
