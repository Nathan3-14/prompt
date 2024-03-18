from _typeshed import IndexableBuffer
import toml
import sys

global_config = {
    "config_path": "prompt.config.toml"
}

def parse_prompt():
    args = sys.argv[:1]
    flags = {
        "-c": "config_path"
    }

    for flag, global_config_key in flags.items():
        if flag not in args:
            continue
        
        try:
            flag_index = args.index(flag)
            flags[flag] = args[flag_index + 1]
        except IndexError:
            print("Incorrect flags supplied")
            quit()

parse_prompt()            

config = toml.load(global_config["config_path"])


