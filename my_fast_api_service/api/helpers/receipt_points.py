from pydanctic_models.receipt_process import ReceiptProcess
from pydanctic_models.item import ItemCreate
from typing import List, Union
from datetime import date, time
import math


def retrieve_receipt(
    id: str, receipts: List[ReceiptProcess]
) -> Union[ReceiptProcess, None]:

    if receipts.get(id):
        return receipts[id]

    return None


def get_alpha_char_points(retailer_name: str) -> int:
    count = 0

    for char in retailer_name:
        if char.isalnum():
            count += 1

    return count


def get_total_round_dollar_points(total: str) -> int:
    if float(total) == round(float(total)):
        return 50

    return 0


def get_total_is_a_multiple_of_one_fourth_points(total: str) -> int:
    if (float(total) % 0.25) == 0.0:
        return 25

    return 0


def get_total_every_two_item_points(items: List[ItemCreate]) -> int:
    count = 0

    for i in range(len(items)):
        if i % 2 != 0:
            count += 5

    return count


def get_length_of_item_description_points(items: List[ItemCreate]) -> int:
    count = 0

    for item in items:
        description_length = item.shortDescription.strip()

        if len(description_length) % 3 == 0:
            result = math.ceil(float(item.price) * 0.2)

            count += result

    return count


def get_purchaseDate_points(date: date) -> int:
    if date.day % 2 != 0:
        return 6

    return 0


def get_purchaseTime_points(purchaseTime: time) -> int:
    start_time = time(14, 0)
    end_time = time(16, 0)

    if start_time < purchaseTime < end_time:
        return 10

    return 0


def get_my_points(receipt: ReceiptProcess) -> int:
    alpha_char_points = get_alpha_char_points(receipt.retailer)
    total_round_dollar_points = get_total_round_dollar_points(receipt.total)
    total_is_a_multiple_of_one_fourth_points = (
        get_total_is_a_multiple_of_one_fourth_points(receipt.total)
    )
    total_every_two_item_points = get_total_every_two_item_points(receipt.items)
    length_of_item_description_points = get_length_of_item_description_points(
        receipt.items
    )
    purchaseDate_points = get_purchaseDate_points(receipt.purchaseDate)
    purchaseTime_points = get_purchaseTime_points(receipt.purchaseTime)

    sum_of_points = (
        alpha_char_points
        + total_round_dollar_points
        + total_is_a_multiple_of_one_fourth_points
        + total_every_two_item_points
        + length_of_item_description_points
        + purchaseDate_points
        + purchaseTime_points
    )

    return sum_of_points
