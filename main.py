import sys
import pathlib
import simplejson as json


class JsonClass:
    def get_file_content(self):
        try:
            with open(self.initial_filepath) as my_file:
                return json.load(my_file)
        except FileNotFoundError:
            "Theres no such file"
        except json.JSONDecodeError:
            "This file isnt json"

    def serialize_json(self):
        json.dump(self.data, open(self.final_filepath, "a"))

    def __init__(self, initial_filepath, final_filepath):
        self.initial_filepath = initial_filepath
        self.final_filepath = final_filepath
        self.data = self.get_file_content()


if __name__ == '__main__':
    arg1 = sys.argv[1]
    arg2 = sys.argv[2]
    file = None
    match pathlib.Path(arg1).suffix.split():
        case ['.json']:
            file = JsonClass(arg1, arg2)
            print(file.data)
        case _:
            pass

    match pathlib.Path(arg2).suffix.split():
        case ['.json']:
            file.serialize_json()
        case _:
            pass


