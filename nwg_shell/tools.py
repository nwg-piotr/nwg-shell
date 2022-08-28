#!/usr/bin/python3

import json


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
        elif new[1] > existing[1]:
            return True
        elif new[2] > existing[2]:
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
