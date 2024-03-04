import json
import zlib
import xml.etree.ElementTree as element_tree

def json_example():
    our_list = ["a", "b", 3, 4, "Hello"]
    our_dict = {"Number": "CSI-275",
                "Class Size": 15}
    list_json = json.dumps(our_list)
    print(f"Encoded list: {list_json}")

    print("JSON with formatting:")
    print(json.dumps(our_dict, indent=4, sort_keys=True))

    list_from_json = json.loads(list_json)
    print(f'Second element is {list_from_json[1]}')


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

# <key>value</key>


def compression_example():
    string = "abcdefghijklmnop" * 1000

    byte_string = string.encode('utf-8')
    print(f'Length of uncompressed string: {len(byte_string)}')

    for i in range(1, 10):
        compressed = zlib.compress(byte_string, i)
        print(f'Compressed length at lv. {i}: {len(compressed)}')

if __name__ == "__main__":
    # json_example()
    # xml_function()
    compression_example()
