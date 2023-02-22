import configparser
from file_reader import read_file

# Read the configuration file
config = configparser.ConfigParser()
config.read('config.ini')

# Get the source and destination file paths from the configuration file
source_file_path = config['source_file']['path']
destination_file_path = config['destination_file']['path']

# Read the content of the source file
source_file_content = read_file(source_file_path)
