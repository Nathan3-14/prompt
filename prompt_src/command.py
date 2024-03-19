from typing import Dict, Tuple, Any, Callable

def get_dict_item_at_index(_dict: Dict[Any, Any], index: int):
	return _dict[list(_dict.keys())[index]]

class Command:
	def __init__(self, name: str, command_callable: Callable, command_args: Dict[str, Tuple[Any, bool]]):
		self.name = name
		self.callable = command_callable
		self.args_check = command_args

	def run_command(self, input_args: tuple) -> bool:
		index = 0
		output_args = list(input_args).copy()
		for arg_name, arg_data in self.args_check.items():
			arg_type = arg_data[0]
			arg_optional_bool = arg_data[1]

			try:
				if arg_type == bool: #? Special conversion case for boolean arguments
					output_args[index] = input_args[index].lower() in ["y", "yes", "true", "1"]
				else:
					output_args[index] = arg_type(input_args[index])
			
			except IndexError:
				print(f"Incorrect arguments supplied.\nExpected '' but recieved")
				return False
			except ValueError:
				print(f"type of {input_args[index]} did not match type required {arg_type}")
				return False
			index += 1
		print(output_args)
		self.callable(tuple(output_args))
		return True

	def __str__(self) -> str:
		return self.name


if __name__ == "__main__":
	class sick_command(Command):
		def say_radical(self, args: Tuple[str, int]):
			for i in range(args[1]):
				print(f"Yo {args[0]}, that's radical!")
			
		def __init__(self):
			super().__init__("radical", self.say_radical, {"name": (str, True), "number": (int, True)})
	test = sick_command()