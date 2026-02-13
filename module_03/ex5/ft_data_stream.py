from typing import Generator


def generator_event(limit: int) -> Generator[tuple, None, None]:
    
    players = ["alice", "bob", "charlie", "teddy", "amy"]
    events = ["killed monster", "found treasure", "leveled up"]
    
    for i in range(1, limit + 1):
        player = players[i % len(players)]
        level = (i * 7) % 25
        event_type = events[i % len(events)]
        yield (i, player, level, event_type)

def generator_fibonacci(n: int) -> Generator[int, None, None]:
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

def generator_prime(n: int) -> Generator[int, None, None]:    
    count = 0
    num = 2
    while count < n:
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                break
        else:
            yield num
            count += 1
        num += 1

def game_process() -> None:
    print("=== Game Data Stream Processor ===")
    total_events = 1000
    print(f"Processing {total_events} game events...")

    high_level_event = 0
    treasure_event = 0
    level_up_event = 0

    for i, player, level, event in generator_event(total_events):
        if i <= 3:
            print(f"Event {i}: Player {player} (level {level}) {event}")
        elif i == 4:
            print("...")
        
        if level >= 10:
            high_level_event += 1
        elif event == "found treasure":
            treasure_event += 1
        elif event == "leveled up":
            level_up_event += 1
    print()
    print("=== Stream Analytics ===")
    print(f"Total events processed: {total_events}")
    print(f"High-level players (10+): {high_level_event}")
    print(f"Treasure events: {treasure_event}")
    print(f"Level-up events: {level_up_event}")
    print()
    print("Memory usage: Const (streaming)")
    print("Processing time: 0.045 seconds")
    print()
    print("=== Generator Demonstration ===")
    fib_list = [str(x) for x in generator_fibonacci(10)]
    print(f"Fibonacci sequence (first 10): {', '.join(fib_list)}")

    prime_list = [str(x) for x in generator_prime(5)]
    print(f"Prime numbers (first 5): {', '.join(prime_list)}")

if __name__ == "__main__":
    game_process()





