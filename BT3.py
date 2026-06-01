# Hệ thống quản lý đơn hàng Grab Express

order_list = ["GE001", "GE002", "GE003"]

while True:
    print("\n===== HỆ THỐNG QUẢN LÝ ĐƠN HÀNG GRAB EXPRESS =====")
    print("1. Hiển thị danh sách đơn hàng")
    print("2. Thêm đơn hàng mới")
    print("3. Xóa đơn hàng theo mã")
    print("4. Thoát chương trình")

    choice = input("Chọn chức năng (1-4): ").strip()

    # Kiểm tra lựa chọn menu hợp lệ
    if not choice.isdigit() or int(choice) not in range(1, 5):
        print("Lựa chọn không hợp lệ, vui lòng nhập lại!")
        continue

    choice = int(choice)

    if choice == 1:
        if not order_list:
            print("Danh sách đơn hàng hiện đang trống.")
        else:
            print("Danh sách đơn hàng hiện tại:")
            for index, order in enumerate(order_list, start=1):
                print(f"{index}. {order}")


    elif choice == 2:
        new_order = input("Nhập mã đơn hàng mới: ").strip().upper()
        if new_order:
            order_list.append(new_order)
            print(f"Đã thêm đơn hàng: {new_order}")
        else:
            print("Mã đơn hàng không hợp lệ!")


    elif choice == 3:
        remove_order = input("Nhập mã đơn hàng cần xóa: ").strip().upper()
        if remove_order in order_list:
            order_list.remove(remove_order)
            print(f"Đã xóa đơn hàng: {remove_order}")
        else:
            print("Không tìm thấy mã đơn hàng cần xóa!")

    # Chức năng 4: Thoát chương trình
    elif choice == 4:
        print("Thoát chương trình.")
        break