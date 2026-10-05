# Cash Register

A small Python object model of a cash register for an e-commerce checkout. It
keeps a running total, records every item scanned, applies a percentage
discount, and can void the most recent transaction.

Built for the Flatiron School lab *Object Oriented Programming (OOP) Part 2 –
Cash Register*.

## Features

- **Optional discount** set when the register is created (`CashRegister(20)` = 20% off)
- **Discount validation** through a property: only whole numbers from 0–100 are
  accepted; anything else prints `Not valid discount`
- **Add items** with a price and optional quantity
- **Apply the discount** to the current total
- **Void the last transaction**, restoring both the total and the item list

## Requirements

- Python 3 (the Pipfile pins 3.8.13; newer versions also work)
- [pipenv](https://pipenv.pypa.io/)

## Installation

```bash
git clone https://github.com/<your-username>/oop-p2-cash-register-lab.git
cd oop-p2-cash-register-lab
pipenv install
pipenv shell
```

If Python 3.8.13 isn't installed, point pipenv at the Python you have:

```bash
pipenv install --python $(which python3)
```

## Usage

```python
from cash_register import CashRegister

register = CashRegister(20)          # 20% discount

register.add_item("eggs", 1.99)
register.add_item("book", 5.00, 3)   # quantity of 3
register.total                       # 16.99
register.items                       # ['eggs', 'book', 'book', 'book']

register.void_last_transaction()     # removes all 3 books
register.total                       # 1.99
register.items                       # ['eggs']

register.apply_discount()
# After the discount, the total comes to $1.59.
```

### API

| Member | Description |
| --- | --- |
| `CashRegister(discount=0)` | Creates a register. `discount` is a percentage from 0–100. |
| `discount` | Validated property. Invalid values print `Not valid discount` and are ignored. |
| `total` | Running total, starting at `0`. |
| `items` | Every unit added, e.g. 3 books add `"book"` three times. |
| `previous_transactions` | List of `{"item", "price", "quantity"}` dicts, one per `add_item` call. |
| `add_item(item, price, quantity=1)` | Adds `price * quantity` to the total and records the transaction. |
| `apply_discount()` | Takes the discount off the total and prints the new total. Prints `There is no discount to apply.` when the discount is 0. |
| `void_last_transaction()` | Undoes the last `add_item` call. Prints `There is no transaction to void.` when there is nothing to undo. |

## Running the Tests

```bash
pipenv run pytest
```

On Python 3.12+ the pinned pytest 7.1.3 can crash during assertion rewriting;
run with plain asserts instead:

```bash
pipenv run pytest --assert=plain
```

## Screenshot

All 14 tests passing:

```
CashRegister in cash_register.py takes one optional argument, a discount, on initialization. .
CashRegister in cash_register.py sets an instance variable total to zero on initialization. .
CashRegister in cash_register.py sets an instance variable items to empty list on initialization. .
CashRegister in cash_register.py accepts a title and a price and increases the total. .
CashRegister in cash_register.py also accepts an optional quantity. .
CashRegister in cash_register.py doesn"t forget about the previous total .
CashRegister in cash_register.py applies the discount to the total price. .
CashRegister in cash_register.py prints success message with updated total .
CashRegister in cash_register.py reduces the total .
CashRegister in cash_register.py prints a string error message that there is no discount to apply .
CashRegister in cash_register.py returns an array containing all items that have been added .
CashRegister in cash_register.py returns an array containing all items that have been added, including multiples .
CashRegister in cash_register.py subtracts the last item from the total .
CashRegister in cash_register.py returns the total to 0.0 if all items have been removed .

============================== 14 passed ==============================
```

## Project Structure

```
lib/
├── cash_register.py          # CashRegister class
└── testing/
    ├── cash_register_test.py # pytest suite
    └── conftest.py           # readable test names
```

## License

See [LICENSE.md](LICENSE.md).
