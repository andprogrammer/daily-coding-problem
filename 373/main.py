def get_max_length_of_consecutive_numbers(numbers):
  if not numbers:
    return 0
  numbers.sort()
  max_length = 0
  current_max_length = 1
  for i in range(0, len(numbers) - 1):
    if numbers[i] + 1 == numbers[i + 1]:
      current_max_length += 1
    else:
      max_length = current_max_length if current_max_length > max_length else max_length
      current_max_length = 1
  return current_max_length if current_max_length > max_length else max_length

if __name__ == '__main__':
  assert 5 == get_max_length_of_consecutive_numbers([5, 2, 99, 3, 4, 1, 100])
  assert 3 == get_max_length_of_consecutive_numbers([4, 6, 8, 11, 13, 16, 12])
  assert 6 == get_max_length_of_consecutive_numbers([4, 6, 8, 11, 13, 7, 16, 12, 5, 9])
