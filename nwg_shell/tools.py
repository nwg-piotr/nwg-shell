#!/usr/bin/python3

import os
import json
import sys


def temp_dir():
    if os.getenv("TMPDIR"):
        return os.getenv("TMPDIR")
    elif os.getenv("TEMP"):
        return os.getenv("TEMP")
    elif os.getenv("TMP"):
        return os.getenv("TMP")

    return "/tmp"


def load_json(path):
    try:
        with open(path, 'r') as f:
            return json.load(f)
    except Exception as e:
        print("Error loading json: {}".format(e))
        return None


def save_json(src_dict, path):
    with open(path, 'w') as f:
        json.dump(src_dict, f, indent=2)


def check_key(dictionary, key, default_value):
    """
    Adds a key w/ default value if missing from the dictionary
    """
    if key not in dictionary:
        dictionary[key] = default_value


def load_text_file(path):
    try:
        with open(path, 'r') as file:
            data = file.read()
            return data
    except Exception as e:
        print(e)
        return None


def save_string(string, file):
    try:
        file = open(file, "wt")
        file.write(string)
        file.close()
    except:
        print("Error writing file '{}'".format(file))


def save_list_to_text_file(data, file_path):
    text_file = open(file_path, "w")
    for line in data:
        text_file.write(line + "\n")
    text_file.close()


def is_newer(string_new, string_existing):
    """
    Compares versions in format 'major.minor.patch' (just numbers allowed).
    :param string_new: new version to compare with existing one
    :param string_existing: existing version
    :return: True if new is newer then existing
    """
    new = major_minor_path(string_new)
    existing = major_minor_path(string_existing)
    if new and existing:
        if new[0] > existing[0]:
            return True
        elif new[1] > existing[1] and new[0] >= existing[0]:
            return True
        elif new[2] > existing[2] and new[0] >= existing[0] and new[1] >= existing[1]:
            return True
        else:
            return False
    else:
        return False


def major_minor_path(string):
    parts = string.split(".")
    if len(parts) != 3:
        return None
    try:
        return int(parts[0]), int(parts[1]), int(parts[2])
    except:
        return None


def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)
