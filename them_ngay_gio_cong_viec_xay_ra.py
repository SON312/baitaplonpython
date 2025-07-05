# Hàm thêm/cập nhật ngày giờ công việc
def them_ngay_gio_cong_viec(tu_dien_cv):
    print("=== THÊM NGÀY GIỜ CÔNG VIỆC XẢY RA ===")
    """Hàm thêm/cập nhật ngày giờ công việc vào từ điển"""
    ten = input("Nhập tên: ")
    ngay_gio = input("Nhập ngày giờ công việc xảy ra (dd/mm/yyyy HH:MM): ")
    
    tu_dien_cv[ten] = ngay_gio  
    
    if ten in tu_dien_cv:
        print(f"Đã cập nhật công việc  '{ten}' vào lúc: {ngay_gio}")
    else:
        print(f"Đã thêm công việc mới  '{ten}' vào lúc: {ngay_gio}")
# Gọi hàm và kiểm tra kết quả
cong_viec_dict = {}
them_ngay_gio_cong_viec(cong_viec_dict)

print("\nTừ điển công việc hiện tại:")
print(cong_viec_dict)