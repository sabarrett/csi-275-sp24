import json
import xml.etree.ElementTree as element_tree
import zlib


def json_example():
    our_list = ["a", "e", "i", "o", "u"]
    our_dict = {"Course Number": "CSI-275",
                "Seats": 15}

    # Turn our list into a json string.
    json_list = json.dumps(our_list)
    print(f'json-encoded list: {json_list}')

    # Turn our dict into a json string
    # Note that json has nice formatting options!
    print(json.dumps(our_dict, sort_keys=True, indent=4))

    # Load json encoded data back into python
    loaded_list = json.loads(json_list)
    print(f'Loaded {loaded_list} from json.')


def xml_function():
    # Create our list
    list = ["e", "d", "c", "b", "a"]

    # Define the XML root element
    root = element_tree.Element("letters")

    # Create a sub element
    root = element_tree.SubElement(root, "letters")

    # Add list to the XML
    for i in range(len(list)):
        child = element_tree.SubElement(root, "letter")
        child.text = list[i]

    # Create XML tree
    letter_tree = element_tree.ElementTree(root)
    print(letter_tree)

    # Write to file
    letter_tree.write("Output.xml",
                      encoding='utf-8', xml_declaration=True)

    # From XML to Python
    xml_string = "<?xml version='1.0' encoding='utf-8'?><letters>" \
                 "<letter>f</letter>" \
                 "<letter>g</letter>" \
                 "<letter>h</letter>" \
                 "<letter>i</letter>" \
                 "<letter>j</letter></letters>"

    # Load the string
    new_root = element_tree.fromstring(xml_string)

    # Build the list from the XML
    new_list = []
    for child in new_root:
        print(f"{child.tag}: {child.text}")
        new_list.append(child.text)
    print(f"List from XML: {new_list}")

# <letters>
#    <letter>e</letter>
#            ^ node.text


def zlib_example():
    string = "abcdefghijklmno"
    as_bytes = string.encode('utf-8')
    compressed = zlib.compress(as_bytes)

    print(f'Len of as_bytes: {len(as_bytes)}')
    print(f'Compressed len : {len(compressed)}')

if __name__ == "__main__":
    # json_example()
    # xml_function()
    zlib_example()
