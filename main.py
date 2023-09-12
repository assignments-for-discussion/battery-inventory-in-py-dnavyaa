# Constants
RATED_CAP = 120  # Rated capacity of a new battery
HEALTHY_THRESH = 80  # SoH percentage threshold for healthy batteries
EXCHANGE_THRESH = 63  # SoH percentage threshold for exchange batteries

def count_batteries_by_health(present_capacities):
    counts = {
        "healthy": 0,
        "exchange": 0,
        "failed": 0
    }

    # Loop through present capacities and classify batteries
    for capacity in present_capacities:
        soh_percentage = (capacity / RATED_CAP) * 100  # Calculate State of Health (SoH) percentage
        
        if soh_percentage > HEALTHY_THRESH:
            counts["healthy"] += 1
        elif HEALTHY_THRESHOLD >= soh_percentage >= EXCHANGE_THRESH:
            counts["exchange"] += 1
        else:
            counts["failed"] += 1

    return counts

def test_bucketing_by_health():
    print("Counting batteries by SoH...\n")
    present_capacities = [115, 118, 80, 95, 91, 72, 120, 0]
    counts = count_batteries_by_health(present_capacities)
    
    # Print Alert if batteries are at minimum or maxium capacities 
    for index, capacity in enumerate(present_capacities):
        if capacity == 0:
            print(f"Alert:This Battery capacity is at the minimum (0 Ah) at index {index}.")
        elif capacity == RATED_CAP:
            print(f"Alert: This Battery capacity is at the maximum (120 Ah) at index {index}.")

    # Assert the counts
    assert counts["healthy"] == 3
    assert counts["exchange"] == 3
    assert counts["failed"] == 2

    # Print the counts for all type of batteries 
    print("Healthy batteries:", counts["healthy"])
    print("Exchange batteries:", counts["exchange"])
    print("Failed batteries:", counts["failed"])
    print("Done counting :)")

if __name__ == '_main_':
    test_bucketing_by_health()
