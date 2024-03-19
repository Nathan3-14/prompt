from typing import Dict, List, Tuple, Any

def get_dict_item_at_index(_dict: Dict[Any, Any], index: int):
	return _dict[list(_dict.keys())[index]]

class Command:
	def __init__(self, name: str, command_callable: callable, command_args: Dict[str, Any]):
		self.name = name
		self.callable = command_callable
		self.args_check = command_args

	def run_command(self, input_args: tuple) -> bool:
		index = 0
		for arg_name, arg_type in self.args_check.items():
			try:
				if not isinstance(input_args[index], arg_type):
					print("You wrong silly")
					return False
			except IndexError:
				print("Give me more stuffs ")
				return False
			index += 1
		self.callable(input_args)
		return True

	def __str__(self) -> str:
		return self.name


if __name__ == "__main__":
	class sick_command(Command):
		def say_radical(self, args: Tuple[str, int]):
			for i in range(args[1]):
				print(f"Yo {args[0]}, that's radical!")
			
		def __init__(self):
			super().__init__("radical", self.say_radical, {"name": str, "number": int})
	test = sick_command()
	test.run_command(("me"))