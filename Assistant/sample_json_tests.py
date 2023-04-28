import json

json_string = """
{
    "name": "John Smith",
    "age": 30,
    "email": "john.smith@example.com",
    "address": {
        "street": "123 Main St",
        "city": "Anytown",
        "state": "CA",
        "zip": "12345"
    },
    "phone_numbers": [
        {
            "type": "home",
            "number": "555-1234"
        },
        {
            "type": "work",
            "number": "555-5678"
        },
        {
            "type": "mobile",
            "number": "555-9012"
        }
    ]
}
"""

data = json.loads(json_string)
data['test'] = True

new_json = json.dumps(data, indent=4)
print(new_json)