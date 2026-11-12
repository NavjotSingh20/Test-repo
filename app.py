
def calculate_total(price, quantity):
    """Calculate the total cost of an order."""
    if price < 0 or quantity < 0:
        raise ValueError("Price and quantity cannot be negative")

    return price * quantity


def is_palindrome(text):
    """Check whether text is a palindrome."""
    cleaned_text = text.replace(" ", "").lower()
    return cleaned_text == cleaned_text[::-1]


def get_delivery_status(days_late):
    """Return delivery status based on the number of days late."""
    if days_late < 0:
        raise ValueError("Days late cannot be negative")

    if days_late == 0:
        return "On Time"
    elif days_late <= 2:
        return "At Risk"
    else:
        return "Delayed"
