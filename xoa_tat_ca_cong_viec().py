def xoa_tat_ca_cong_viec():
    cong_viec = []

    print("=== NHẬP CÔNG VIỆC (gõ 'xong' để dừng) ===")
    while True:
        ten = input("Công việc: ")
        if ten.lower() == 'xong':
            break
        cong_viec.append(ten)

    if not cong_viec:
        print("\nKhông có công việc nào.")
        return

    print("\nDANH SÁCH CÔNG VIỆC:")
    for i, cv in enumerate(cong_viec, 1):
        print(f"{i}. {cv}")

    xac_nhan = input("\nXóa tất cả công việc? (y/n): ")
    if xac_nhan.lower() == 'y':
        cong_viec = []
        print("\nĐã xóa toàn bộ công việc.")
    else:
        print("\nKhông xóa. Danh sách vẫn giữ nguyên.")

    print("\nDANH SÁCH HIỆN TẠI:")
    if cong_viec:
        for i, cv in enumerate(cong_viec, 1):
            print(f"{i}. {cv}")
    else:
        print("Danh sách trống.")

# Gọi hàm
xoa_tat_ca_cong_viec()
