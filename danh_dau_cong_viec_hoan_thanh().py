def danh_dau_cong_viec_hoan_thanh():
    print("\n=== ĐÁNH DẤU CÔNG VIỆC HOÀN THÀNH ===")
    
    # Nhập tên công việc
    ten_cong_viec = input("Nhập tên công việc đã hoàn thành: ")
    
    # Xác nhận với người dùng
    print(f"\nBạn có chắc muốn đánh dấu '{ten_cong_viec}' là hoàn thành?")
    xac_nhan = input("Nhập 'y' để xác nhận, phím bất kỳ để hủy: ")
    
    # Xử lý kết quả
    if xac_nhan.lower() == 'y':
        print("\nĐÃ ĐÁNH DẤU THÀNH CÔNG!")
        print("Công việc:", ten_cong_viec)
    else:
        print("\nĐÃ HỦY THAO TÁC")

# Chạy chương trình
danh_dau_cong_viec_hoan_thanh()