def hien_thi_cong_viec():
    print("\n=== DANH SÁCH CÔNG VIỆC ===")
    
    # Danh sách công việc mẫu (mỗi công việc là 1 dictionary)
    cong_viec = [
        {
            "ten": "Kiểm tra hệ thống",
            "nguoi_pt": "Nguyễn Mạnh Hùng",
            "trang_thai": "Đang làm"
        },
        {
            "ten": "Cập nhật phần mềm",
            "nguoi_pt": "Trần Thị Bích",
            "trang_thai": "Hoàn thành"
        },
    ]
    
    if len(cong_viec) == 0:
        print("Chưa có công việc nào")
    else:
        stt = 1
        for cv in cong_viec:
            print(f"{stt}. {cv['ten']}")
            print(f"   Người phụ trách: {cv['nguoi_pt']}")
            print(f"   Trạng thái: {cv['trang_thai']}\n")
            stt += 1

# Chạy chương trình
hien_thi_cong_viec()