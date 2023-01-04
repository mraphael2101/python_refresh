"""
We often only want certain code to execute when a specific condition is met
which is where code flow control comes in:

    a) Control Flow syntax makes use of colons and indentation (whitespace)
    b) This indentation system is crucial to Python and distinguishes it
    from other languages
"""


def main():
    paid = True

    if not paid:
        print("Overdraft initiated")
    else:
        print("Debit the Positive Balance")


if __name__ == '__main__':
    main()
