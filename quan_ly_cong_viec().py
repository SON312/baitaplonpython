from datetime import datetime

def nhap_cong_viec():
    cv = []
    print("\n=== NHẬP CÔNG VIỆC ===")
    print("(Gõ 'xong' khi muốn kết thúc nhập)")
    
    while True:
        ten = input("Tên công việc: ")
        if ten == "xong":
            break
        ngay = input("Ngày (dd/mm/yyyy): ")
        try:
            cv.append((ten, datetime.strptime(ngay, "%d/%m/%Y")))
        except:
            print("Sai định dạng ngày!")
    return cv

def xem_cong_viec(cv):
    if not cv:
        print("\nKhông có công việc nào!")
        return
    
    print("\n1. Xem theo ngày")
    print("2. Xem theo tuần")
    print("3. Xem theo tháng")
    chon = input("Chọn: ")
    
    if chon == "1":
        ngay = input("Nhập ngày cần xem (dd/mm/yyyy): ")
        try:
            ngay = datetime.strptime(ngay, "%d/%m/%Y").date()
            print("\n=== KẾT QUẢ ===")
            for i, (ten, ngay_cv) in enumerate(cv, 1):
                if ngay_cv.date() == ngay:
                    print(f"{i}. {ten} - {ngay_cv.strftime('%d/%m/%Y')}")
        except:
            print("Ngày không hợp lệ!")
    
    elif chon == "2":
        ngay = input("Nhập ngày trong tuần cần xem (dd/mm/yyyy): ")
        try:
            ngay = datetime.strptime(ngay, "%d/%m/%Y")
            tuan, nam = ngay.isocalendar()[1], ngay.year
            print("\n=== KẾT QUẢ ===")
            for i, (ten, ngay_cv) in enumerate(cv, 1):
                if ngay_cv.isocalendar()[1] == tuan and ngay_cv.year == nam:
                    print(f"{i}. {ten} - {ngay_cv.strftime('%d/%m/%Y')}")
        except:
            print("Ngày không hợp lệ!")
    
    elif chon == "3":
        try:
            thang, nam = map(int, input("Nhập tháng/năm cần xem (mm/yyyy): ").split("/"))
            print("\n=== KẾT QUẢ ===")
            for i, (ten, ngay_cv) in enumerate(cv, 1):
                if ngay_cv.month == thang and ngay_cv.year == nam:
                    print(f"{i}. {ten} - {ngay_cv.strftime('%d/%m/%Y')}")
        except:
            print("Sai định dạng!")

# Chạy chương trình
danh_sach = nhap_cong_viec()
xem_cong_viec(danh_sach)