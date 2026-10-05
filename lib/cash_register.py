#!/usr/bin/env python3


class CashRegister:
  """Simulates a cash register for an e-commerce checkout.

  Tracks a running total, every item scanned, and a history of
  transactions so the most recent one can be voided.
  """

  def __init__(self, discount=0):
    # Start from a safe default so an invalid discount still leaves
    # the register in a usable state.
    self._discount = 0
    self.discount = discount
    self.total = 0
    self.items = []
    self.previous_transactions = []

  @property
  def discount(self):
    """Percentage off the total (e.g. 20 means 20% off)."""
    return self._discount

  @discount.setter
  def discount(self, value):
    # Discounts must be whole-number percentages from 0 to 100 inclusive.
    # bool is a subclass of int, so it is rejected explicitly.
    if isinstance(value, int) and not isinstance(value, bool) and 0 <= value <= 100:
      self._discount = value
    else:
      print("Not valid discount")

  def add_item(self, item, price, quantity=1):
    """Scan an item, adding its cost to the total and recording the transaction."""
    self.total = round(self.total + price * quantity, 2)
    # Each unit appears in items, so 3 books add "book" three times.
    self.items.extend([item] * quantity)
    self.previous_transactions.append(
      {"item": item, "price": price, "quantity": quantity}
    )

  def apply_discount(self):
    """Take the discount percentage off the current total."""
    if self.discount == 0:
      print("There is no discount to apply.")
      return

    self.total = round(self.total * (100 - self.discount) / 100, 2)
    print(f"After the discount, the total comes to ${self._format_money(self.total)}.")

  def void_last_transaction(self):
    """Undo the most recent add_item call, restoring the total and items."""
    if not self.previous_transactions:
      print("There is no transaction to void.")
      return

    last = self.previous_transactions.pop()
    self.total = round(self.total - last["price"] * last["quantity"], 2)

    # Remove one instance of the item per unit that was added,
    # starting from the end so earlier identical items are kept.
    for _ in range(last["quantity"]):
      for index in range(len(self.items) - 1, -1, -1):
        if self.items[index] == last["item"]:
          del self.items[index]
          break

  @staticmethod
  def _format_money(amount):
    # Whole-dollar totals drop the cents (800 instead of 800.0);
    # everything else shows two decimal places (6.30 instead of 6.3).
    return int(amount) if amount == int(amount) else f"{amount:.2f}"
