response = {
    "id": "0001",
    "type": "donut",
    "longOne": "01234567890123456789",
    "data": 1234,
    "newdate": "",
    "control": [
        2,
        4,
        "abcdefghijklmnopqrstuvwxyz",
        {
            "width": 200,
            "length": None
        },
        "",
        12.129
    ],
    "image": {
        "height": 200,
        "length": None,
        "rate": 100.01,
        "image": {
            "height": 200,
            "length": None,
            "rate": 100.01,
            "owner1": [],
            "owner2": {},
            "ownership": [
                "",
                None,
                "123",
                [
                    "1",
                    "b",
                    '',
                    [],
                    {}
                ],
                "xyz"
            ]
        }
    },
    "thumbnail": {
        "height": 32,
        "wieght": ""
    }
}

def check_value(value):
    if type(value) is list: 
        value = [x for x in value if x]
        value = [clean_dic(x) if (type(x) is dict) else x for x in value]
        return value
    if not value: return False
    if value in ["", None]:
        return False
    return value

def check_data_is_iterable(value):
    return type(value) is dict


def clean_dic(data):
    filtered_data = {}
    for key, value in data.items():
        if check_data_is_iterable(value):
            clean_sub_data = clean_dic(value)
            result = check_value(clean_sub_data)
            if result:
              filtered_data[key]  = result
        else:
            result = check_value(value)
            if result:
              filtered_data[key]  = result

    if filtered_data:
        return filtered_data
    else:
        None

result = clean_dic(response)
print(result)