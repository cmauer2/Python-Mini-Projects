import json
from pathlib import Path

DATA_FILE = Path("data") / "testing.json"

def load_data() -> dict:
    # load all saved password from the JSON file
    try:
        with DATA_FILE.open("r", encoding="utf-8") as read_file:
            return json.load(read_file)
    except:
        return {}

def save_data(data: dict) -> None:
    # save all passwords back to the JSON file
    try: 
        with DATA_FILE.open("w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)
    except:
        print("Error saving to JSON.")

def add_entry(service: str, username: str, password: str) -> None:
    """
    Save a password for a given service and username.

    Example structure in JSON:
    {
        "github": {
            "user@example.com": "password123"
        }
    }
    """
    
    data = load_data()
    
    if service not in data:
        data[service] = {}
    
    data[service][username] = password
    save_data(data)

def get_entry(service: str, username: str) -> str | None:
    # get the pw for a specific service + username, or None if not found
    data = load_data()
    # password = data[service][username]
    # return password
    return data.get(service, {}).get(username)

def list_entries() -> dict:
    # return the whole data dict (for now)
    return load_data()