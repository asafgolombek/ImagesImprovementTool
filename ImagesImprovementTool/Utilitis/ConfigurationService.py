from Utilitis.CmdArgumentsService import CmdArgumentsService
import json

def read_and_parse_json(filepath):
    """
    Reads a file and parses its content as JSON.

    Args:
        filepath: The path to the file.

    Returns:
        A Python dictionary or list representing the JSON data, or None if an error occurs.
        Prints error messages to the console if there's an issue.
    """
    try:
        with open(filepath, 'r', encoding='utf-8') as f:  # 'r' for reading, utf-8 encoding
            try:
                data = json.load(f)  # Parse the JSON data
                return data
            except json.JSONDecodeError as e:
                print(f"Error decoding JSON in {filepath}: {e}")
                return None  # Or handle the error differently, e.g., raise it
    except FileNotFoundError:
        print(f"File not found: {filepath}")
        return None
    except Exception as e:  # Catch any other potential errors (e.g., permissions)
        print(f"An error occurred while reading {filepath}: {e}")
        return None


class ConfigurationService:
    def __init__(self, cmd_arguments_service: CmdArgumentsService):
        self.cmdArgumentsService = cmd_arguments_service
        self.configuration = read_and_parse_json(self.cmdArgumentsService.getConfigurationFilePath())

    def getImages(self):
        return self.configuration["Images"]

