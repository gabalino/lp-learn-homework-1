"""

Домашнее задание №1

Цикл for: Продажи товаров

* Дан список словарей с данными по колличеству проданных телефонов
  [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]},
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]
* Посчитать и вывести суммарное количество продаж для каждого товара
* Посчитать и вывести среднее количество продаж для каждого товара
* Посчитать и вывести суммарное количество продаж всех товаров
* Посчитать и вывести среднее количество продаж всех товаров
"""

sales = [
    {'product': 'iPhone 12',
     'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]},
    {'product': 'Xiaomi Mi11',
     'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21',
     'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
]


def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    total_count = 0
    avg_count = 0
    avg_sum = 0
    for product in sales:
        product_total = sum(product['items_sold'])
        product['product_total'] = product_total
        total_count += product_total
        product_avg = product_total / len(product['items_sold'])
        product['product_avg'] = product_avg
        avg_sum += product_avg
        print(f"{product['product']} - total: {product_total}, avg: {round(product_avg)}")
    avg_count = round(avg_sum / len(sales))
    print('-' * 50)
    print(f"Total: {total_count}\nAvg: {avg_count}")


if __name__ == "__main__":
    main()
