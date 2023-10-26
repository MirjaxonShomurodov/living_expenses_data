import json
def total_expenses(file_path: str) -> float:
    """
    get total expenses from json file
    
    Args:
        file_path (str): path to json file

    Returns:
        float: total expenses
    """
    f = open(file_path).read()
    d = json.loads(f)
    b=0
    for i in d:
        if d[i]>0:
            b+=d[i]
    return b
file_path = "data.json"
total = total_expenses(file_path)
print(total)
