def main() -> None:
    print("=== Achievement Tracker System ===\n")

    p_alice = {'first_kill', 'level_10', 'treasure_hunter', 'speed_demon'}
    p_bob = {'first_kill', 'level_10', 'boss_slayer', 'collector'}
    p_charlie = {'level_10', 'treasure_hunter', 'boss_slayer', 'speed_demon',
                 'perfectionist'}
    print(f"Player alice achievements: {p_alice}")
    print(f"Player bob achievements: {p_bob}")
    print(f"Player charlie achievements: {p_charlie}")
    print()
    print("=== Achievement Analytics ===\n")

    all_achievements = p_alice | p_bob | p_charlie
    total_achievements = len(all_achievements)
    print(f"All unique achievements: {all_achievements}")
    print(f"Total unique achievements: {total_achievements}")
    print()
    common = p_alice & p_bob & p_charlie
    only_alice = p_alice - p_bob - p_charlie
    only_bob = p_bob - p_alice - p_charlie
    only_charlie = p_charlie - p_alice - p_bob
    dif = only_alice | only_bob | only_charlie
    print(f"Common to all players: {common}")
    print(f"Rare achievements (1 player): {dif}")
    print()
    com_alice_bob = p_alice & p_bob
    dif_alice_bob = p_alice - p_bob
    dif_bob_alice = p_bob - p_alice
    print(f"Alice vs Bob commom: {com_alice_bob}")
    print(f"Alice unique: {dif_alice_bob}")
    print(f"Bob unique: {dif_bob_alice}")


if __name__ == "__main__":
    main()
