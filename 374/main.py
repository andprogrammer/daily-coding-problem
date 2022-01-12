def get_lowest_index(data):
  if not data:
    return None
  for i in range(len(data)):
    if i == data[i]:
      return i
  return None

if __name__ == '__main__':
  assert 2 == get_lowest_index([-5, -3, 2, 3])
