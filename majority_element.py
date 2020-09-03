# python3
import sys

def majority_element_naive(elements):
    """
    This naive function returns the majority element in the passed-in sequence if there is one.
    Otherwise, it returns -1.
    Time complexity: O(n**2).
    """
    assert len(elements) <= 10 ** 5
    for e in elements:
        if elements.count(e) > len(elements) / 2:
            return e

    return -1


def get_majority_element(elements, hi, lo):
    assert len(elements) <= 10 ** 5

    """
    This function is a divide-and-conquer algo that returns the majority element 
    in the subsequence of "elements" from index "lo" to "hi" if there is one. 
    Otherwise, the function returns -1
    First, we split the sequence into 2 halves. 
    If there is a majority element 
    (i.e. an element that appears more than n/2 with n = length of the (sub)sequence), 
    that element must be the majority element of either one of the halves or both.
    Time complexity: O(nlog(n)).
    Example 1:
    input (sequence of non-negative numbers):
    5
    2 3 9 2 2
    output: 2 (majority element = 2)
    Example 2:
    input: 
    5
    0 1 2 3 4
    output: -1 (no majority element)
    """
    # If the sequence is of length 1, return the only element as the majority element
    if hi == lo:
        return elements[hi]
    # Otherwise, split the sequence into 2 halves and find the majority element of each half "left" and "right"
    else:
        mid = (hi + lo) // 2
        left = get_majority_element(elements, mid, lo)
        right = get_majority_element(elements, hi, mid+1)

    # If the majority elements of the two halves are the same, return that element as the majority element.
    # That means the two halves either have the same majority element or none i.e. left = right = -1
    if left == right:
        return left
    # Otherwise, check which of the two majority elements are the true majority element
    # of the sequence made up of the two halves
    else:
        left_count, right_count = 0, 0
        if left != -1:
            left_count += sum(1 for i in range(lo, hi+1) if elements[i] == left)
        if right != -1:
            right_count += sum(1 for i in range(lo, hi+1) if elements[i] == right)
        if left_count > ((hi-lo+1)/2):
            return left
        if right_count > ((hi-lo+1)/2):
            return right
        else:
            return -1


def get_majority_element_optimized(elements):
    """
    This function returns the majority element
    in a sequence "elements" of non-negative elements if there is one using hash map
    Otherwise, it returns -1
    Time complexity: O(n)
    Example 1:
    input (sequence of non-negative numbers):
    5
    2 3 9 2 2
    output: 2 (majority element = 2)
    Example 2:
    input:
    5
    0 1 2 3 4
    output: -1 (no majority element)
    """
    # Create an empty hash map to keep track of the count of each unique element
    d = {}
    for e in elements:
        d[e] = d.get(e, 0) + 1

    # Return the majority element if there is one
    for key, value in d.items:
        if value > len(elements) / 2:
            return key

    # No majority element present
    return -1


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    n = len(a)
    if get_majority_element(a, n-1, 0) != -1:
        print(1)
    else:
        print(0)


