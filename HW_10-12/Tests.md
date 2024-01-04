План тестирования интернет-магазина:

1. Unit Test для сервисов бизнес логики интернет-магазина
1.1 Метод добавления товара в корзину (addProduct)
Ожидаемый результат: Происходит добавление нового товара в корзину. Количество товара пересчитывается и обновляется общая стоимость продукта.

1.2 Метод удаления товара из корзины (deleteProduct)
Ожидаемый результат: Происходит удаление товара из корзины. Количество товара пересчитывается и обновляется общая стоимость продукта.

1.3 Метод фильтрации товаров
Ожидаемый результат: Происходит вывод товаров с конкретными заданными параметрами, такими как диапазон цены, производитель и другие.

1.4 Метод оформления заказа
Ожидаемый результат: Происходит сохранение данных заказа. Указывается список товаров, количество, стоимость, вариант доставки и стоимость доставки.

1.5 Метод отображения списка заказов
Ожидаемый результат: Выводит список всех заказов с номерами заказов (ID). Также выводит список заказов, созданных конкретным пользователем. В строке заказа указывается количество товаров и стоимость заказа.