""" test exceptions. """
import sys


def convert(s):
    """ Convert to an integer."""
    try:
        return int(s)
    except (ValueError, TypeError) as e:
        print(f"Conversion error: {str(e)}", file=sys.stderr)
        return -1


convert("33")

convert("test")

convert([1, 2])
