from delivery_strategies.abstract_delivery_strategy import AbsDeliveryStrategy
from delivery_strategies.util.calculated_delivery import calculated_delivery
from parse_to_currency import format_to_currency


class OpayDelivery(AbsDeliveryStrategy):

    percentage_to_increase_by = 2
    name = 'Opay'

    def calculate(self, minimum_delivery_cost: int) -> str:
        new_delivery_cost = calculated_delivery(minimum_delivery_cost, OpayDelivery.percentage_to_increase_by)
        return format_to_currency(number=new_delivery_cost)
