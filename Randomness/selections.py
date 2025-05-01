import random

# Define locations with study places and gyms
places = {
    "university": {
        "study_places": ["U Lib", "CC Lib", "UC Lib", "Shaw Lib", "NA Lib", "Common", "E+ Cafe", "Sensory ZERO", "NUK Café", "SMACK"],
        "gyms": ["U Gym", "UC Gym", "Shaw Gym", "NA Gym", "SHHO Gym", "Pommerenke Gym"]
    },
    "shatin": {
        "study_places": ["Beans The Greenhouse", "Starbucks", "Kahu Coffee", "2 + 2 Cafe & Bar", "Shatin Lib", "Luckin Coffee", "Pacific Coffee", "The Alchemist Cafe"],
        "gyms": ["Yuen Wo Road Gym"]
    },
    "taiwai": {
        "study_places": ["Cozy Coffee", "The Shack Cafe", "Whisk Factory", "The Chas Long Long Ago", "Aries Cafe", "ALOHA", "Jackycat Teahouse"],
        "gyms": ["Mei Lam Gym", "Che Kung Temple Gym"]
    },
    "mos": {
        "study_places": ["Stay", "WM Cafe and Bar", "T.B.M.Comfy", "L.D.K. by Ufufu Café", "Starbucks", "Casa Cafe & Bistro MOS Lib"],
        "gyms": ["Heng On Gym", "MOS Gym"]
    },
    "yuenchaukok": {
        "study_places": ["HIS Cafe", "Yuen Chau Kok Lib", "Cafe Koinonia", "Reactors Coffee", "Starbucks", "Little Luck Cafe"],
        "gyms": ["Yuen Chau Kok Gym"]
    }
}

def select_location(location=None):
    """Select a location either by name or randomly, then randomize gym and study place."""
    if location is None:
        chosen_location = random.choice(list(places.keys()))
        message = f"randomly selected location: {chosen_location}"
    else:
        location = location.lower().strip()
        if location in places:
            chosen_location = location
            message = f"chosen location: {chosen_location}"
        else:
            return None, f"location '{location}' not found. available locations are: {', '.join(places.keys())}."
    
    # Randomize gym and study place immediately
    gym_message = ""
    study_message = ""
    
    if places[chosen_location]["gyms"]:
        chosen_gym = random.choice(places[chosen_location]["gyms"])
        gym_message = f"gym: {chosen_gym}"
    else:
        gym_message = "gym: none available"
    
    if places[chosen_location]["study_places"]:
        chosen_study_place = random.choice(places[chosen_location]["study_places"])
        study_message = f"study place: {chosen_study_place}"
    else:
        study_message = "study place: none available"
    
    full_message = f"{message} - {gym_message}, {study_message}"
    return chosen_location, full_message

def add_to_location(location, category, item):
    """Add a new gym or study place to the specified location."""
    location = location.lower().strip()
    category = category.lower().strip()
    if location in places:
        if category == "gym":
            places[location]["gyms"].append(item)
            return f"added '{item}' to gyms in {location}."
        elif category == "study":
            places[location]["study_places"].append(item)
            return f"added '{item}' to study places in {location}."
        else:
            return f"category '{category}' invalid. use 'gym' or 'study'."
    else:
        return f"location '{location}' not found. available locations are: {', '.join(places.keys())}."

# Main loop with a single prompt
while True:
    prompt = "type 'random' to randomize a location and get a gym/study place, 'choose (place)' to pick a location and get a gym/study place, 'add (place) (gym/study) (name)' to add, or 'exit': "
    command = input(prompt).strip()
    parts = command.split()

    if not parts:
        print("please enter a command.")
    elif parts[0].lower() == "random":
        _, message = select_location()
        print(message)
    elif parts[0].lower() == "choose" and len(parts) >= 2:
        location_name = " ".join(parts[1:]).lower()
        _, message = select_location(location_name)
        print(message)
    elif parts[0].lower() == "add" and len(parts) >= 4:
        location_name = parts[1].lower()
        category = parts[2].lower()
        item = " ".join(parts[3:])
        print(add_to_location(location_name, category, item))
    elif parts[0].lower() == "exit":
        break
    else:
        print("invalid command. follow the prompt instructions.")
