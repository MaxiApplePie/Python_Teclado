accounts = {
    'checking': 1452.00,
    'savings': 2488.00
}


def add_balance(amount: float, name: str = 'checking') -> float:
    """updates the selected account and returns the amount"""
    print(accounts[name])
    accounts[name] += amount
    return accounts[name]


print(add_balance(300.00))
