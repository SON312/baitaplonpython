def dat_nhac_nho():
    """Hàm đặt nhắc nhở cho công việc"""
    print("\n=== ĐẶT NHẮC NHỞ CÔNG VIỆC ===")
    
    # Nhập thông tin
    ten_cv = input("Nhập tên công việc: ")
    thoi_gian = input("Nhập thời gian nhắc (dd/mm/yyyy HH:MM): ")
    noi_dung = input("Nhập nội dung nhắc nhở: ")
    
    # Hiển thị thông tin đã nhập
    print("\n=== THÔNG TIN NHẮC NHỞ ===")
    print(f"Công việc: {ten_cv}")
    print(f"Thời gian: {thoi_gian}")
    print(f"Nội dung: {noi_dung}")
    
    # Kiểm tra và thông báo
    if ten_cv and thoi_gian:
        print("=> Đã đặt nhắc nhở thành công!")
    else:
        print("=> Lỗi: Thiếu thông tin bắt buộc")

# Gọi hàm thực hiện
if __name__ == "__main__":
    dat_nhac_nho()