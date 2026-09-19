import json

new = {}
source = json.load(open('src/assets/MlCodeLang.json'))
del source["HANDLERS"]
del source["CUSTOM"]

for handler, variants in source.items():
    new_variants = {}
    for variant in variants:
        unit = {
            "sign": {
                "ru": "",
                "en": "",
                "uk": None,
                "de": None
            }
        }
        name = variant['name']
        if (args := variant.get('args')) is not None:
            v: dict
            new_args = {}
            for k, v in args.items():
                if v.get("type") == "switch":
                    l: list = v["states"]
                    ex = len(l) * [""]
                    new_args[k] = {
                        "ru": ex,
                        "en": ex,
                        "uk": None,
                        "de": None
                    }
            if len(new_args) > 0:
                unit["args"] = new_args
        new_variants[name] = unit
    new[handler] = new_variants

with open('mlcode_translates.json', 'w') as f:
    json.dump(new, f, indent="\t", ensure_ascii=False)
input("done")