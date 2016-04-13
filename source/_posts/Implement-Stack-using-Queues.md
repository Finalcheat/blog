title: 使用队列实现栈
create_time: 2016/04/13 20:45:25
tags:
- Stack
- Design
categories:
- leetcode
- C++

---
## [Implement Stack using Queues](https://leetcode.com/problems/implement-stack-using-queues/)
> Implement the following operations of a stack using queues.
> * push(x) -- Push element x onto stack.
> * pop() -- Removes the element on top of the stack.
> * top() -- Get the top element.
> * empty() -- Return whether the stack is empty.
> 
> Notes:
> * You must use only standard operations of a queue -- which means only push to back, peek/pop from front, size, and is empty operations are valid.
> * Depending on your language, queue may not be supported natively. You may simulate a queue by using a list or deque (double-ended queue), as long as you use only standard operations of a queue.
> * You may assume that all operations are valid (for example, no pop or top operations will be called on an empty stack).

### [Code](https://github.com/Finalcheat/leetcode/blob/master/src/Implement-Stack-using-Queues.cpp)
```
class Stack {
    public:
        // Push element x onto stack.
        void push(int x) {
            q2.push(x);
            _q1MoveToQ2();
            q1.swap(q2);
        }

        // Removes the element on top of the stack.
        void pop() {
            q1.pop();
        }

        // Get the top element.
        int top() {
            return q1.front();
        }

        // Return whether the stack is empty.
        bool empty() {
            return q1.empty();
        }
        
    private:
        void _q1MoveToQ2() {
            while (!q1.empty()) {
                int value = q1.front();
                q1.pop();
                q2.push(value);
            }
        }
        
    private:
        std::queue<int> q1;
        std::queue<int> q2;
};
```
