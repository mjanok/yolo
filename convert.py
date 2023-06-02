import xml.etree.ElementTree as ET

# Define dictionary to map labels to class numbers
class_dict = {
    'exit': 0,
    'fireextinguisher': 1,
    'clock': 2,
    'chair': 3,
    'trashbin': 4,
    'printer': 5,
    'screen': 6
}

# TODO add file iteration

# Parse the XML file
tree = ET.parse('annotation_s1.xml')
root = tree.getroot()

# Loop through each image element in the XML file
for image in root.findall('images/image'):
    filename = image.get('file').replace('.jpg', '') + '.txt'
    with open(filename, 'w') as f:
        # Loop through each box element in the image
        for box in image.findall('box'):
            label = box.find('label').text
            class_num = class_dict[label]
            top = int(box.get('top'))
            left = int(box.get('left'))
            width = int(box.get('width'))
            height = int(box.get('height'))
            x_center = round((2 * left + width) / (2 * 1280), 6)
            y_center = round((2 * top + height) / (2 * 720), 6)
            w = round(width / 1280, 6)
            h = round(height / 720, 6)
            f.write('{} {} {} {} {}\n'.format(class_num, x_center, y_center, w, h))
