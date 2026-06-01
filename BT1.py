delivery_orders = ["GRAB1", "GRAB2", "GRAB3-CANCEL"]

delivery_orders.append("GRAB4")

delivery_orders.insert(0, "GRAB0")

delivery_orders[2] = "GRAB2-UPDATED"

delivery_orders.remove("GRAB3-CANCEL")

transferred_order = delivery_orders.pop()

print(f"- Danh sách đơn hàng còn lại: {delivery_orders}")
print(f"- Đơn hàng được bàn giao: {transferred_order}")