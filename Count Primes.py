# https://leetcode.com/problems/count-primes/description/

# Sieve of Eratosthenes, TC:O(sqrt(N)loglogN), O(n/2+n/+n/5+...+n/last prime). This is bounded by O(loglogN), SC:O(N)
def countPrimes(n: int) -> int:
    if n <= 2: return 0
    isPrime = [True] * n
    isPrime[0] = False
    isPrime[1] = False
    for num in range(2, int(n ** 0.5) + 1):  # TC:O(sqrt(n)*)
        if isPrime[num]:
            for i in range(num * num, n, num):
                isPrime[i] = False
    return sum(isPrime)