import toml
import os
from rich import print
import json
from typing import Dict, Any
import sys

from prompt_commands import ListDir

global_config = {"config_path": "prompt.config.toml", "help": False}


def rich_input(input_message: str):
	print(input_message, end="")
	return input("")


def display_help(help_data: Dict[str, Any] | str):
	if isinstance(help_data, str):
		display_help(json.load(open(help_data, "r")))
		return
	for command_name, command_help in help_data.items():
		print(f"[bold]{command_name}[/bold]")
		print(f"    Description: {command_help['description']}")
		print(f"    Usage: {command_help['usage']}\n")


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

#* Consts *#
command_list = [
	ListDir
]
commands = {
	command.name: command for command in command_list
}


	
#* User Variables *#
prompt_data = {
	"file_addr": "/"
}

parse_prompt()

config = toml.load(global_config["config_path"])
if global_config["help"]:
	display_help(config["help"]["path"])
	quit()

prompt_config = config["prompt"]
message_config = prompt_config["messages"]

prompt = ""
for text, text_data in message_config.items():
	prompt += f"[{text_data['colour']}]{text_data['text']}[/{text_data['colour']}]"

while True:
	for prompt_var, prompt_var_data in prompt_data.items():
		prompt_var_replace = "{{@}}".replace("@", prompt_var)
		prompt = prompt.replace(f"{prompt_var_replace}", prompt_var_data)
	user_input = rich_input(prompt)
	if user_input in ["exit", "quit"]:
		break
	if user_input == "help":
		display_help(config["help"]["path"])
		continue

	commands[user_input[0]](tuple(user_input[1:]))

