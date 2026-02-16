from typing import List, Dict, Set


def main() -> None:
    players = ["alice", "bob", "charlie", "diana"]
    scores = [2300, 1800, 2150, 2000]
    regions = ["north", "east", "central", "north"]
    inventory = [
        {"item": "sword", "rarity": "common"},
        {"item": "potion", "rarity": "rare"},
        {"item": "shield", "rarity": "common"},
        {"item": "gem", "rarity": "legendary"},
    ]
    print("=== Game Analytics Dashboard ===\n")
    high_score: List[str] = [p for p, s in zip(players, scores) if s > 2000]
    double_score: List[int] = [s * 2 for s in scores]
    active_player: List[str] = [players[i] for i in range(3)]
    print("=== List Comprehension Examples ===")
    print(f"High scorers (>2000): {high_score}")
    print(f"Scores doubled: {double_score}")
    print(f"Active players: {active_player}")
    print()
    print("=== Dict Comprehension Examples ===")
    players_score: Dict[str, int] = {p: s for p, s in zip(players, scores)}
    score_categories: Dict[str, int] = {
        "high": len([s for s in scores if s < 2100]),
        "medium": len([s for s in scores if 1900 <= s <= 2100]),
        "low": len([s for s in scores if s < 1900])
    }
    achievements_counts: Dict[str, int] = {"alice": 5, "bob": 3, "charlie": 7}
    print(f"Player scores: {players_score}")
    print(f"Scores categories: {score_categories}")
    print(f"Achievement counts: {achievements_counts}")
    print()
    print("=== Set Comprehension Examples ===")
    unique_regions: Set[str] = {r for r in regions}
    unique_rarities: Set[str] = {i["rarity"] for i in inventory}
    print(f"Unique players: {players}")
    print(f"Unique item rarities: {unique_rarities}")
    print(f"Active regions: {unique_regions}")
    print()
    print("=== Combined Analysis ===")
    top_performer = max(players_score, key=players_score.get)
    print(f"Total players: {len(players)}")
    print(f"Total unique item rarities: {len(unique_rarities)}")
    print(f"Average score: {sum(scores) / len(players)}")
    top_perf = top_performer
    points = players_score[top_perf]
    print(f"Top performer: {top_perf} ({points} points)")


if __name__ == "__main__":
    main()
