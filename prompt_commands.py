import os
from rich import print


def list_dir(directory: str):
    print(os.listdir(directory))


if __name__ == "__main__":
    print("")
    list_dir(".")