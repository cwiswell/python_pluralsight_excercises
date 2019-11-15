""" test exceptions. """


def convert(s):
    """ Convert to an integer."""
    x = -1
    try:
        x = int(s)
    except (ValueError, TypeError):
        pass
    return x


convert("33")

convert("test")

convert([1, 2])
