# python3
import sys

def majority_element_naive(elements):
    assert len(elements) <= 10 ** 5
    for e in elements:
        if elements.count(e) > len(elements) / 2:
            return 1

    return 0


def get_majority_element(elements, hi, lo):
    assert len(elements) <= 10 ** 5

    # base case: once the array is split into an array of length 1
    # ie. hi = lo
    # return the only element in it
    # which is in effect the majority element
    if hi == lo:
        return elements[hi]
    else:
        mid = lo + (hi-lo)//2
        left = get_majority_element(elements, mid, lo)
        right = get_majority_element(elements, hi, mid+1)

    # once the recursive calls are done
    # check if the return values are the same
    # if yes, the return value is the majority element of the array in consideration
    # example: array [2, 2, 3] will be split into
    # left [2, 2] and right [3]
    # left will be then split into left-left [2] and left-right [2]
    # since left-left = left-right, left = 2
    # right = 3
    # since left != right, count the occurence of left (ie. 2) and right (ie. 3) in the array
    # if the either left_count > n/2 or right_count > n/2 with n = len(array)
    # return that value as the majority element
    # else, return -1 to indicate that there's no majority element in the array
    # since left (ie. 2) appears 2 times (2>(n/2) with n=3) whereas right (ie. 3 appears one time
    # 2 is the majority element
    if left == right:
        return left
    else:
        left_count = sum(1 for i in range(lo, hi+1) if elements[i] == left)
        right_count = sum(1 for i in range(lo, hi+1) if elements[i] == right)

        # check if the candidate element is repeated more than n/2 time
        # n/2 is calculated as (hi-lo+1)/2
        if left_count > ((hi-lo+1)/2):
            return left
        elif right_count > ((hi-lo+1)/2):
            return right
        else:
            return -1


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    n = len(a)
    if get_majority_element(a, n-1, 0) != -1:
        print(1)
    else:
        print(0)
    print(majority_element_naive(a))


