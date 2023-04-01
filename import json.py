import csv
import json
from IPython.display import display, HTML


def flatten_json(json_obj, delimiter='_'):
    flattened_dict = {}

    def flatten(obj, name=''):
        if isinstance(obj, dict):
            for key, value in obj.items():
                flatten(value, name + key + delimiter)
        elif isinstance(obj, list):
            for i, item in enumerate(obj):
                flatten(item, name + str(i) + delimiter)
        else:
            flattened_dict[name[:-1]] = obj

    flatten(json_obj)
    return flattened_dict


# Open the JSON file and load its contents
with open('JSONTOCSV.json', 'r', encoding='utf-8') as json_file:
    data = json.load(json_file)

# Display the data in a tabular form using IPython
headers = [key for key in flatten_json(data['data'][0]).keys()]
rows = [[str(value) for value in flatten_json(obj).values()]
        for obj in data['data']]
display(
    HTML('<table><thead><tr>{}</tr></thead><tbody>{}</tbody></table>'.format(
        '<th>' + '</th><th>'.join(headers) + '</th>', ''.join([
            '<tr><td>{}</td></tr>'.format('</td><td>'.join(row))
            for row in rows
        ]))))

# Open the CSV file in write mode and write the headers
with open('JSONTOCSV.csv', 'w', encoding='utf-8', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(headers)

    # Write the data to the CSV file
    for obj in data['data']:
        row = [flatten_json(obj).get(header, '') for header in headers]
        
        writer.writerow(row)

## CORRECT CODE ABOVE











