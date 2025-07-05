def thong_ke_cong_viec():
    # Danh sách lưu công việc
    danh_sach = []
    
    print("\n=== NHẬP CÔNG VIỆC ===")
    print("(Gõ 'xong' khi muốn dừng nhập)")
    
    # Nhập công việc
    while True:
        ten = input("Tên công việc: ")
        if ten == "xong":
            break
        
        trang_thai = input("Đã hoàn thành chưa? (y/n): ")
        hoan_thanh = trang_thai == "y"  
        
        # Thêm vào danh sách
        danh_sach.append({
            "ten": ten,
            "hoan_thanh": hoan_thanh
        })
    
    # Tính toán thống kê
    tong_cv = len(danh_sach)
    cv_da_xong = sum(1 for cv in danh_sach if cv["hoan_thanh"])
    cv_chua_xong = tong_cv - cv_da_xong
    
    # Hiển thị kết quả
    print("\n=== KẾT QUẢ THỐNG KÊ ===")
    print(f"Tổng công việc: {tong_cv}")
    print(f"Đã hoàn thành: {cv_da_xong}")
    print(f"Chưa hoàn thành: {cv_chua_xong}")

# Chạy chương trình
thong_ke_cong_viec()