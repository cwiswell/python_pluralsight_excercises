from pprint import pprint as pp

"""This code is based on a pluralsight video for python classes"""


class Trip:
    """A trip with a particular passenger train"""

    def __init__(self, number, train):
        if not number[:2].isalpha():
            raise ValueError(f"No train code in '{number}'")

        if not number[:2].isupper():
            raise ValueError(f"Invalid train code '{number}'")

        if not (number[2:].isdigit() and int(number[2:]) <= 99999):
            raise ValueError(f"Invalid route number '{number}'")

        self._number = number
        self._train = train
        rows, seats = self._train.seating_plan()
        self._seating = [None] + [{letter: None for letter in seats} for _ in rows]

    def number(self):
        return self._number

    def train(self):
        return self._number[:2]

    def train_model(self):
        return self._train.model()

    def print_seating(self):
        pp(self._seating)

    def allocate_seat(self, seat, passenger):
        """Allocate a seat to a passenger

        Args:
            seat: A seat designator such as '12C' or '21F'.
            passenger: The passenger name

        Raises:
             ValueError: If the seat is unavailable
        """
        rows, seat_letters = self._train.seating_plan()

        letter = seat[-1]
        if letter not in seat_letters:
            raise ValueError(f"Invalid seat letter {letter}")

        row_text = seat[:-1]
        try:
            row = int(row_text)
        except ValueError:
            raise ValueError(f"Invalid seat row {row_text}")

        if row not in rows:
            raise ValueError(f"Invalid row number {row}")

        if self._seating[row][letter] is not None:
            raise ValueError(f"Seat {seat} already occupied")

        self._seating[row][letter] = passenger


class Train:

    def __init__(self, registration, model, num_rows, num_seats_per_row):
        self._registration = registration
        self._model = model

        if num_rows < 1:
            raise ValueError(f"Invalid number of rows {num_rows}")

        if num_seats_per_row < 1:
            raise ValueError(f"Invalid number of seats per row {num_seats_per_row}")

        self._num_rows = num_rows
        self._num_seats_per_row = num_seats_per_row

    def registration(self):
        return self._registration

    def model(self):
        return self._model

    def seating_plan(self):
        return range(1, self._num_rows + 1), "ABCDEFGHJK"[:self._num_seats_per_row]


some_trip = Trip("BA9911", Train("G-PPT", "Some Train", num_rows=10, num_seats_per_row=5))
t = Train("G-PPT", "Some Train", num_rows=10, num_seats_per_row=5)

pp(some_trip.train_model())
some_trip.print_seating()
