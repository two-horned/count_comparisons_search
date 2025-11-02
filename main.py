class SearchResult:
    def __init__(self, index: int, comparisons: int):
        self.result = index
        self.comparisons = comparisons
    def __str__(self):
        return "Result: " + str(self.result) + ", Comparisons needed: " + str(self.comparisons)


def binary_search(array: list[int], elem: int) -> SearchResult:
    comparisons = 0
    left = 0
    right = len(array)

    comparisons += 1
    while left < right:
        mid = left + (right - left) // 2
        
        comparisons += 1
        if array[mid] < elem:
            left = mid + 1
            comparisons += 1 # while-loop
            continue
        
        comparisons += 1
        if array[mid] > elem:
            right = mid
            comparisons += 1 # while-loop
            continue
        
        return SearchResult(mid, comparisons)
    return SearchResult(-1, comparisons)

def ternary_search(array: list[int], elem: int) -> SearchResult:
    comparisons = 0
    left = 0
    right1 = len(array)

    comparisons += 1
    while left < right1:
        right2 = right1 - 1
        mid1 = left + (right1 - left) // 3
        mid2 = right2 - (right2 - left) // 3
        
        comparisons += 1
        if array[mid1] < elem:
        
            comparisons += 1
            if array[mid2] < elem:
                left = mid2 + 1
                comparisons += 1 # while-loop
                continue

            comparisons += 1
            if array[mid2] > elem:
                left = mid1 + 1
                right1 = mid2
                comparisons += 1 # while-loop
                continue
        
            return SearchResult(mid2, comparisons)

        comparisons += 1
        if array[mid1] > elem:
            right1 = mid1
            comparisons += 1 # while-loop
            continue
        
        return SearchResult(mid1, comparisons)
    return SearchResult(-1, comparisons)

def count_max_comparisons(r):
    print("Checking for range 0-", r)
    arr = list(range(r))

    max_b = 0
    max_t = 0

    for i in range(-1,r+1):
        b = binary_search(arr, i)
        t = ternary_search(arr, i)
        assert(b.result == t.result)
        max_b = max(max_b, b.comparisons)
        max_t = max(max_t, t.comparisons)

    print("Max comparisons for binary search:", max_b)
    print("Max comparisons for ternary search:", max_t)

if __name__ == "__main__":
    print("Enter range to check for:")
    r = int(input())
    count_max_comparisons(r)
