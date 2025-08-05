import json

filename = 'src/storage/saved_facts.json'


def dump_fact(saved_facts, fact):
    if fact not in saved_facts:
        saved_facts.append(fact)
        with open(filename, "w") as f:
            json.dump(saved_facts, f, indent=2)
        return "Fact saved successfully"
    return "This fact is already saved"


def load_Facts():
    try:
        with open(filename, "r") as f:
            saved = json.load(f)
            return saved
    except Exception:
        return []
