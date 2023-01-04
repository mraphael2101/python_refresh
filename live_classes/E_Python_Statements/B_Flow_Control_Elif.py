"""

In the same block:

- Python does not have a switch or case statement

- You can only ever have one else statement

- You can have multiple if conditions

- You can have 1..* elif conditions if you already have an if statement

"""


def main():
    paid = True
    account_status = 'Pending'

    if not paid:
        print("Overdraft initiated")
    elif paid and account_status == 'Pending':
        print("Enact Business Process 151")
    elif paid and account_status == 'Closure Requested':
        print("Enact Business Process 120")
    else:
        print("Debit Positive Balance")


if __name__ == '__main__':
    main()
