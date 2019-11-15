""" test exceptions. """


def convert(s):
    """ Convert to an integer."""
    try:
        x = int(s)
        print(f"Conversion succeeded! x = {x}")
    except ValueError:
        print("Conversion failed!")
        x = -1
    return x


convert("33")

convert("test")
