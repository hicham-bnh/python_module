from typing import Dict, List


def artifact_sorter(artifacts: List[Dict]) -> List[Dict]:
    result: List[Dict] = sorted(
        artifacts, key=lambda x: x['power'], reverse=True
        )
    return result


def power_filter(mages: List[Dict], min_power: int) -> List[Dict]:
    result: List[Dict] = list(filter(lambda x: x['power'] >= min_power, mages))
    return result


def spell_transformer(spells: List[str]) -> List[str]:
    result: List[str] = list(map(lambda x: f"* {x} *", spells))
    return result


def mage_stats(mages: List[Dict]) -> Dict:
    all_power: List = list(map(lambda x: x['power'], mages))
    final_sum: int = sum(all_power)
    len_power: int = len(mages)
    try:
        avg: float = final_sum/len_power
    except ZeroDivisionError as e:
        print(e)
    return {
        "max_power": max(mages, key=lambda x: x['power']),
        "min_power": min(mages, key=lambda x: x['power']),
        "avg_power": round(avg, 2)
    }


if __name__ == "__main__":
    artifacts = [
        {'name': 'Ice Wand', 'power': 75, 'type': 'armor'},
        {'name': 'Lightning Rod', 'power': 85, 'type': 'armor'},
        {'name': 'Wind Cloak', 'power': 114, 'type': 'relic'},
        {'name': 'Ice Wand', 'power': 86, 'type': 'armor'}
        ]
    mages = [
        {'name': 'Storm', 'power': 79, 'element': 'ice'},
        {'name': 'Phoenix', 'power': 68, 'element': 'fire'},
        {'name': 'Nova', 'power': 82, 'element': 'light'},
        {'name': 'Zara', 'power': 83, 'element': 'wind'},
        {'name': 'Storm', 'power': 73, 'element': 'earth'}
        ]
    spells = ['meteor', 'lightning', 'heal', 'flash']
    print("\nTesting artifact sorter...")
    test1 = artifact_sorter(artifacts)
    print(f"{test1[0]['name']} ({test1[0]['power']})", end=" ")
    print("comes before", end=" ")
    print(f"{test1[1]['name']} ({test1[1]['power']})")
    print()
    print("Testing spell transformer...")
    test2 = spell_transformer(spells)
    for ele in test2:
        print(ele, end=" ")
    print()
