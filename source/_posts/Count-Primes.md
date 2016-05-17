title: 素数的个数
create_time: 2016/05/17 21:03:46
tags:
- Hash Table
- Math
categories:
- leetcode
- C++

---
## [Count Primes](https://leetcode.com/problems/count-primes/)
> Description:
> Count the number of prime numbers less than a non-negative number, n.

### 实现思路
原文里面已经有答案，看图片即可得出思路。
![看图](http://7xl4we.com1.z0.glb.clouddn.com/Sieve_of_Eratosthenes_animation.gif)

### [Code](https://github.com/Finalcheat/leetcode/blob/master/src/Count-Primes.cpp)
```
class Solution {
    public:
        int countPrimes(int n) {
            std::vector<bool> isPrime(n);
            for (int i = 2; i < n; ++i) {
                isPrime[i] = true;
            }
            for (int i = 2; i * i < n; ++i) {
                if (!isPrime[i]) {
                    continue;
                }
                for (int j = i * i; j < n; j += i) {
                    isPrime[j] = false;
                }
            }
            int count = 0;
            for (int i = 2; i < n; i++) {
                if (isPrime[i]) {
                    ++count;
                }
            }
            return count;
        }
};
```
