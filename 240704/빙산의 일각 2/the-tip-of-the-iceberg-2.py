n = 7
ice = [6, 4, 5, 2, 7, 1, 8]
water_level = 5

submerged = [height > water_level for height in ice]
print(submerged)  # Output: [True, False, False, False, True, False, True]

def count_ice_chunks(ice, water_level):
    submerged = [height > water_level for height in ice]
    count = 0
    i = 0
    while i < n:
        if submerged[i]:
            count += 1
            while i < n and submerged[i]:
                i += 1
        i += 1
    return count

# Example usage
water_level = 5
print(count_ice_chunks(ice, water_level))  # Output for water_level = 5