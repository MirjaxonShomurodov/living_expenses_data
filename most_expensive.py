import json

def most_expensive(file_path: str) -> str:
    """
    get most expensive item from json file
    
    Args:
        file_path (str): path to json file

    Returns:
        str: most expensive item
    """
    f=open(file_path).read()
    a= json.loads(f)
    mx = a['rent']
    for i in  a:
        if  mx<a[i]:
            mx = a[i]
    return mx
file_path = "data.json"
most_expensive_item = most_expensive(file_path)
print(most_expensive_item)