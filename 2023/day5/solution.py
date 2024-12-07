import multiprocessing


def get_input_lines_from_file():
    with open("input", "r") as input_file:
        return input_file.read().splitlines()


def part_one() -> int:
    maps = create_mapping()
    seeds = [num for num in map(lambda seed: int(seed), lines[0].split(': ')[1].split(" "))]
    source_type = "seed"
    locations = []
    for seed in seeds:
        locations.append(find_destination_for_source(seed, source_type, maps, {}))
    return min(locations)


def find_destination_for_source(source: int, source_type: str, maps, cache) -> int:
    destination_type = maps["to"].get(source_type)
    if not destination_type:
        return source
    map_key_name = [r for r in filter(lambda x: x == f"{source_type}-to-{destination_type}", maps.keys())][0]
    destination = source
    for range_index, val_range in enumerate(maps[map_key_name]["source"]["ranges"]):
        if source in val_range:
            range_diff = source - val_range.start
            destination = maps[map_key_name]["destination"]["ranges"][range_index][range_diff]
            cache.setdefault(source_type, {})[source] = destination
            break
    # print(f"{source} {source_type} corresponds to {destination} {destination_type}")
    return find_destination_for_source(destination, destination_type, maps, cache)


def part_two() -> int:
    seeds = [num for num in map(lambda seed: int(seed), lines[0].split(': ')[1].split(" "))]
    maps = create_mapping()
    locations = []
    cache = {}
    for i in range(0, len(seeds), 2):
        print(i, seeds[i], seeds[i + 1], range(seeds[i], seeds[i] + seeds[i + 1]))
        with multiprocessing.Pool(processes=4) as pool:
            locations.extend(pool.starmap(find_destination_for_source,
                                          [(seed, "seed", maps, cache) for seed in range(seeds[i], seeds[i] + seeds[i + 1])]))
    return min(locations)


def create_mapping():
    maps = {"to": {}}
    line_index = 2
    current_map = ""
    while line_index < len(lines):
        if lines[line_index].endswith("map:"):
            current_map = lines[line_index].split(" ")[0]
            maps[current_map] = dict.fromkeys(["source", "destination"])
            for key in maps[current_map].keys():
                maps[current_map][key] = {"ranges": []}
            source, _, destination = current_map.split("-")
            maps["to"][source] = destination
        elif lines[line_index]:
            destination_range_start, source_range_start, range_length = (
                val for val in map(lambda x: int(x), lines[line_index].split(" ")))
            if not maps[current_map]["source"]["ranges"]:
                maps[current_map]["source"]["ranges"] = []
            maps[current_map]["source"]["ranges"].append(range(source_range_start, source_range_start + range_length))
            if not maps[current_map]["destination"]["ranges"]:
                maps[current_map]["destination"]["ranges"] = []
            maps[current_map]["destination"]["ranges"].append(
                range(destination_range_start, destination_range_start + range_length))
        line_index += 1
    return maps


if __name__ == "__main__":
    lines = get_input_lines_from_file()
    print(part_one())
    print(part_two())
