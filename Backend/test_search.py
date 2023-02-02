import json
import ideal_search
import best_search
import ideal_split_search


if __name__ == "__main__":

    # Oepn the json file
    file = open('campus.json')
    # Same it and load it into here: 
    campus_data = json.load(file)   

    # Just a simple print to print everything out 
    print(json.dumps(campus_data, indent=2))
    

    # 