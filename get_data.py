import json
from pprint import pprint
def get_data(file_path: str) -> dict:
    """
    get data from json file as dictionary
    
    Args:
        file_path (str): path to json file

    Returns:
        dict: dictionary of data
    """
    f = open('data.json','r').read()
    m = json.loads(f)
    return m 
    
file_path = open("data.json",'r')
data = get_data(file_path)
pprint(data)
