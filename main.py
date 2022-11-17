import sys
import json

from randomize import randomize

def main():
    if len(sys.argv) >= 2:
        rom_path = sys.argv[1]
        with open('config.json') as config_json:
            config = json.load(config_json)
        randomize(rom_path, config)
    else:
        print("Rom not provided")

if __name__ == "__main__":
    main()