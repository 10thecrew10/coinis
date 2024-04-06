import json
#
# x = '{"name":"John", "age":30, "city":"New York"}'
# y = json.loads(x)
# print(y['age'])
#
# with open('week-6/files/json_data.json', 'w') as f:
#     json.dump(y, f)


# x = {
#     'name': 'John',
#     'age': 30,
#     'merried': True,
#     'children': ('Ann', 'Billy'),
#     'pets': None,
#     'cars': [
#         {'model': 'BMW 230'},
#         {'model': 'Ford'}
#     ]
# }
#
# print(json.dumps(x, indent=4))


# content = ''
# with open('week-6/files/json_content.json', 'r', encoding='utf-8') as f:
#     content = json.load(f)
#     print(content['data'][1]['lastName'])


from urllib import request

resp = request.urlopen('https://en.wikipedia.org/wiki/Main_Page')
data = resp.read()

html = data.decode('UTF-8')
# print(html)

content = request.urlopen('https://jsonblob.com/api/1226218978098929664')
data = content.read()
python_dict = json.loads((data.decode()))
print(type(python_dict))
print(python_dict['data'][0]['firstName'])