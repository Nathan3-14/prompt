import os
from rich import print
from command import Command
from typing import Tuple


class ListDir(Command):
	def list_dir(self, args: Tuple[str, bool]):
		l_just = 12
		directory = args[0]
		sudo = args[1]
		
		list_of_dir = os.listdir(directory)
		for element in list_of_dir:
			to_print = ""
			to_print_word = ""
			affects = []
			
			element_split = element.split(".")
			if element.startswith(".") and not sudo: #? Skip hidden elements if not sudo
				continue
			
			match element_split[-1]:
				case "py":
					to_print_word = "python"
				case "md":
					to_print_word = "markdown"
				case _:
					if element.startswith("."):
						affects.append("blue")
					to_print_word = element_split[-1]
			if len(affects) > 0:
				to_print = f"{to_print_word.ljust(l_just)} [{' '.join(affects)}]{element}[/{' '.join(affects)}]"
			else:
				to_print = f"{to_print_word.ljust(l_just)} {element}"
			print(to_print)
	def __init__(self):
		super().__init__("list_dir", self.list_dir, {"directory": str, "sudo": bool})
	

if __name__ == "__main__":
	commands = {
		"list_dir": ListDir
	}
