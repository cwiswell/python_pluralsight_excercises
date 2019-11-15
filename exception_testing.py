""" test exceptions. """


def convert(s):
    """ Convert to an integer."""
    x = -1
    try:
        x = int(s)
        print(f"Conversion succeeded! x = {x}")
    except (ValueError, TypeError):
        print("Conversion failed!")
    return x


convert("33")

convert("test")

convert([1,2])
