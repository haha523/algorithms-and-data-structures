from src.lab5.order import Order

class OrdersManager:
    def __init__(
        self,
        orders_path,
        valid_orders_path = None,
        non_valid_orders_path = None
    ):
        self.__non_valid_orders_path = non_valid_orders_path
        self.__order_county_path = valid_orders_path
        self.__valid_orders = []
        self.__non_valid_orders = []

        self.__import_orders_from_file(orders_path)


    def write_valid_orders(self) -> None:
        # Запись провалидированных заказов в файл
        if self.__order_county_path:
            to_write = self.get_valid_orders_output()
            f = open(self.__order_county_path, "w", encoding="utf-8")
            f.write(to_write)
            f.close()
        else:
            print("OrderManager.write_valid_orders() - файл не указан\n")

    def write_non_valid_orders(self) -> None:
        # Запись заказов с ошибкой
        if self.__non_valid_orders_path:
            to_write = self.get_non_valid_orders_output()
            f = open(self.__non_valid_orders_path, "w", encoding="utf-8")
            f.write(to_write)
            f.close()
        else:
            print("OrderManager.write_non_valid_orders() - файл не указан\n")

    def print_valid_orders(self) -> None:
        # Вывод валидированных заказов
        print(self.get_valid_orders_output())

    def print_non_valid_orders(self) -> None:
        # Вывод заказов с ошибкой
        print(self.get_non_valid_orders_output())

    def get_valid_orders_output(self) -> str:
        # Получение строки валидированных заказов
        output = []
        for order in self.__get_sorted_valid_orders():
            output.append(order.to_string())
        return "\n".join(output)

    def get_non_valid_orders_output(self) -> str:
        # Получение строки заказов с ошибкой
        output = []
        for order in self.__non_valid_orders:
            output.append(order.to_string())
        return "\n".join(output)

    def __get_sorted_valid_orders(self) -> list:
        # Получение сортированных валидированных заказов

        first_county = "Россия"

        first_county_orders = []
        rest_orders = []
        for order in self.__valid_orders:
            if order.get_country() == first_county:
                first_county_orders.append(order)
            else:
                rest_orders.append(order)

        first_county_orders.sort(key=lambda order_: order_.get_priority_int())
        rest_orders.sort(key=lambda order_: (
            order_.get_country(),
            order_.get_priority_int()
        ))
        orders_sorted = first_county_orders + rest_orders
        return orders_sorted

    def __import_orders_from_file(self, orders_path) -> None:
        # Импортирование заказов из файла
        f = open(orders_path, encoding="utf-8")
        for order_str in f.read().split("\n"):
            self.__import_order(order_str)
        f.close()

    def __import_order(self, order_str) -> None:
        # Импортирование заказа из строки в соответствующий список
        order = Order(order_str)
        if order.is_address_valid() and order.is_phone_number_valid():
            self.__add_valid_order(order)
        else:
            self.__add_non_valid_order(order)

    def __add_valid_order(self, order) -> None:
        # Добавление заказа с ошибкой в соответствующий список
        self.__valid_orders.append(order)

    def __add_non_valid_order(self, order) -> None:
        # Добавление валидированного заказа в соответствующий список
        self.__non_valid_orders.append(order)