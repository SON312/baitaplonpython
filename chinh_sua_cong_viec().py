def chinh_sua_cong_viec():
    """Hàm chỉnh sửa công việc (bao gồm người phụ trách)"""
    print("\n=== CHỈNH SỬA CÔNG VIỆC ===")
    
    # Bước 1: Nhập thông tin công việc
    ten_cv = input("Nhập tên công việc: ")
    nguoi_pt = input("Nhập người phụ trách: ")
    trang_thai = input("Nhập trạng thái (Ví dụ: Đang làm/Xong/Chưa bắt đầu): ")
    
    # Bước 2: Hiển thị thông tin
    print("\nTHÔNG TIN CÔNG VIỆC:")
    print(f"1. Tên: {ten_cv}")
    print(f"2. Người phụ trách: {nguoi_pt}")
    print(f"3. Trạng thái: {trang_thai}")
    
    # Bước 3: Menu lựa chọn
    while True:
        print("\nBạn muốn sửa gì?")
        print("1. Tên công việc")
        print("2. Người phụ trách")
        print("3. Trạng thái")
        print("4. Kết thúc")
        
        lua_chon = input("Chọn (1-4): ")
        
        # Bước 4: Xử lý lựa chọn
        if lua_chon == "1":
            ten_cv = input("Nhập tên mới: ")
            print(f"Đã cập nhật tên: {ten_cv}")
        elif lua_chon == "2":
            nguoi_pt = input("Nhập người phụ trách mới: ")
            print(f"Đã cập nhật người PT: {nguoi_pt}")
        elif lua_chon == "3":
            trang_thai = input("Nhập trạng thái mới: ")
            print(f"Đã cập nhật trạng thái: {trang_thai}")
        elif lua_chon == "4":
            print("\nKẾT QUẢ CUỐI CÙNG:")
            print(f"- Tên: {ten_cv}")
            print(f"- Người PT: {nguoi_pt}")
            print(f"- Trạng thái: {trang_thai}")
            break
        else:
            print("Lựa chọn không hợp lệ, vui lòng chọn lại!")

# Chạy chương trình
chinh_sua_cong_viec()