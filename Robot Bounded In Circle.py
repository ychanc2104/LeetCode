# https://leetcode.com/problems/robot-bounded-in-circle/description/


# TC:O(N), SC:O(1)
def isRobotBounded(instructions: str) -> bool:
    # if direction is changed or back to initial pos => return True
    pos = [0, 0]
    direction = ((0, 1), (-1, 0), (0, -1), (1, 0))
    choose = 0
    for s in instructions:
        if s == 'G':
            pos[0] += direction[choose][0]
            pos[1] += direction[choose][1]
        elif s == 'L':
            choose += 1
        else:
            choose -= 1
        choose = choose % 4
    # print(pos, choose)
    return choose != 0 or pos == [0, 0]