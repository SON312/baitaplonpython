# FILE: quan_ly_cong_viec.py
from datetime import datetime

ds_cong_viec = []  # Danh sách toàn cục

# === CÁC CHỨC NĂNG ===

def them_cong_viec_moi():
    print("=== THÊM CÔNG VIỆC MỚI ===")
    ten = input("Tên công việc: ")
    ngay = input("Ngày bắt đầu (dd/mm/yyyy): ")
    nguoi = input("Người phụ trách: ")
    try:
        ngay = datetime.strptime(ngay, "%d/%m/%Y")
        ds_cong_viec.append({
            "ten": ten,
            "ngay": ngay,
            "nguoi": nguoi,
            "trang_thai": "Chưa bắt đầu",
            "nhac_nho": None
        })
        print("\nĐã thêm công việc:")
        print(f"- Tên: {ten}")
        print(f"- Ngày: {ngay.strftime('%d/%m/%Y')}")
        print(f"- Người phụ trách: {nguoi}")
    except:
        print("Sai định dạng ngày!")

def them_ngay_gio():
    print("=== THÊM NGÀY GIỜ CÔNG VIỆC XẢY RA ===")
    ten = input("Nhập tên: ")
    ngay_gio = input("Nhập ngày giờ công việc xảy ra (dd/mm/yyyy HH:MM): ")
    for cv in ds_cong_viec:
        if cv['ten'] == ten:
            try:
                cv['ngay'] = datetime.strptime(ngay_gio, "%d/%m/%Y %H:%M")
                print(f"Đã cập nhật công việc  '{ten}' vào lúc: {ngay_gio}")
                return
            except:
                print("Sai định dạng ngày giờ!")
                return
    print("Không tìm thấy công việc!")

def dat_nhac_nho():
    print("\n=== ĐẶT NHẮC NHỞ CÔNG VIỆC ===")
    ten_cv = input("Nhập tên công việc: ")
    thoi_gian = input("Nhập thời gian nhắc (dd/mm/yyyy HH:MM): ")
    noi_dung = input("Nhập nội dung nhắc nhở: ")
    for cv in ds_cong_viec:
        if cv['ten'] == ten_cv:
            try:
                cv['nhac_nho'] = {
                    "thoi_gian": datetime.strptime(thoi_gian, "%d/%m/%Y %H:%M"),
                    "noi_dung": noi_dung
                }
                print("=> Đã đặt nhắc nhở thành công!")
                return
            except:
                print("=> Sai định dạng!")
                return
    print("=> Không tìm thấy công việc!")

def hien_thi_cong_viec():
    print("\n=== DANH SÁCH CÔNG VIỆC ===")
    if not ds_cong_viec:
        print("Chưa có công việc nào")
    else:
        stt = 1
        for cv in ds_cong_viec:
            print(f"{stt}. {cv['ten']}")
            print(f"   Người phụ trách: {cv['nguoi']}")
            print(f"   Trạng thái: {cv['trang_thai']}\n")
            stt += 1

def dem_cong_viec():
    print("\n=== DANH SÁCH CÔNG VIỆC ===")
    if not ds_cong_viec:
        print("Không có công việc nào.")
    else:
        print(f"\nBạn có {len(ds_cong_viec)} công việc:")
        for i, cv in enumerate(ds_cong_viec, 1):
            print(f"{i}. {cv['ten']}")

def chinh_sua_cong_viec():
    print("\n=== CHỈNH SỬA CÔNG VIỆC ===")
    ten_cv = input("Nhập tên công việc: ")
    for cv in ds_cong_viec:
        if cv['ten'] == ten_cv:
            print("\nBạn muốn sửa gì?")
            print("1. Tên công việc")
            print("2. Người phụ trách")
            print("3. Trạng thái")
            print("4. Kết thúc")
            while True:
                lua_chon = input("Chọn (1-4): ")
                if lua_chon == "1":
                    cv['ten'] = input("Nhập tên mới: ")
                elif lua_chon == "2":
                    cv['nguoi'] = input("Nhập người phụ trách mới: ")
                elif lua_chon == "3":
                    cv['trang_thai'] = input("Nhập trạng thái mới: ")
                elif lua_chon == "4":
                    break
                else:
                    print("Lựa chọn không hợp lệ!")
            return
    print("Không tìm thấy công việc!")

def danh_dau_hoan_thanh():
    print("\n=== ĐÁNH DẤU CÔNG VIỆC HOÀN THÀNH ===")
    ten_cong_viec = input("Nhập tên công việc đã hoàn thành: ")
    for cv in ds_cong_viec:
        if cv['ten'] == ten_cong_viec:
            cv['trang_thai'] = "Hoàn thành"
            print("\nĐÃ ĐÁNH DẤU THÀNH CÔNG!")
            return
    print("\nKhông tìm thấy công việc!")

def xoa_cong_viec():
    ten_xoa = input("\nNhập tên công việc muốn xóa: ")
    for cv in ds_cong_viec:
        if cv['ten'] == ten_xoa:
            ds_cong_viec.remove(cv)
            print(f"Đã xóa '{ten_xoa}'")
            return
    print("Không tìm thấy công việc!")

def xoa_tat_ca_cong_viec():
    xac_nhan = input("\nXóa tất cả công việc? (y/n): ")
    if xac_nhan.lower() == 'y':
        ds_cong_viec.clear()
        print("\nĐã xóa toàn bộ công việc.")
    else:
        print("\nKhông xóa. Danh sách vẫn giữ nguyên.")

def tim_kiem_cong_viec():
    tu_khoa = input("Nhập từ khóa cần tìm: ").lower()
    ket_qua = [cv for cv in ds_cong_viec if tu_khoa in cv['ten'].lower()]
    if ket_qua:
        print("\nKẾT QUẢ TÌM KIẾM:")
        for i, cv in enumerate(ket_qua, 1):
            print(f"{i}. {cv['ten']} - {cv['trang_thai']}")
    else:
        print("Không có công việc phù hợp")

def loc_cong_viec():
    tu_khoa = input("\nNhập từ cần lọc: ").lower()
    ket_qua = [cv for cv in ds_cong_viec if tu_khoa in cv['ten'].lower()]
    if ket_qua:
        print("\nCÔNG VIỆC TÌM ĐƯỢC:")
        for i, cv in enumerate(ket_qua, 1):
            print(f"{i}. {cv['ten']} - {cv['trang_thai']}")
    else:
        print("Không có công việc nào phù hợp")

def quan_ly_theo_thoi_gian():
    print("\n1. Xem theo ngày")
    print("2. Xem theo tuần")
    print("3. Xem theo tháng")
    chon = input("Chọn: ")
    try:
        if chon == "1":
            ngay = datetime.strptime(input("Nhập ngày (dd/mm/yyyy): "), "%d/%m/%Y").date()
            for cv in ds_cong_viec:
                if cv['ngay'].date() == ngay:
                    print(cv['ten'])
        elif chon == "2":
            ngay = datetime.strptime(input("Nhập ngày trong tuần (dd/mm/yyyy): "), "%d/%m/%Y")
            tuan = ngay.isocalendar()[1]
            for cv in ds_cong_viec:
                if cv['ngay'].isocalendar()[1] == tuan:
                    print(cv['ten'])
        elif chon == "3":
            thang, nam = map(int, input("Nhập tháng/năm (mm/yyyy): ").split("/"))
            for cv in ds_cong_viec:
                if cv['ngay'].month == thang and cv['ngay'].year == nam:
                    print(cv['ten'])
    except:
        print("Sai định dạng!")

def thong_ke_cong_viec():
    tong = len(ds_cong_viec)
    da_xong = sum(1 for cv in ds_cong_viec if cv['trang_thai'] == "Hoàn thành")
    chua_xong = tong - da_xong
    print("\n=== KẾT QUẢ THỐNG KÊ ===")
    print(f"Tổng công việc: {tong}")
    print(f"Đã hoàn thành: {da_xong}")
    print(f"Chưa hoàn thành: {chua_xong}")

# === MENU CHÍNH ===
def hien_thi_menu():
    print("\n====== ỨNG DỤNG QUẢN LÝ CÔNG VIỆC CÁ NHÂN ======")
    print("1. Thêm công việc mới")
    print("2. Thêm ngày giờ cho công việc")
    print("3. Đặt nhắc nhở cho công việc")
    print("4. Hiển thị tất cả công việc")
    print("5. Đếm số lượng công việc hiện tại")
    print("6. Chỉnh sửa công việc")
    print("7. Đánh dấu công việc là đã hoàn thành")
    print("8. Xóa công việc")
    print("9. Xóa toàn bộ công việc")
    print("10. Tìm kiếm công việc")
    print("11. Lọc công việc theo trạng thái hoặc thời gian")
    print("12. Quản lý công việc theo ngày, tuần, tháng")
    print("13. Thống kê công việc")
    print("0. Thoát chương trình")
    print("===============================================")

while True:
    hien_thi_menu()
    lua_chon = input("Vui lòng chọn chức năng (0–13): ")

    if lua_chon == '1':
        them_cong_viec_moi()
    elif lua_chon == '2':
        them_ngay_gio()
    elif lua_chon == '3':
        dat_nhac_nho()
    elif lua_chon == '4':
        hien_thi_cong_viec()
    elif lua_chon == '5':
        dem_cong_viec()
    elif lua_chon == '6':
        chinh_sua_cong_viec()
    elif lua_chon == '7':
        danh_dau_hoan_thanh()
    elif lua_chon == '8':
        xoa_cong_viec()
    elif lua_chon == '9':
        xoa_tat_ca_cong_viec()
    elif lua_chon == '10':
        tim_kiem_cong_viec()
    elif lua_chon == '11':
        loc_cong_viec()
    elif lua_chon == '12':
        quan_ly_theo_thoi_gian()
    elif lua_chon == '13':
        thong_ke_cong_viec()
    elif lua_chon == '0':
        print(">> Đã thoát chương trình. Tạm biệt!")
        break
    else:
        print(">> Lựa chọn không hợp lệ. Vui lòng thử lại.")
