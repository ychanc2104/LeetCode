# https://leetcode.com/problems/minimum-health-to-beat-game/

# greedy, TC:O(N), SC:O(1)
def minimumHealth(damage: List[int], armor: int) -> int:
    return sum(damage) + 1 - min(armor, max(damage))