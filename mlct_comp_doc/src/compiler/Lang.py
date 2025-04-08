import json


class Lang:
    def __init__(self, pathLang):
        self.file = json.load(open(pathLang, "r", encoding="UTF-8"))

        # Загрузка блоков кода
        self.handlers = {}
        self.initHandlers()

        # Загрузка кастомных параметров
        self.custom = {}
        self.initCustom()

        self.variants = {}

        # Загрузка всех вариантов блоков
        self.initVariant("PLAYER_EVENT")
        self.initVariant("WORLD_EVENT")
        self.initVariant("PLAYER_ACTION")
        self.initVariant("VARIABLE_ACTION")
        self.initVariant("GAME_ACTION")
        self.initVariant("ARRAY_ACTION")
        self.initVariant("IF_GAME")
        self.initVariant("IF_VARIABLE")
        self.initVariant("IF_ENTITY")
        self.initVariant("IF_PLAYER")
        self.initVariant("SELECT_OBJECT")

    def initHandlers(self):
        for value in self.file["HANDLERS"]:
            noVariants = value.get("noVariants", False)
            self.handlers[value["name"]] = {
                "customName": value["customName"],
                "type": value["type"],
                "noVariants": noVariants
            }

    def initCustom(self):
        for value in self.file["CUSTOM"]:
            name = value.pop("name")
            # Меняем местами пользовательское имя и внешнее ммя
            values = {customName: name for name, customName in value["values"].items()}
            self.custom[name] = values

    def initVariant(self, handler):
        variants: list = self.file[handler]
        for variant in variants:
            variant["handler"] = handler
            self.variants[variant.pop("name")] = variant

    def initEnv(self, path):
        env = json.load(open(path, "r", encoding="UTF-8"))
        self.env = env

    def debug(self, name: str = None):
        def variants():
            return "Language param \"variants: {0}\"".format(self.variants)

        def handlers():
            return "Language param \"handlers: {0}\"".format(self.handlers)

        def customs():
            return "Language param \"customs: {0}\"".format(self.custom)

        def env():
            return "Language param \"env: {0}\"".format(self.env)

        if name is None:
            return [handlers(), variants(), customs(), env()]

