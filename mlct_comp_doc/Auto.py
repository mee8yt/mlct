from src.compiler.Lang import Lang
import json

lang = Lang("src\\assets\\MlCodeLang.json")
links = json.load(open("links.json", "r", encoding="UTF-8"))
# actions = {i[0]: [links[i[0]], i[1]["customName"]] for i in lang.handlers.items() if i[1]["type"] in ["action", "condition"] and i[0] != "ELSE"}
variants = {i["customName"]: k for k, i in lang.variants.items() if lang.handlers[i["handler"]]["type"] in ["action", "condition"] and i["handler"] not in ["ELSE", "SELECT_OBJECT"]}


def createDescriptions(save_old: bool):
    if save_old:
        with open("descriptions.json", "r", encoding="UTF-8") as f:
            old = json.loads(f.read())
    else:
        old = {}

    fresult = {}
    for k, v in variants.items():
        langvar = lang.variants[v]
        handlerCustom = lang.handlers[langvar["handler"]]["customName"]
        variantCustom = langvar["customName"]
        customK = handlerCustom + "." + variantCustom
        args = {ak: "" for ak, i in langvar["args"].items()} if langvar.__contains__("args") else {}
        example = ""
        if old.__contains__(customK):
            args = old[customK]["descriptions"]
            example = old[customK]["example"]

        fresult[customK] = {"descriptions": args, "example": example}

    with open("descriptions.json", "w", encoding="UTF-8") as f:
        f.write(json.dumps(fresult, indent=4, ensure_ascii=False))
        print(json.dumps(fresult, indent=4))

def createGit():
    with open("descriptions.json", "r", encoding="UTF-8") as f:
        descriptions = json.loads(f.read())
    fresult = ""
    for k, v in variants.items():
        langvar = lang.variants[v]
        rargs = ""
        handlerCustom = lang.handlers[langvar["handler"]]["customName"]
        variantCustom = langvar["customName"]
        customK = handlerCustom + "." + variantCustom
        example = descriptions[customK]["example"]
        link = links[langvar["handler"]]
        result = ("## `" + handlerCustom + "." + variantCustom + f"();` [↩️]({link})" +
                  "\n" + "**Пример:**" +
                  "\n" + "```js"
                  "\n" + example + "\n```"
                  "\n" + "\n**Аргументы**:" + "\n")
        try:
            args = langvar["args" if not langvar.__contains__("parent") else "parent"]
            if isinstance(args, str):
                args = lang.variants[args]["args"]
        except KeyError:
            result += "*` пусто `*"
        else:
            result += ("\n" + "| **Имя** | **Тип** | **Описание** | **Синонимы** |" +
                       "\n" + "| :--- | --- | --- | --- |")
            for argName, argValue in args.items():
                type = "Значение" if argValue["type"] == "value" else "Переключатель"
                aliases = ""
                if argValue.__contains__("aliases"):
                    for alias in argValue["aliases"]:
                        aliases += "`" + alias + "`, "
                    aliases = aliases[:-2]
                else:
                    aliases = "`-`"
                description = example = descriptions[customK]["descriptions"][argName]
                rargs = rargs + "\n" + f"| `{argName}` | {type} | {description} | {aliases} |"
        print(result)
        print()
        fresult += "\n" + result

    with open("result.txt", "w", encoding="UTF-8") as f:
        f.write(fresult)

while True:
    ac = input("Чо делать пожелаешь\n\t[1] Сгенерировать словарь описаний\n\t[2] Сгенерировать готовое для гитхаба\n: ")
    if ac in ["1", "2"]:
        if ac == "1":
            createDescriptions(True)
            print("Готово")
            break
        if ac == "2":
            createGit()
            print("Готово, результат в 'result.txt', копируй и пихай в гитхаб")
            break
    else:
        print("АЛО БЛЯ 1 или 2")


pass

## `player.send();` [↩️](actions.md#действие-игрока---playeractionargs-)
# **Пример:**
# ```js
# player.send(["Игрок зашёл в игру", "Поприветствуем его"], sep=2);
# ```
#
# **Аргументы**:
# | **Имя** | **Тип** | **Описание** | **Синонимы** |
# | :--- | --- | --- | --- |
# | `texts` | Значение | Сообщение для отправки | `message` |
# | `switch` | Переключатель | Разделение между сообщениями | `separator`, `sep` |
