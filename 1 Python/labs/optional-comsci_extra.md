

## Version 3 - Bubble Sort (optional)

[Bubble sort](https://en.wikipedia.org/wiki/Bubble_sort) is one of the simplest and least efficient sorting algorithms. We repeatedly loop over the list, comparing each number to the one next to it, and swapping them if needed.

```
procedure bubbleSort(A : list of sortable items)
    n := length(A)
    repeat
        swapped = false
        for i := 1 to n - 1 inclusive do
            /* if this pair is out of order */
            if A[i - 1] > A[i] then
                /* swap them and remember something changed */
                swap(A[i - 1], A[i])
                swapped := true
            end if
        end for
    until not swapped
end procedure
```

## Version 4 - Insertion Sort (optional)

Implement [insertion sort](https://en.wikipedia.org/wiki/Insertion_sort), which like bubble sort is also `O(n^2)`, but is efficient at placing new values into an already-sorted list.

Psuedocode:
```
i ← 1
while i < length(A)
    j ← i
    while j > 0 and A[j-1] > A[j]
        swap A[j] and A[j-1]
        j ← j - 1
    end while
    i ← i + 1
end while
```


## Version 5 - Quicksort (optional)

[Quicksort](https://en.wikipedia.org/wiki/Quicksort) is one of the most efficient sorting algorithms. It works by swapping elements on either side of a pivot value.

Psuedocode:
```
algorithm quicksort(A) is
    quicksort_recursive(A, 0, length(A) - 1)

algorithm quicksort_recursive(A, lo, hi) is
    if lo < hi then
        p := partition(A, lo, hi)
        quicksort_recursive(A, lo, p)
        quicksort_recursive(A, p + 1, hi)

algorithm partition(A, lo, hi) is
    pivot := A[lo + (hi - lo) / 2]
    i := lo - 1
    j := hi + 1
    loop forever
        do
            i := i + 1
        while A[i] < pivot
        do
            j := j - 1
        while A[j] > pivot
        if i ≥ j then
            return j
        swap A[i] with A[j]
```





## Doubly Linked List (optional)

In a [doubly-linked list](https://en.wikipedia.org/wiki/Doubly_linked_list) each node maintains a reference to both the next and previous node. Implement a class `DoubleyLinkedList` with the same methods as `LinkedList` but with each node having a reference to both the `previous` and `next` nodes.
