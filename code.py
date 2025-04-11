class Item:
    def __init__(self, code, name, quantity, price):
        self.code = code
        self.name = name
        self.quantity = quantity
        self.price = price

    def total_value(self):
        return self.quantity * self.price

def input_items():
    items = []
    
    n = int(input("Nhập số lượng mặt hàng: "))
    for _ in range(n):
        code = input("Mã hàng: ")
        name = input("Tên mặt hàng: ")
        quantity = int(input("Số lượng: "))
        price = float(input("Giá tiền: "))
        item = Item(code, name, quantity, price)
        items.append(item)
    
    return items

def display_items(items):
    print(f"{'Mã hàng':<10} {'Tên mặt hàng':<20} {'Số lượng':<10} {'Giá tiền':<10} {'Tổng giá trị':<15}")
    print("="*65)
    for item in items:
        print(f"{item.code:<10} {item.name:<20} {item.quantity:<10} {item.price:<10} {item.total_value():<15}")

def calculate_total_value(items):
    return sum(item.total_value() for item in items)

def find_min_value_item(items):
    return min(items, key=lambda item: item.total_value())

def count_items_above_quantity(items, quantity_limit=5):
    return sum(1 for item in items if item.quantity > quantity_limit and item.total_value() < 1000000)

def main():
    items = input_items()
    display_items(items)
    
    total_value = calculate_total_value(items)
    print(f"\nTổng giá trị của tất cả mặt hàng: {total_value} VND")
    
    min_item = find_min_value_item(items)
    print(f"\nMặt hàng có tổng giá trị nhỏ nhất: {min_item.name} - Tổng giá trị: {min_item.total_value()} VND")
    
    count_above_quantity = count_items_above_quantity(items)
    print(f"Số lượng mặt hàng có số lượng lớn hơn 5 và tổng giá trị dưới 1,000,000 VND: {count_above_quantity}")

if __name__ == "__main__":
    main()