#!/usr/bin/python3
"""Module for serializing and deserializing with XML."""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """Serialize a dictionary to XML and save to a file."""
    root = ET.Element("data")
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)
    tree = ET.ElementTree(root)
    tree.write(filename)


def deserialize_from_xml(filename):
    """Deserialize a dictionary from an XML file."""
    tree = ET.parse(filename)
    root = tree.getroot()
    return {child.tag: child.text for child in root}
