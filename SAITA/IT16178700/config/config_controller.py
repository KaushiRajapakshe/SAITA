from configparser import ConfigParser

# Set Config location
config_location = ""


# Initialize Application configuration
def init_config(filename):
    config = ConfigParser(default_section="default")
    config.read(config_location + filename)
    return config
