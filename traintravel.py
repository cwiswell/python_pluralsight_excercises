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

    def _parse_set(self, seat):
        """Parse a seat designator into a valid row and letter

        Args:
            seat: A seat designator such as '12F'

        Returns:
            A tuple containing an integer and a string for row and seat.
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

        return row, letter

    def allocate_seat(self, seat, passenger):
        """Allocate a seat to a passenger

        Args:
            seat: A seat designator such as '12C' or '21F'.
            passenger: The passenger name

        Raises:
             ValueError: If the seat is unavailable
        """
        row, letter = self._parse_set(seat)

        if self._seating[row][letter] is not None:
            raise ValueError(f"Seat {seat} already occupied")

        self._seating[row][letter] = passenger

    def relocate_passenger(self, from_seat, to_seat):
        """Relocate a passenger to a different seat.

        Args:
            from_seat: The existing seat designator for the passenger to be moved.
            to_seat: The new seat designator.
        """
        from_row, from_letter = self._parse_set(from_seat)
        if self._seating[from_row][from_letter] is None:
            raise ValueError(f"No passenger to relocate in {from_seat}")

        to_row, to_letter = self._parse_set(to_seat)
        if self._seating[to_row][to_letter] is not None:
            raise ValueError(f"Seat {from_seat} is already occupied")

        self._seating[to_row][to_letter] = self._seating[from_row][from_letter]
        self._seating[from_row][from_letter] = None

    def num_available_seats(self):
        return sum(sum(1 for s in row.values() if s is None)
                   for row in self._seating
                   if row is not None)

    def make_boarding_cards(self, card_printer):
        for passenger, seat in sorted(self._passenger_seats()):
            card_printer(passenger, seat, self.number(), self.train_model)

    def _passenger_seats(self):
        """An iterable series of passenger seating allocations."""
        row_numbers, seat_letters = self._train.seating_plan()
        for row in row_numbers:
            for letter in seat_letters:
                passenger = self._seating[row][letter]
                if passenger is not None:
                    yield passenger, f"{row}{letter}"


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


def make_trip():
    some_trip = Trip("BA9911", Train("G-PPT", "Some Train", num_rows=15, num_seats_per_row=6))
    some_trip.allocate_seat("6A", "Bob Ross")
    some_trip.allocate_seat("13F", "Timothy Toddle")
    some_trip.allocate_seat("1B", "Some Dude")
    some_trip.allocate_seat("5C", "Mel Gibbs")
    some_trip.allocate_seat("1D", "Richard Richardson")
    return some_trip


def console_card_printer(passenger, seat, train_number, train):
    output = f"| Name: {passenger}" \
             f"  Trip: {train_number}" \
             f"  Seat: {seat}" \
             f"  Train: {train}"
    banner = '+' + '-' * (len(output) - 2) + '+'
    border = '|' + ' ' * (len(output) - 2) + '|'
    lines = [banner, border, output, border, banner]
    card = '\n'.join(lines)
    print(card)
    print()


t = make_trip()
t.print_seating()
t.relocate_passenger('13F', '1A')
t.print_seating()
print(t.num_available_seats())
