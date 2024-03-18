import toml
from rich import print
import sys

global_config = {"config_path": "prompt.config.toml", "help": False}


def rich_input(input_message: str):
	print(input_message, end="")
	return input("")


def display_help(help_dict: dict):
	pass


def parse_prompt():
	args = sys.argv[1:]
	flags = {"-c": ("config_path", False), "-h": ("help", True)}

	for flag, flag_data in flags.items():
		flag_name = flag_data[0]
		flag_bool = flag_data[1]
		if flag not in args:
			continue

		try:
			flag_index = args.index(flag)
			if flag_bool:
				global_config[flag_name] = not (global_config[flag_name])
			else:
				global_config[flag_name] = args[flag_index + 1]
		except IndexError:
			quit()




parse_prompt()

if global_config["help"]:
	print("Help stuff!")
	quit()
config = toml.load(global_config["config_path"])
prompt_config = config["prompt"]
message_config = prompt_config["messages"]

prompt = ""
for text, text_data in message_config.items():
	prompt += f"[{text_data['colour']}]{text_data['text']}[/{text_data['colour']}]"

while True:
  print(rich_input(prompt))
