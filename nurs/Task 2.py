# task2_strategy/sorting_processor.py
from abc import ABC, abstractmethod


# 1. Негізгі Стратегия Класы
class SortingStrategy(ABC):
    """Сұрыптау әдісіне арналған базалық интерфейс."""

    @abstractmethod
    def sort(self, data):
        pass


# 2. Нақты Стратегия: QuickSort
class QuickSortStrategy(SortingStrategy):
    def sort(self, data):
        # Python-дағы list.sort() әдетте Timsort-ты (гибридті) қолданады,
        # бірақ біз мұны тез сұрыптаудың өкілі ретінде пайдаланамыз.
        sorted_data = sorted(data)
        print(" -> QuickSort стратегиясы қолданылды.")
        return sorted_data


# 2. Нақты Стратегия: BubbleSort
class BubbleSortStrategy(SortingStrategy):
    def sort(self, data):
        n = len(data)
        arr = list(data)  # Көшірмесін жасау
        for i in range(n):
            for j in range(0, n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        print(" -> BubbleSort стратегиясы қолданылды.")
        return arr


# 3. Context (DataProcessor)
class DataProcessor:
    """Деректерді өңдеуші, ол стратегияны қабылдайды."""

    def __init__(self, strategy: SortingStrategy):
        self._strategy = strategy

    @property
    def strategy(self) -> SortingStrategy:
        return self._strategy

    @strategy.setter
    def strategy(self, strategy: SortingStrategy):
        """Жұмыс уақытында стратегияны ауыстыруға мүмкіндік береді."""
        self._strategy = strategy

    def process(self, data):
        """Таңдалған стратегия арқылы деректерді өңдейді."""
        print(f"Бастапқы деректер: {data}")
        result = self._strategy.sort(data)
        print(f"Сұрыпталған деректер: {result}")
        return result


# --- Демонстрация ---
if __name__ == "__main__":
    print("### Тапсырма 2: Strategy үлгісін тексеру ###")

    test_data = [9, 1, 5, 2, 8, 3]

    # 4. 1-стратегия: QuickSort
    processor = DataProcessor(QuickSortStrategy())
    print("\n--- QuickSort қолдану ---")
    processor.process(test_data)

    # 4. 2-стратегия: Жұмыс уақытында стратегияны ауыстыру
    processor.strategy = BubbleSortStrategy()
    print("\n--- BubbleSort-қа ауысу ---")
    processor.process(test_data)