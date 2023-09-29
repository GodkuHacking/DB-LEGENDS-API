import json

def load_characters_data(file_name):
    try:
        with open(file_name, 'r') as json_file:
            data = json.load(json_file)
        return data
    except FileNotFoundError:
        return None

def find_character_by_id(characters_data, character_id):
    for character in characters_data:
        if character.get("id") == character_id:
            return character
    return None

def display_character_info(character):
    if character:
        print("Character Information:")
        print(f"Name: {character['name']}")
        print(f"ID: {character['id']}")
        print(f"Color: {character['color']}")
        print(f"Rarity: {character['rarity']}")
        print("Tags: ", ', '.join(character['tags']))
        print("Base Stats:")
        for stat, value in character['base_stats'].items():
            print(f"{stat}: {value}")
        print("Max Stats:")
        for stat, value in character['max_stats'].items():
            print(f"{stat}: {value}")
    else:
        print("Character not found in the database.")

if __name__ == "__main__":
    characters_data = load_characters_data("chars.json")
    if characters_data is None:
        print("Error: chars.json file not found.")
    else:
        character_id = input("Enter the character ID to find (e.g., DBL51-03U): ")
        character = find_character_by_id(characters_data, character_id)
        display_character_info(character)
