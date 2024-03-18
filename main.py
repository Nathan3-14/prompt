import toml
import sys

global_config = {
    "config_path": "prompt.config.toml",
    "help": False
}

def parse_prompt():
    args = sys.argv[:1]
    flags = {
        "-c": ("config_path", False),
        "-h": ("help", True)
    }

    for flag, global_config_data in flags.items():
        global_config_bool = global_config_data[0]
        global_config_flag = global_config_data[1]

        if flag not in args:
            continue
        
        try:
            flag_index = args.index(flag)
            if global_config_bool:
                flags[flag] = not (flags[flag])
            else:
                flags[flag] = args[flag_index + 1]
        except IndexError:
            print("Incorrect flags supplied")
            quit()

parse_prompt()            

if global_config["help"]:
    print("Help stuff!")
    quit()
config = toml.load(global_config["config_path"])


