"""
Example of greedy algorithm

Find minimum number of stations that will cover most
of the states
"""


states_needed = set(["mt", "wa", "or", "id", "nv", "ut", "ca", "az"])

stations = {
    "kone": set(["id", "nv", "ut"]),
    "ktwo": set(["wa", "id", "mt"]),
    "kthree": set(["or", "nv", "ca"]),
    "kfour": set(["nv", "ut"]),
    "kfive": set(["ca", "az"]),
}

final_stations = set()

while states_needed:
    best_station = None
    states_covered = set()
    for station, states in stations.items():
        coverage = states_needed & states
        if len(states_covered) < len(coverage):
            states_covered = coverage
            best_station = station

    states_needed -= states_covered
    final_stations.add(best_station)

print(final_stations)
assert final_stations == {"kone", "kthree", "kfive", "ktwo"}
