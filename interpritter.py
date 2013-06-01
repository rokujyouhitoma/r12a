import sys

from r12a.main import create_entry_point


if __name__ == "__main__":
    entry_point = create_entry_point({})
    entry_point(sys.argv)
