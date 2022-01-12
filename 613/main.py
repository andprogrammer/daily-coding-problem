class PrefixMapSum:
    def __init__(self):
        self.m = {}

    def insert(self, key, value):
        self.m[key] = value

    def sum(self, key):
        result = 0
        for k, v in self.m.items():
            if k.startswith(key):
                result += v
        return result


def main():
    mapsum = PrefixMapSum()
    mapsum.insert("columnar", 3)
    assert mapsum.sum("col") == 3

    mapsum.insert("column", 2)
    assert mapsum.sum("col") == 5


if __name__ == '__main__':
    main()
