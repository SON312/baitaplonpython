def xoa_cong_viec():
    cong_viec = []

    print("=== NHẬP CÔNG VIỆC (gõ 'xong' để kết thúc) ===")
    while True:
        ten = input("Nhập công việc: ")
        if ten.lower() == 'xong':
            break
        cong_viec.append(ten)

    if not cong_viec:
        print("\nKhông có công việc nào!")
        return

    print("\nDANH SÁCH CÔNG VIỆC:")
    for i, cv in enumerate(cong_viec, 1):
        print(f"{i}. {cv}")

    ten_xoa = input("\nNhập tên công việc muốn xóa: ")
    if ten_xoa in cong_viec:
        cong_viec.remove(ten_xoa)
        print(f"Đã xóa '{ten_xoa}'")
    else:
        print("Không tìm thấy công việc!")

    print("\nDANH SÁCH CÒN LẠI:")
    for i, cv in enumerate(cong_viec, 1):
        print(f"{i}. {cv}")

# Chạy hàm
xoa_cong_viec()
