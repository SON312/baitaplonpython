def loc_cong_viec():
    # Bước 1: Nhập danh sách công việc
    print("\nNHẬP CÔNG VIỆC CỦA BẠN")
    print("(Gõ 'xong' khi đã nhập xong)\n")
    
    ds_cong_viec = []
    while True:
        ten = input("Nhập công việc: ")
        if ten.lower() == 'xong':
            break
        ds_cong_viec.append(ten)
    
    # Bước 2: Hiển thị danh sách
    print("\nDANH SÁCH CỦA BẠN:")
    if not ds_cong_viec:
        print("(Trống)")
        return
    
    for i, ten in enumerate(ds_cong_viec, 1):
        print(f"{i}. {ten}")
    
    # Bước 3: Lọc công việc
    tu_khoa = input("\nNhập từ cần tìm: ").lower()
    ket_qua = []
    
    for ten in ds_cong_viec:
        if tu_khoa in ten.lower():
            ket_qua.append(ten)
    
    # Bước 4: Hiển thị kết quả
    print("\nCÔNG VIỆC TÌM ĐƯỢC:")
    if ket_qua:
        for i, ten in enumerate(ket_qua, 1):
            print(f"{i}. {ten}")
    else:
        print("Không có công việc nào phù hợp")

# Chạy chương trình
print("CHƯƠNG TRÌNH LỌC CÔNG VIỆC ĐƠN GIẢN")
loc_cong_viec()