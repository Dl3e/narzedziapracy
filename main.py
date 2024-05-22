import sys
import pathlib
import simplejson as json
import xmltodict
import yaml
import xml.etree.ElementTree as ET

def json2xml(json_obj, line_padding=""):
    result_list = list()

    json_obj_type = type(json_obj)

    if json_obj_type is list:
        for sub_elem in json_obj:
            result_list.append(json2xml(sub_elem, line_padding))

        return "\n".join(result_list)

    if json_obj_type is dict:
        for tag_name in json_obj:
            sub_obj = json_obj[tag_name]
            result_list.append("%s<%s>" % (line_padding, tag_name))
            result_list.append(json2xml(sub_obj, "\t" + line_padding))
            result_list.append("%s</%s>" % (line_padding, tag_name))

        return "\n".join(result_list)

    return "%s%s" % (line_padding, json_obj)

class Serializer:
    def get_file_content(self):
        match pathlib.Path(arg1).suffix.split():
            case ['.json']:
                try:
                    with open(self.initial_filepath) as my_file:
                        return json.load(my_file)
                except FileNotFoundError:
                    "Theres no such file"
                except json.JSONDecodeError:
                    "This file isnt json"
            case ['.yml']:
                try:
                    with open(self.initial_filepath) as my_file:
                        return yaml.load(my_file, Loader=yaml.FullLoader)
                except FileNotFoundError:
                    "Theres no such file"
            case ['.xml']:
                try:
                    with open(self.initial_filepath) as my_file:
                        return xmltodict.parse(my_file.read())
                except FileNotFoundError:
                    "Theres no such file"
    def serialize(self):
        match pathlib.Path(arg2).suffix.split():
            case ['.json']:
                json.dump(self.data, open(self.final_filepath, "a"))
            case ['.yml']:
                yaml.dump(self.data, open(self.final_filepath, "a"))
            case ['.xml']:
                match pathlib.Path(arg1).suffix.split():
                    case ['.json']:
                        with open(self.final_filepath, "a") as filef:
                            filef.write(json2xml(self.data))
                    case['.yml']:
                        with open(self.final_filepath, "a") as filef:
                            filef.write(xmltodict.unparse(self.data))
    def __init__(self, initial_filepath, final_filepath):
        self.initial_filepath = initial_filepath
        self.final_filepath = final_filepath
        self.data = self.get_file_content()
        self.serialize()


if __name__ == '__main__':
    arg1 = sys.argv[1]
    arg2 = sys.argv[2]
    try:
        file = Serializer(arg1, arg2)
    except:
        exit(-1)
