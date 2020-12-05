# Nth-Element-of-LinkedList

This code documents the algorithm for fetching the Nth element from a uni-directional LinkedList. The catch here is that we are to return the Nth element from the end!

The LinkedList is uni-directional from HEAD to NULL. We are only given the HEAD node in the beginning, so there is no way to tell the size of the list.

Solution 1:-
We simply traverse the LinkedList from HEAD to NULL, and store the individual Nodes in an Array(or Python List datatype). We can them simply fetch the appropriate index(Length - N) from the Array corresponding to the value N and return it.

Solution 2:-
We can make use of two pointers(say, LEFT and RIGHT) and traverse them separately from HEAD. RIGHT will first traverse N nodes from HEAD, while LEFT will remain stationary at HEAD. We then start moving both LEFT and RIGHT pointers, until RIGHT hits the end of the list. RIGHT should hit the end first as it is already ahead of LEFT. Then, LEFT will be at the Nth position from the end, and would be duly returned as the final answer!

Solution 1 is what we would end up thinking of first in "Brute-force" POV. However, when we try to imagine going N places from the end of the LinkedList, we must get an idea that using two pointers placed N elements apart would lead to the LEFT pointer being on the correct element if the RIGHT pointer were at the end. This would be a more optimal solution in with respect to Time AND Space complexity.

