# task5_integration/messaging_system.py
from abc import ABC, abstractmethod
import time


# =======================================================
# 1. SINGLETON ҮЛГІСІ: RateLimiter
# =======================================================
class RateLimiter:
    """
    Жалғыз дананы қамтамасыз ететін хабарлама жіберу жылдамдығын шектеуші.
    """
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(RateLimiter, cls).__new__(cls)
            cls._instance.last_sent_time = 0
            cls._instance.delay = 0.5  # Хабарламалар арасындағы ең аз кідіріс
        return cls._instance

    def check_limit(self):
        """Жіберуге рұқсат етілгенін тексереді."""
        current_time = time.time()
        if current_time - self.last_sent_time >= self.delay:
            self.last_sent_time = current_time
            return True
        else:
            return False


# =======================================================
# 2. STRATEGY ҮЛГІСІ: Форматтау Стратегиясы
# =======================================================
class MessageFormatter(ABC):
    @abstractmethod
    def format(self, content):
        pass


class HtmlFormatter(MessageFormatter):
    def format(self, content):
        return f"<html><body><h1>{content}</h1></body></html>"


class PlainTextFormatter(MessageFormatter):
    def format(self, content):
        return f"--- {content} ---"


# =======================================================
# 3. FACTORY ҮЛГІСІ: Тасымалдау Фабрикасы
# =======================================================

class TransportSender(ABC):
    @abstractmethod
    def send(self, message):
        pass


class EmailSender(TransportSender):
    def send(self, message):
        print(f"[EMAIL] Жіберілді: {message}")


class SmsSender(TransportSender):
    def send(self, message):
        print(f"[SMS] Жіберілді: {message}")


class TransportFactory:
    """Хабарлама түріне негізделген сәйкес Тасымалдаушыны жасайды."""

    def create_sender(self, transport_type: str) -> TransportSender:
        transport_type = transport_type.lower()
        if transport_type == "email":
            return EmailSender()
        elif transport_type == "sms":
            return SmsSender()
        else:
            raise ValueError(f"Белгісіз тасымалдау түрі: {transport_type}")


# =======================================================
# БІРІКТІРІЛГЕН КОНТЕКСТ
# =======================================================
class MessagingService:
    """
    Singleton RateLimiter, Strategy Formatter және Factory Transport-ты біріктіреді.
    """

    def __init__(self, factory: TransportFactory, formatter: MessageFormatter):
        self._factory = factory
        self._formatter = formatter
        self._rate_limiter = RateLimiter()  # Singleton данасын алады

    def set_formatter(self, formatter: MessageFormatter):
        """Strategy-ді ауыстыру."""
        self._formatter = formatter

    def dispatch_message(self, transport_type: str, raw_content: str):

        # 3. Singleton: Жіберу жылдамдығын тексеру
        if not self._rate_limiter.check_limit():
            print(f"\n[Айрықша жағдай] Жылдамдық шектеуі: {transport_type} жіберуге тым ерте.")
            return

        print("\n[Жаңа Хабарлама]")

        # 2. Strategy: Мазмұнды форматтау
        formatted_message = self._formatter.format(raw_content)
        print(f"Форматтаушы: {self._formatter.__class__.__name__}")

        # 1. Factory: Жіберушіні алу
        try:
            sender = self._factory.create_sender(transport_type)
            # Жіберу
            sender.send(formatted_message)
        except ValueError as e:
            print(f"[Қате] {e}")


# --- Демонстрация ---
if __name__ == "__main__":
    print("### Тапсырма 5: Үлгілерді біріктіру (Messaging System) ###")

    factory = TransportFactory()

    # Бастапқы Strategy (PlainText)
    service = MessagingService(factory, PlainTextFormatter())

    # 1. Әртүрлі арналарға жіберу (Factory)
    service.dispatch_message("email", "Жаңа есеп беру қолжетімді")
    service.dispatch_message("sms", "Код: 123456")

    # 2. Strategy-ді ауыстыру
    service.set_formatter(HtmlFormatter())
    service.dispatch_message("email", "Сәлемдеме расталды")

    # 3. Singleton-ды тексеру (Жылдамдық шектеуі)
    print("\n--- Жылдамдық шектеуін тексеру (0.5 секунд күту) ---")
    service.dispatch_message("sms", "Тез жіберу әрекеті 1")
    service.dispatch_message("sms", "Тез жіберу әрекеті 2")  # Бұл сәтсіз болуы керек

    # RateLimiter-дің жалғыз дана екенін тексеру:
    limiter1 = RateLimiter()
    limiter2 = RateLimiter()
    print(f"\nRateLimiter1 мен RateLimiter2 бір нысан ба?: {limiter1 is limiter2}")  # True болуы керек