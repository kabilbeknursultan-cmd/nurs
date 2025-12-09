# task1_singleton/configuration_manager.py

class ConfigurationManager:
    """
    Singleton үлгісін қолданатын конфигурация менеджері.
    Жүйеде тек бір ғана конфигурация данасының болуын қамтамасыз етеді.
    """
    _instance = None

    # 1. Конфигурация параметрлерін сақтауға арналған сөздік
    configurations = {}

    def __new__(cls):
        # Егер дана әлі жасалмаған болса, жаңасын жасайды
        if cls._instance is None:
            cls._instance = super(ConfigurationManager, cls).__new__(cls)
        # Әрқашан бұрыннан бар жалғыз дананы қайтарады
        return cls._instance

    def load_config(self, key, value):
        """Конфигурация параметрін сөздікке қосады/жаңартады."""
        print(f"Конфигурация жүктелді: {key} = {value}")
        self.configurations[key] = value

    def get_config(self, key):
        """Белгілі бір конфигурация параметрін қайтарады."""
        return self.configurations.get(key, "Кілт табылмады")


# --- Демонстрация ---
if __name__ == "__main__":
    print("### Тапсырма 1: Singleton үлгісін тексеру ###")

    # Екі дананы жасауға тырысу
    config1 = ConfigurationManager()
    config2 = ConfigurationManager()

    # 4. Бірдей нысанға сілтеме жасайтынын тексеру
    print(f"\nconfig1 мен config2 бір нысан ба? (config1 is config2): {config1 is config2}")
    print(f"config1 ID: {id(config1)}")
    print(f"config2 ID: {id(config2)}")

    # config1 арқылы параметр орнату
    config1.load_config("API_KEY", "ABC-123-XYZ")
    config1.load_config("DB_HOST", "localhost:5432")

    # config2 арқылы параметрді оқу (бірдей деректерді бөлісуді тексеру)
    print("\nconfig2 арқылы оқу:")
    api_key = config2.get_config("API_KEY")
    db_host = config2.get_config("DB_HOST")

    print(f"API_KEY (config2): {api_key}")
    print(f"DB_HOST (config2): {db_host}")

    # config2 арқылы жаңа параметр орнату
    config2.load_config("TIMEOUT", 30)

    # config1 арқылы жаңа параметрді оқу
    print("\nconfig1 арқылы оқу:")
    timeout = config1.get_config("TIMEOUT")
    print(f"TIMEOUT (config1): {timeout}")