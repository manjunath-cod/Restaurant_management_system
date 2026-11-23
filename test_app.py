# test_app.py - Automated tests for Jenkins (no keyboard input needed)

from unittest.mock import patch
from app import take_order

def test_order():
    # Simulate: pick Burger x2, Coffee x1, then 0 to finish
    fake_inputs = ["1", "2", "5", "1", "0"]

    with patch("builtins.input", side_effect=fake_inputs):
        take_order()

    print("\n--- TEST PASSED ---")

if __name__ == "__main__":
    test_order()
