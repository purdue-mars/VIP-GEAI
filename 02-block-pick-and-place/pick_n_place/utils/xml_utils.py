import os
import re
import xml.etree.ElementTree as ET
from xml.dom import minidom
import robohive
import sys
from pathlib import Path

SIMHIVE_PATH = Path(robohive.__file__).absolute().parent / "simhive"

def replace_simhive_path(xml_path: str):
    # Parse the XML file
    tree = ET.parse(xml_path)
    root = tree.getroot()

    # Compile a regex pattern to find '*simhive'
    pattern = re.compile(r".*simhive")

    # Iterate over all elements and replace 'file' attribute if it contains '.*simhive'
    for elem in root.iter():
        for attrib in elem.attrib:
            if "file" in attrib or "dir" in attrib:
                elem.attrib[attrib] = pattern.sub(str(SIMHIVE_PATH), elem.attrib[attrib])

    # Return the new XML structure as a string
    return ET.tostring(root, encoding="unicode")

