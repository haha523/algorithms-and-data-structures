from orders_manager import OrdersManager

def main():
    # Инициализируйте OrdersManager необходимыми файлами
    order_manager = OrdersManager("orders.txt", "order_country.txt", "non_valid_orders.txt")

    # Запись действительных и недействительных заказов в файл
    order_manager.write_valid_orders()
    order_manager.write_non_valid_orders()

    # Распечатать содержимое полученных файлов
    print("order_country.txt:")
    order_manager.print_valid_orders()

    print("\nnon_valid_orders.txt:")
    order_manager.print_non_valid_orders()

def print_file(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        print(file.read())

if __name__ == "__main__":
    main()