import heapq

def merge_cables(cables):

    heapq.heapify(cables)

    total = 0

    while len(cables) > 1:
        cable1 = heapq.heappop(cables)
        cable2 = heapq.heappop(cables)

        merged_cable = cable1 + cable2
        heapq.heappush(cables, merged_cable)

        total += merged_cable

        print(f"Об'єднання кабелів: {cable1} + {cable2} = {merged_cable}")

    return total


def main():
    cables = [int(x) for x in input("Введіть Integer довжини кабелів через пробіл: ").split()]

    total = merge_cables(cables)

    print(f"Загальні витрати: {total}")

if __name__ == "__main__":
    main()
