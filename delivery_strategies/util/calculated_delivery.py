def calculated_delivery(minimum_delivery_cost: int, percentage_to_increase_by: float) -> float:
    """
    Reusable function to calculate expected delivery for different delivery strategies
    :param minimum_delivery_cost: the minimum delivery cost that is same for all delivery type
    :param percentage_to_increase_by:  the percentage a delivery should increase by
    :return:
    """
    delivery_cost_increased_by = minimum_delivery_cost * (percentage_to_increase_by / 100)
    new_delivery_cost = minimum_delivery_cost + delivery_cost_increased_by
    return new_delivery_cost
