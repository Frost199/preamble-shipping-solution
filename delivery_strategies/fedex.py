from delivery_strategies.abstract_delivery_strategy import AbsDeliveryStrategy
from delivery_strategies.util.calculated_delivery import calculated_delivery
from parse_to_currency import format_to_currency


class FedExDelivery(AbsDeliveryStrategy):

    percentage_to_increase_by = 5
    name = 'FedEx'

    def calculate(self, minimum_delivery_cost: int) -> str:
        new_delivery_cost = calculated_delivery(minimum_delivery_cost, FedExDelivery.percentage_to_increase_by)
        return format_to_currency(number=new_delivery_cost)
