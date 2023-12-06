import json

# Specify the path to your JSON file
json_file_path = 'userName.json'

# Read the content of the JSON file
with open(json_file_path, 'r') as json_file:
    loaded_data = json.load(json_file)
print("Element at position 1:", loaded_data[0].get('name')
)
# # Extract elements at positions 0 and 1
# element_at_0 = loaded_data.get('id')
# element_at_1 = loaded_data.get('name')
#
# # Print the extracted elements
# print("Element at position 0:", element_at_0)
# print("Element at position 1:", element_at_1)