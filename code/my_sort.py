def sort_array(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        left = [x for x in arr[1:] if x < pivot]
        right = [x for x in arr[1:] if x >= pivot]
        return sort_array(left) + [pivot] + sort_array(right)


def my_strip(s, chars=None):
    if chars is None:
        chars = ' \t\n\r\v\f'

    start = 0
    end = len(s) - 1

    # Remove leading characters
    while start <= end and s[start] in chars:
        start += 1

    # Remove trailing characters
    while end >= start and s[end] in chars:
        end -= 1

    # Return the sliced string
    return s[start:end+1]
