def range_sum(numbers, start, end):
    # return sum(filter(lambda x: start <= x <= end, numbers))
    return sum(x for x in numbers if start <= x <= end)

# input_numbers = map(int, input().split())
# a, b = map(int, input().split())
input_numbers = [int(x) for x in input().split()]
a, b = [int(x) for x in input().split()]

print(range_sum(input_numbers, a, b))