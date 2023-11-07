import json

with open(r'tests.json') as json_data:
    tests = json_data.read()

with open(r'values.json') as json_data:
    values = json_data.read()

parsed_tests = json.loads(tests)
parsed_values = json.loads(values)


def recursive_search(d, i, v):
    for key, value in d.items():
        if type(value) == list:
            for i_item in value:
                if type(i_item) == dict:
                    if i_item['id'] == i:
                        i_item['value'] = v
                        return d
                    recursive_search(i_item, i, v)


for i in parsed_values.values():
    for j in i:
        recursive_search(parsed_tests, j['id'], j['value'])

with open('report.json', 'w') as f:
    json.dump(parsed_tests, f)

