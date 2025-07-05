#codeMENU.py
def them_cong_viec():
    print(">> Thêm công việc mới")

def them_ngay_gio():
    print(">> Thêm ngày giờ cho công việc")

def dat_nhac_nho():
    print(">> Đặt nhắc nhở cho công việc")

def hien_thi_cong_viec():
    print(">> Hiển thị tất cả công việc")

def dem_cong_viec():
    print(">> Đếm số lượng công việc hiện tại")

def chinh_sua_cong_viec():
    print(">> Chỉnh sửa công việc")

def danh_dau_hoan_thanh():
    print(">> Đánh dấu công việc là đã hoàn thành")

def xoa_cong_viec():
    print(">> Xóa một công việc")

def xoa_tat_ca_cong_viec():
    print(">> Xóa toàn bộ công việc")

def tim_kiem_cong_viec():
    print(">> Tìm kiếm công việc")

def loc_cong_viec():
    print(">> Lọc công việc theo trạng thái hoặc thời gian")

def quan_ly_theo_thoi_gian():
    print(">> Quản lý công việc theo ngày/tuần/tháng")

def thong_ke_cong_viec():
    print(">> Thống kê công việc")

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

# Vòng lặp menu chính
while True:
    hien_thi_menu()
    lua_chon = input("Vui lòng chọn chức năng (0–13): ")

    if lua_chon == '1':
        them_cong_viec()
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
