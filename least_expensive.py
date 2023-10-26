import json

def least_expensive(file_path: str) -> str:
    """
    get least expensive item from json file
    
    Args:
        file_path (str): path to json file

    Returns:
        str: least expensive item
    """
    f = open(file_path).read()
    a = json.loads(f)
    m = a['rent']
    for i in a:
        if m>a[i]:
            m=a[i]
    return m
file_path = ("data.json")
least_expensive_item = least_expensive(file_path)
print(least_expensive_item)
