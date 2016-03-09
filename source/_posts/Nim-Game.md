title: 取石子游戏
create_time: 2016/03/06 15:17:18
tags:
- Math
categories:
- leetcode
- C++

---
## [Nim Game](https://leetcode.com/problems/nim-game/)
> You are playing the following Nim Game with your friend: There is a heap of stones on the table, each time one of you take turns to remove 1 to 3 stones.
> The one who removes the last stone will be the winner. You will take the first turn to remove the stones.
> Both of you are very clever and have optimal strategies for the game. Write a function to determine whether you can win the game given the number of stones in the heap.
> For example, if there are 4 stones in the heap, then you will never win the game: no matter 1, 2, or 3 stones you remove, the last stone will always be removed by your friend.

### 实现思路
每个人一次只能取1-3石子，则无论对方取多少，我方都能保证双方取走的石子之和为4，而题目要求是我方先取，所以只要保证数字不被4整除就可以了。
数字不被4整除，我方先取走数字除以4得到的余数，则剩下的石头数是4的倍数，接着在每轮的取石子过程中，只要我方与对方取走石子之和为4则必胜。

### [Code](https://github.com/Finalcheat/leetcode/blob/master/src/Nim-Game.cpp)
```
class Solution {
    public:
        bool canWinNim(int n) {
            return n % 4 != 0;
        }
};
```
