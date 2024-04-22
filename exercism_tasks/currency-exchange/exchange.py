"""Functions for calculating steps in exchaning currency.

Python numbers documentation: https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex

Overview of exchanging currency when travelling: https://www.compareremit.com/money-transfer-tips/guide-to-exchanging-currency-for-overseas-travel/
"""



def exchange_money(budget, exchange_rate):
    """
    This function  returns the value of the exchanged currency.

    :param budget: float - amount of money you are planning to exchange.
    :param exchange_rate: float - unit value of the foreign currency.
    :return: float - exchanged value of the foreign currency you can receive.
    """
    return budget / exchange_rate


def get_change(budget, exchanging_value):
    """
    This function returns the amount of money that *is left* from the budget.

    :param budget: float - amount of money you own.
    :param exchanging_value: float - amount of your money you want to exchange now.
    :return: float - amount left of your starting currency after exchanging.
    """
    return budget - exchanging_value


def get_value_of_bills(denomination, number_of_bills):
    """
    This function returns the total value of the bills the booth would give back.

    :param denomination: int - the value of a bill.
    :param number_of_bills: int - total number of bills.
    :return: int - calculated value of the bills.
    """
    return denomination * number_of_bills


def get_number_of_bills(amount, denomination):
    """
    This function returns the _number of currency bills_ that you can receive within the given _amount_.

    :param amount: float - the total starting value.
    :param denomination: int - the value of a single bill.
    :return: int - number of bills that can be obtained from the amount.
    """
    return amount // denomination


def get_leftover_of_bills(amount, denomination):
    """
    This function returns the _leftover amount_ that cannot be returned from your starting _amount_
given the denomination of bills.

    :param amount: float - the total starting value.
    :param denomination: int - the value of a single bill.
    :return: float - the amount that is "leftover", given the current denomination.
    """
    return amount % denomination


def get_actual_exchange_rate(exchange_rate, spread):
    """
    Calculate the actual exchange rate after including the spread.

    :param exchange_rate: float - the base unit value of the foreign currency.
    :param spread: float - percentage that is taken as an exchange fee.
    :return: float - the actual exchange rate after including the spread.
    """
    return exchange_rate * (1 + spread / 100)


def exchangeable_value(budget, exchange_rate, spread, denomination):
    """
    This function returns the maximum value of the new currency after calculating the *exchange rate*
plus the *spread*.

    :param budget: float - the amount of your money you are planning to exchange.
    :param exchange_rate: float - the unit value of the foreign currency.
    :param spread: int - percentage that is taken as an exchange fee.
    :param denomination: int - the value of a single bill.
    :return: int - maximum value you can get.
    """
    # Apply the spread by increasing the exchange rate by the given spread percentage
    actual_exchange_rate = get_actual_exchange_rate(exchange_rate, spread)
    # Calculate the money after the exchange
    exchanged_money = exchange_money(budget, actual_exchange_rate)
    # Calculate the number of bills according to denomination
    number_of_bills = get_number_of_bills(exchanged_money, denomination)
    # Return the total value of the bills of the specified denomination
    return get_value_of_bills(denomination, number_of_bills)
