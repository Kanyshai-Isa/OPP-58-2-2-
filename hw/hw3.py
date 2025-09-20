# class LibraryBook:
#
#     def __init__(self, title, is_taken, secret_code):
#         self.title = title
#         self._is_taken = is_taken
#         self.__secret_code = secret_code
#
#     def take_book(self, secret_code):
#         if secret_code == self.__secret_code and self._is_taken == 'no':
#             print(f"доступ к {self.title} разблокирован")
#         else:
#             print("код неверный или книга не в наличии")
#
#     def return_book(self):
#         if self._is_taken == 'no':
#             print(f' книга {self.title} возвращена')
#         else:
#             print(f' книга {self.title} не возвращена')
#
#
# book_1 = LibraryBook('Atlas Shrugged', 'no', '222')
#
# book_1.take_book('222')

from abc import ABC, abstractmethod

class PaymentSystem(ABC):

    @abstractmethod
    def pay(self, amount):
        pass

    @abstractmethod
    def refund(self, amount):
        pass

class CardPayment(PaymentSystem):

    def __init__(self, amount):
        self.amount = amount

    def pay(self, amount):
        print(f'{self.amount}$ были списана с карты')

    def refund(self, amount):
        print(f'{self.amount}$ поступило на карту')

class CryptoPayment:

    def __init__(self, amount):
        self.amount = amount

    def pay(self, amount):
        print(f'сумма {self.amount}$ была проведена через криптовалюто')

    def refund(self, amount):
        print(f'возврат {self.amount}$ через криптовалюту')

primer = CryptoPayment('56778')
primer.pay('')
primer.refund('')

primer_2 = CardPayment('34500')
primer_2.pay('')
primer_2.refund('')