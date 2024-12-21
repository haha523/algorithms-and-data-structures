import unittest
from src.lab5.order import Order
from src.lab5.orders_manager import OrdersManager

class TestOrder(unittest.TestCase):
    def test_valid_orders(self):
        with open("C:\\Users\\FPT 2633\\cs102\\src\\lab5\\orders.txt", "r", encoding="utf-8") as f:
            for line in f:
                order_str = line.strip()
                order = Order(order_str)

                # Проверьте адрес
                if not order.is_address_valid():
                    self.assertFalse(order.is_address_valid())
                    continue

                # Проверить номер телефона
                if not order.is_phone_number_valid():
                    self.assertFalse(order.is_phone_number_valid())
                    continue

                # Получить информацию из строки заказа
                expected_country = order_str.split(';')[3].strip().split('.')[0].strip()  # Получить часть страны
                expected_priority = order_str.split(';')[-1].strip()
                self.assertEqual(order.get_country(), expected_country,f"Expected country '{expected_country}' for order: {order_str}")
                self.assertEqual(order.get_priority(), expected_priority,f"Expected priority '{expected_priority}' for order: {order_str}")

    def test_invalid_order_address(self):
        # Чтение из файла order.txt
        with open("C:\\Users\\FPT 2633\\cs102\\src\\lab5\\orders.txt", "r", encoding="utf-8") as f:
            for line in f:
                order = Order(line.strip())  # Создайте объект Order из каждой строки
                if not order.is_address_valid():  # Проверяем, действителен ли адрес
                    self.assertFalse(order.is_address_valid())  # Неверный чек

    def test_invalid_order_phone(self):
        # Чтение из файла order.txt
        with open("C:\\Users\\FPT 2633\\cs102\\src\\lab5\\orders.txt", "r", encoding="utf-8") as f:
            for line in f:
                order = Order(line.strip())  # Создайте объект Order из каждой строки.

                # Проверьте актуальность номера телефона
                if not order.is_phone_number_valid():  # Если номер телефона недействителен
                    self.assertFalse(order.is_phone_number_valid(), f"Valid phone number for order: {line.strip()}")

class TestOrdersManager(unittest.TestCase):

    def setUp(self):
        self.manager = OrdersManager(
            "C:\\Users\\FPT 2633\\cs102\\src\\lab5\\orders.txt",
            "C:\\Users\\FPT 2633\\cs102\\src\\lab5\\order_country.txt",
            "C:\\Users\\FPT 2633\\cs102\\src\\lab5\\non_valid_orders.txt"
        )

    def test_valid_orders_output(self):
        self.manager.write_valid_orders()
        with open("C:\\Users\\FPT 2633\\cs102\\src\\lab5\\order_country.txt", "r", encoding="utf-8") as f:
            content = f.read()

            # Проверьте каждую строку в файле order_country.txt
            for line in content:
                self.assertIn(line.strip(), content, f"Expected output not found: {line.strip()}")

    def test_non_valid_orders_output(self):
        self.manager.write_non_valid_orders()
        with open("C:\\Users\\FPT 2633\\cs102\\src\\lab5\\non_valid_orders.txt", "r", encoding="utf-8") as f:
            content = f.read()

            # Проверьте каждую строку в файле non_valid_orders.txt
            for line in content:
                self.assertIn(line.strip(), content, f"Expected output not found: {line.strip()}")

if __name__ == "__main__":
    unittest.main()