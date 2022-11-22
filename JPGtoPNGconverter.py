import sys
import os
from PIL import Image

# python3 JPGtoPNGconverter.py Exemplos/ new/

# sys.argv[0] == ‘sample.py’ 
# sys.argv[1] == ‘Hello’ 
# sys.argv[2] == ‘Python’

# grab 1st and 2nd arguments
image_folder = sys.argv[1]
output_folder = sys.argv[2]

# check if new folder exists, if not, create it
if not os.path.exists(output_folder):
    os.makedirs(output_folder)


# loop through Examples
# convert images to png
# save to the new folder
for filename in os.listdir(image_folder):
    img = Image.open(f'{image_folder}{filename}')
    clean_name = os.path.splitext(filename)[0]
    img.save(f'{output_folder}{clean_name}.png', 'png')
    print('All done')
