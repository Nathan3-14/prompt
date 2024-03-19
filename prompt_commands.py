import os
from rich import print


def list_dir(directory: str, sudo: bool=False):
	l_just = 12
	
	list_of_dir = os.listdir(directory)
	for element in list_of_dir:
		to_print = ""
		to_print_word = ""
		affects = []
		
		element_split = element.split(".")
		if element.startswith(".") and not sudo:
			continue
		match element_split[-1]:
			case "py":
				to_print_word = "python"
			case "md":
				to_print_word = "markdown"
			case _:
				if element.startswith("."):
					to_print_word = f"[bold]{element_split[-1].ljust(l_just)}[/bold]"
					affects.append("blue")
				else:
					to_print_word = element_split[-1]
		if len(affects) > 0:
			to_print = f"{to_print_word.ljust(l_just)} [{' '.join(affects)}]{element}[/{' '.join(affects)}]"
		else:
			to_print = f"{to_print_word.ljust(l_just)} {element}"
		print(to_print)


if __name__ == "__main__":
	list_dir(".")
	print("")
	list_dir(".", True)
	print("\n")