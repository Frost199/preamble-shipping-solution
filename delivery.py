from delivery_strategies import AbsDeliveryStrategy
from recipient_info import RecipientInformation


class Delivery:
    minimum_delivery_cost = 20000

    def __init__(self, recipient_information: RecipientInformation, delivery_strategy: AbsDeliveryStrategy):
        self._cost = Delivery.minimum_delivery_cost
        self._recipient_information = recipient_information
        self._delivery_strategy = delivery_strategy

    def calculate_delivery(self) -> str:
        """
        calculates the delivery for a recipient
        :return:
        """
        self._cost = self._delivery_strategy.calculate(Delivery.minimum_delivery_cost)
        return self._cost

    @property
    def show(self):
        return f"""
Your delivery details:

Recipient:        {self._recipient_information.name}
Phone Number:     {self._recipient_information.phone_number}
Delivery Address: {self._recipient_information.address}

===========================================================

Delivery Type:    {self._delivery_strategy.name}
Cost Increase:    {self._delivery_strategy.percentage_to_increase_by}% 
Total Cost:       {self._cost}
"""
