import json

json_data = """{
    "name": "John Doe", "last_name": "Doe", "age": 30, "city": "New York",}"""

def validate_json(json_string):
    try:
        json.loads(json_string)
        return True
    except ValueError as e:
        print(f"Invalid JSON: {e}")
        return False

is_valid = validate_json(json_data)
print(f"Is the JSON data valid? {is_valid}")