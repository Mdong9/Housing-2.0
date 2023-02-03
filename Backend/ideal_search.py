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

def ideal_search (group_Size, list_Of_Pref, campus_Data): 
    # Return dictionary of available rooms
    recommended_Rooms = {}
    # First grab the preferences
    buildingPref = list_Of_Pref[0]
    floorPref = list_Of_Pref[1]
    studentYear = list_Of_Pref[2]
    # Room number will be used as keys 
    roomNum = 0        
    # Store access to check rooms of building
    access_Key = campus_Data[buildingPref][floorPref]
    # Now we can look though the campus_Data and available rooms 
    for room in access_Key:
        # Continue if student year doesnt match the type of the room
        if(access_Key[room]["type"] != studentYear):
            continue

        # Get the amount of people in current room: 
        people_In_Room = len(access_Key[room]["Occupants"])
        
        if(match_group_size(people_In_Room, group_Size, access_Key[room]["size"])):
            recommended_Rooms[roomNum] = room

        roomNum += 1
    return recommended_Rooms

# Function to check if group size can fit in room
def match_group_size (num_Occupants, group_Size, room_Size):
    if (num_Occupants == 0 and (int(group_Size) <= int(room_Size))): 
        return True
    else:
        return False
    
