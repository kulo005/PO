from abc import ABC, abstractmethod


class ControllerPay(ABC):

    @abstractmethod
    def calculate_pay(self):
        pass


class ChildPaySystem(ControllerPay):

    def calculate_pay(age):
        return age * 4

    def calculate_relief(pay):
        if pay < 200:
            return (pay / 2)
        else:
            return (pay / 2).__add__(20)


class AdultPaySystem(ChildPaySystem, ControllerPay):

    def calculate_pay(age):
        return age * 6
