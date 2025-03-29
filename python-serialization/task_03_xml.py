#!/usr/bin/python3
"Importing Module XML"
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    It serialize the dictionary into XML
    and save it to the given filename.

    Args:
        dictionary: Python dictionary
        filename: Dictionnary where it save
    """
    root = ET.Element("data")

    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)

    tree = ET.ElementTree(root)
    tree.write(filename)


def deserialize_from_xml(filename):
    """
    It read the XML data from that file,
    and return a deserialized Python dictionary.
    Args:
        filename: read the data from this file

    Returns:
        A deserialized Python dictionary.
    """
    tree = ET.parse(filename)
    root = tree.getroot()

    dictionary = {}
    for child in root:
        dictionary[child.tag] = child.text

    return dictionary
