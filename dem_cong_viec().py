def dem_cong_viec():
    """Hàm đếm và hiển thị danh sách công việc đơn giản"""
    print("\n=== DANH SÁCH CÔNG VIỆC ===")
    
    # Tạo danh sách rỗng để lưu công việc
    cong_viec = []
    
    # Nhập công việc từ người dùng
    while True:
        ten = input("Nhập tên công việc (bỏ trống để dừng): ")
        if ten == "":
            break
        cong_viec.append(ten)  # Thêm công việc vào danh sách
    
    # Đếm và hiển thị kết quả
    so_luong = len(cong_viec)
    print(f"\nBạn có {so_luong} công việc:")
    
    # Hiển thị từng công việc có đánh số
    stt = 1
    for viec in cong_viec:
        print(f"{stt}. {viec}")
        stt += 1

# Chạy chương trình
dem_cong_viec()