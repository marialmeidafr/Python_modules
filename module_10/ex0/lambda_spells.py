def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(artifacts, key=lambda a: a["power"], reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda m: m["power"] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda s: "* " + s + " *", spells))


def mage_stats(mages: list[dict]) -> dict:
    if not mages:
        return {"max_power": 0, "min_power": 0, "avg_power": 0.0}
    max_power = max(mages, key=lambda x: x["power"])
    min_power = min(mages, key=lambda x: x["power"])
    average_power = round(
        sum(map(lambda x: x["power"], mages)) / len(mages),
        2,
    )
    final_dict = {
        "max_power": max_power["power"],
        "min_power": min_power["power"],
        "avg_power": average_power,
    }
    return final_dict


def main() -> None:
    artifacts = [
        {"name": "Fire Staff", "power": 92},
        {"name": "Crystal Orb", "power": 85},
    ]
    spells = ["fireball", "heal", "shield"]

    art_sort = artifact_sorter(artifacts)
    print("Testing artifact sorter...")
    print(
        f"{art_sort[0]['name']} ({art_sort[0]['power']} power) "
        f"comes before {art_sort[1]['name']} ({art_sort[1]['power']} power)"
    )
    print()
    print("Testing spell transformer...")
    trans_spell = spell_transformer(spells)
    print(" ".join(trans_spell))


if __name__ == "__main__":
    main()
