# DivideandConquer_MajorityElement
https://www.coursera.org/learn/algorithmic-toolbox/

__Assignment description__:
Input: A sequence of n ≤ 10^5 integers.
Output: 1, if there is an element that is repeated more than n/2 times, and 0 otherwise.

As you might have already guessed, this problem can be solved by the divide-and-conquer algorithm in time O(nlogn). Indeed, if a sequence of length n contains a majority element, then the same element is also a majority element for one of its halves. Thus, to solve this problem you first split a given sequence into halves and recursively solve it for each half. Do you see how to combine the results of two recursive calls?

__Disclaimer__: If you're currently taking the same course, please refrain yourself from checking out this solution as it will be against Coursera's Honor Code and won’t do you any good. Plus, once you're worked your heart out and was able to solve a particularly difficult problem, a sense of confidence you gained from such experience is priceless :)
