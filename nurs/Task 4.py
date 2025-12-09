# task4_observer/stock_observer.py
from abc import ABC, abstractmethod


# 2. Observer (Бақылаушы) Интерфейсі
class Investor(ABC):
    """Барлық инвесторлардың іске асыруы қажет интерфейс."""

    @abstractmethod
    def update(self, stock_name, price):
        pass


# 1. Subject (Нысан) Класы
class Stock:
    """Баға өзгерген кезде Бақылаушыларды хабардар етеді."""

    def __init__(self, name, initial_price):
        self._name = name
        self._price = initial_price
        self._observers = []

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, new_price):
        """Баға өзгергенде, барлық тіркелген бақылаушыларға хабарлайды."""
        if new_price != self._price:
            self._price = new_price
            print(f"\n[{self._name}] Жаңа баға: {self._price}")
            self.notify()

    # 6. attach(observer)
    def attach(self, observer: Investor):
        """Бақылаушыны тізімге қосады."""
        print(f"{observer.__class__.__name__} {self._name} акциясына тіркелді.")
        self._observers.append(observer)

    # 7. detach(observer)
    def detach(self, observer: Investor):
        """Бақылаушыны тізімнен жояды."""
        print(f"{observer.__class__.__name__} тіркеуден шығарылды.")
        self._observers.remove(observer)

    # 8. notify()
    def notify(self):
        """Барлық тіркелген бақылаушыларды жаңарту туралы хабардар етеді."""
        for observer in self._observers:
            observer.update(self._name, self._price)


# 3. Нақты Бақылаушы: Bullish Investor
class BullishInvestor(Investor):
    """Баға өскенде сатып алуға дайын инвестор."""

    def update(self, stock_name, price):
        if price > 100:
            print(f"BullishInvestor: {stock_name} бағасы жоғары, {price}$! Көбірек сатып алуға дайынмын.")
        else:
            print(f"BullishInvestor: {stock_name} бағасы {price}$. Күтемін...")


# 3. Нақты Бақылаушы: Bearish Investor
class BearishInvestor(Investor):
    """Баға төмендегенде сатуға дайын инвестор."""

    def update(self, stock_name, price):
        if price < 90:
            print(f"BearishInvestor: {stock_name} бағасы төмен, {price}$! Сату мүмкіндігі!")
        else:
            print(f"BearishInvestor: {stock_name} бағасы {price}$. Тұрақты.")


# --- Демонстрация ---
if __name__ == "__main__":
    print("### Тапсырма 4: Observer үлгісін тексеру ###")

    # Нысанды жасау
    tesla_stock = Stock("TESLA", 95.00)

    # Бақылаушыларды жасау
    bull = BullishInvestor()
    bear = BearishInvestor()

    # Тіркеу
    tesla_stock.attach(bull)
    tesla_stock.attach(bear)

    # 4. Бағаны өзгерту 1: Бағаны жоғарылату (Bullish реакциясын тудырады)
    print("\n--- Баға өзгерісі 1: Бағаны 95.00 -> 105.00 дейін өзгерту ---")
    tesla_stock.price = 105.00

    # Тіркеуден шығару
    print("\n--- Bearish Investor-ды тіркеуден шығару ---")
    tesla_stock.detach(bear)

    # 4. Бағаны өзгерту 2: Бағаны төмендету (Тек Bullish реакциясы қалады)
    print("\n--- Баға өзгерісі 2: Бағаны 105.00 -> 85.00 дейін өзгерту ---")
    tesla_stock.price = 85.00