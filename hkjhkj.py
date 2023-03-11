from account import Account as Ac

class Bank():
    def __init__(self):
        self.__accounts = []

    def __whatnumberinaccountsbyid(self, id1: int):
        '''Возвращает номер в списке аккаунтов который соответствует счету в банке\n
        -1 если его нет.'''
        fgh = []
        id1 = int(id1)
        if len(self.__accounts) == 0:
            return -1
        for i in range(len(self.__accounts)):
            s = self.__accounts[i]
            fgh.append(s.id)
            if s.id == id1:
                return i
        print(fgh)
        return -1

    def create(self, overdraft: int):
        '''Создаёт аккаунт.\n
        Передаётся овердрафт,\n
        Возвращается масив в котором:\n
        1 элемент - id\n
        2 элемент - pin\n'''
        amom = Ac(overdraft)
        self.__accounts.append(amom)
        return amom.pin_id

    def add_money(self, monney: int, id: int):
        mass_id = self.__whatnumberinaccountsbyid(id)
        if mass_id == -1:
            return False
        ac = self.__accounts[mass_id]
        if ac.balance(monney):
            return True
        else:
            return False

    def get_money(self, monney: int, id: int, pin: int):
        mass_id = self.__whatnumberinaccountsbyid(id)
        if mass_id == -1:
            return False
        ac = self.__accounts[mass_id]
        mon = int("-"+str(monney))
        if ac.balance(mon, pin):
            return True
        else:
            return False

    def money(self, id: int):
        mass_id = self.__whatnumberinaccountsbyid(id)
        ac = self.__accounts[mass_id]
        return ac.balance

def test_new_and_get():
    sber = Bank()
    pin_id = sber.create(10)
    assert sber.money(pin_id[0]) == 0