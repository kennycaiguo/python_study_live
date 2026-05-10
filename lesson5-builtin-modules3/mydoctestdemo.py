# doctest只要求我们把复制到文件字符串中就行了，当然啦还是另外加两行代码不过这个是死的，记下来就是了
def select_sort(lst):
    """
    选择排序算法

    >>> lst = [3,2,1,4,5,6,-1]
    >>> select_sort(lst)
    >>> lst
    [-1, 1, 2, 3, 4, 5, 6]
    >>> 
    >>> lst = [2,1]
    >>> select_sort(lst)
    >>> lst
    [1, 2]
    >>> 
    >>> lst = [0]
    >>> select_sort(lst)
    >>> lst
    [0]
    """
    for i in range(0,len(lst)):
        min_item_index = i
        for j in range(i,len(lst)):
            if lst[j] < lst[min_item_index]:
                min_item_index = j
        if min_item_index != i:
            lst[min_item_index],lst[i] = lst[i],lst[min_item_index]


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)