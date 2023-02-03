import json
from ideal_search import ideal_search
from best_search import best_search 
from ideal_split_search import ideal_split_search 


if __name__ == "__main__":

    # Oepn the json file
    file = open('campus.json')
    # Same it and load it into here: 
    campus_data = json.load(file)   

    # Just a simple print to print everything out 
    # print(json.dumps(campus_data, indent=2))
    
    # Testing ideal_search: 
    building = input("Preferred Dorm: ")
    groupSize = input("Group Size: ")
    floorPref = input("Floor Preference: ")
    studentYear = input("Student year: ")

    floorPrefToStr = "floor" + floorPref
    
    listPreferences = [building, floorPrefToStr, studentYear]
    print(ideal_search(groupSize, listPreferences, campus_data))