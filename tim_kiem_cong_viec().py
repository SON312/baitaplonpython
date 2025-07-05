def tim_kiem_cong_viec():
    # Bước 1: Nhập danh sách công việc
    print("NHẬP CÔNG VIỆC (gõ 'xong' để dừng)")
    cong_viec = []
    while True:
        ten = input("Nhập tên công việc: ")
        if ten.lower() == 'xong':
            break
        cong_viec.append(ten)
    
    # Bước 2: Hiển thị danh sách vừa nhập
    print("\nDANH SÁCH CỦA BẠN:")
    for i, ten in enumerate(cong_viec, 1):
        print(f"{i}. {ten}")
    
    # Bước 3: Tìm kiếm
    if cong_viec:
        tukhoa = input("\nNhập từ cần tìm: ").lower()
        print("\nKẾT QUẢ:")
        
        found = False
        for ten in cong_viec:
            if tukhoa in ten.lower():
                print(f"- {ten}")
                found = True
        
        if not found:
            print("Không tìm thấy!")
    else:
        print("\nDanh sách trống!")

# Chạy chương trình
print("CHƯƠNG TRÌNH TÌM KIẾM ĐƠN GIẢN")
tim_kiem_cong_viec()