import operator


def calculate(price_of_houses):
    previous_color = '0'
    whole_cost = 0
    for i in price_of_houses:
        sorted_costs = sorted(i.items(), key=operator.itemgetter(1))
        counter = 0
        while counter < len(sorted_costs):
            cheapest_color = sorted_costs[counter][0]
            if cheapest_color != previous_color:
                previous_color = cheapest_color
                whole_cost += sorted_costs[counter][1]
                break
            counter += 1
    return whole_cost


if __name__ == '__main__':
    price_of_houses = [{'r': 50, 'g': 75, 'b': 100}, {'r': 100, 'g': 50, 'b': 75}, {'r': 100, 'g': 75, 'b': 50}]
    assert calculate(price_of_houses) == 150
    price_of_houses = [{'r': 50, 'g': 75, 'b': 100}, {'r': 100, 'g': 50, 'b': 75}, {'r': 70, 'g': 50, 'b': 60}]
    assert calculate(price_of_houses) == 160
