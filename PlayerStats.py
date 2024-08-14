import requests
import json

# Base URL of the Wynncraft API
API_URL = "https://api.wynncraft.com/v3"

# Function to get player statistics
def get_player_stats(player_name):
    endpoint = f"{API_URL}/player/{player_name}" #Add ?fullResult for all character data
    response = requests.get(endpoint)
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: Unable to fetch data for player {player_name}. Status code: {response.status_code}")
        return None

# Function to get the character list
def get_character_list():
    endpoint = f"{API_URL}/player/{player_name}/characters"
    response = requests.get(endpoint)
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: Unable to fetch server status. Status code: {response.status_code}")
        return None

# # Function to get those characters ability maps
# def get_character_abilities():
    
#     endpoint = f"{API_URL}/player/{player_name}/characters/{character_UUID}/abilities"
#     response = requests.get(endpoint)
    
#     if response.status_code == 200:
#         return response.json()
#     else:
#         print(f"Error: Unable to fetch server status. Status code: {response.status_code}")
#         return None


# Usage
if __name__ == "__main__":
    # Prompt the user for a player name
    player_name = input("Enter the player name: ")
    character_UUID = 0 # Implement if 0 ERROR message

    # File to save requests
    file_object = open(player_name+'.json', 'w+')

    # Get player stats
    player_stats = get_player_stats(player_name)
    if player_stats:
        print(f"\nPlayer Stats for {player_name}:")
        print(player_stats)
        json.dump(player_stats, file_object, indent = 6)
    
    # Get character list
    character_list = get_character_list()
    if character_list:
        print("\nCharacter List:")
        print(character_list)

        json.dump(character_list, file_object, indent = 6)

    file_object.close()
