# Finish Implementing this first!

# Finds a room with a size that matches the group size and takes preferences into account
# Takes in the following as parameters:
#   - Group Size
#   - List of preferences [Dorm building preference, floor, year]
#   - campus_data (Dictionary of all dorms and their availability)
#
# @Return returns a dictionary in this structure: 
#   Dorm_building: {
#       floor: {
#           rooms: {
#               room_info {}
#   }}}

def ideal_search (group_Size, list_Of_Pref , campus_Data): 
    # Return var
    dict_Of_Rooms = {}
    # First grab the preferences
    buildingPref = list_Of_Pref[0]
    floorPref = list_Of_Pref[1]
    studentYear = list_Of_Pref[2]

    # Now we can look though the campus_Data and available rooms 
    for room in campus_Data[buildingPref][floorPref]:
        # Continue if student year doesnt match the type of the room
        if(room["type"] != studentYear):
            continue
        else: 
            # See if there are any occupants in the room: 
            people_In_Room = len(room["Occupants"])
            
            # See
    return dict_Of_Rooms

def search_occupants (num_Occupants):
    if (num_Occupants == 0): 
        return True
    else:
        return False