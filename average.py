import json

def average_expenses(file_path: str) -> float:
    """
    get average expenses from json file
    
    Args:
        file_path (str): path to json file

    Returns:
        float: average expenses
    """
    f = open(file_path).read()
    a = json.loads(f)
    b=0
    for i in a:
        if a[i]>0:
            b+=a[i]
    return b/2

# test
file_path = "data.json"
average = average_expenses(file_path)
print(average)
