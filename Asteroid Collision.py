# https://leetcode.com/problems/asteroid-collision/


# stack, TC:O(n), SC:O(1) if don't take result into account, O(n)
def asteroidCollision(asteroids):
    # 5,10,-5
    # -2,-1,1,2
    stack = []
    for asteroid in asteroids:
        cur = asteroid
        while stack and cur < 0 and stack[-1] * cur < 0:
            # collide
            pre = stack.pop()
            if abs(pre) > abs(cur):
                # cur explode
                cur = pre
            elif abs(pre) == abs(cur):
                cur = 0
            else:
                cur = cur
        if cur != 0:
            stack.append(cur)
    return stack

# clean stack, TC:O(n), SC:O(1) if don't take result into account, O(n)
def asteroidCollision2(asteroids):
    # 5,10,-5
    # -2,-1,1,2
    stack = []
    for cur in asteroids:
        while stack and cur<0<stack[-1]:
            # collide
            if cur+stack[-1]==0:
                # two asteroid exploded, end loop
                stack.pop()
                break
            elif stack[-1] < -cur:
                # stack[-1] explode, cur preserve, continue loop
                stack.pop()
                continue
            else:
                # cur explode, stack[-1] preserve, end loop
                break
        else:
            stack.append(cur)
    return stack


# clean stack, TC:O(n), SC:O(1) if don't take result into account, O(n)
def asteroidCollision3(asteroids):
    # collide, only when left is positive and right is negative
    stack = []
    for asteroid in asteroids:
        while stack and stack[-1] > 0 and asteroid < 0:
            # collide
            if -asteroid > stack[-1]:
                stack.pop()
            elif -asteroid == stack[-1]:
                stack.pop()
                break # both explode
            else:
                break # do not append
        else:
            stack.append(asteroid)
    return stack