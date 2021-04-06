from abc import ABC, abstractmethod


class AbsDeliveryStrategy(ABC):

    @property
    @abstractmethod
    def percentage_to_increase_by(self):
        return NotImplementedError

    @property
    @abstractmethod
    def name(self):
        return NotImplementedError

    @abstractmethod
    def calculate(self, minimum_delivery_cost) -> str:
        """
        calculate delivery cost
        :param minimum_delivery_cost: the minimum delivery cost regardless of the delivery type
        :return: string representation of the calculated delivery cost in naira
        """
        pass
