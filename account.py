import random
from eazy_encrypter import main

class Account:
    """Описывает банковский счет с положительным балансом."""

    def __init__(self, overdrfat: int):
        self.__overdraft = overdrfat
        self.__balance = 0
        self.__id = random.randint(999, 9999)
        self.__pin = main.new_pin()

    @property
    def balance(self) -> int:
        """Возвращает баланс счета."""
        kjjj = self.__balance
        return kjjj

    @property
    def pin(self) -> int:
        """Возвращает пин-код счета."""
        il = self.__pin
        return il

    @property
    def pin_id(self) -> list:
        '''[id,pin]'''
        gfhhfg = []
        gfhhfg.append(self.id)
        gfhhfg.append(self.pin)
        return gfhhfg

    @property
    def id(self) -> int:
        """Возвращает id счета."""
        return self.__id


    @balance.setter
    def balance(self, amount: int, pin: int):
        """Задает баланс."""
        if self.__balance + amount >= int("-"+str(self.__overdraft)) and pin == self.__pin:
            self.__balance =+ amount
            return True
        else:
            return False

if __name__ == "__main__":
    account = Account(10)
    assert account.balance == 0

    account.balance -= 10
    assert account.balance == -10

    account.balance -= 10
    assert account.balance == -10