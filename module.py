import configparser
import json
from file_utils import read_file

# Read configuration file
config = configparser.ConfigParser()
config.read('config.ini')
source_file = config['FILES']['source_file']
destination_file = config['FILES']['destination_file']

# Read content of source file
source_content = read_file(source_file)
data = json.loads(source_content)

# Create destination file
with open(destination_file, 'w') as file:
    # Write keys on the first line
    keys = list(data.keys())
    keys_line = ','.join(keys)
    file.write(keys_line + '\n')
    # Write values on the second line
    values = list(data.values())
    values_line = ','.join(values)
    file.write(values_line + '\n')