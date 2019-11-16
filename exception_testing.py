""" test exceptions. """
import sys


def convert(s):
    """ Convert to an integer."""
    try:
        return int(s)
    except (ValueError, TypeError) as e:
        print(f"Conversion error: {str(e)}", file=sys.stderr)
        raise


convert("33")

convert("test")

convert([1, 2])
