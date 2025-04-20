def tinh_diem_tong_ket(diem_gk, diem_ck):
    return 0.4 * diem_gk + 0.6 * diem_ck

def nhap_danh_sach_sinh_vien():
    danh_sach = []
    n = int(input("Nhập số lượng sinh viên: "))
    for i in range(n):
        print(f"\nNhập thông tin sinh viên thứ {i+1}:")
        ma_sv = input("  Mã SV: ")
        ho_ten = input("  Họ tên: ")
        diem_gk = float(input("  Điểm giữa kỳ: "))
        diem_ck = float(input("  Điểm cuối kỳ: "))
        sv = {
            "MaSV": ma_sv,
            "HoTen": ho_ten,
            "DiemGK": diem_gk,
            "DiemCK": diem_ck,
            "DiemTK": tinh_diem_tong_ket(diem_gk, diem_ck)
        }
        danh_sach.append(sv)
    return danh_sach

def in_danh_sach(danh_sach):
    print("\nDanh sách sinh viên và điểm tổng kết:")
    for sv in danh_sach:
        print(f'{sv["MaSV"]} - {sv["HoTen"]}: GK = {sv["DiemGK"]}, CK = {sv["DiemCK"]}, TK = {sv["DiemTK"]:.2f}')

def tim_sv_diem_cao(danh_sach):
    print("\nSinh viên có điểm TK >= 8.0:")
    for sv in danh_sach:
        if sv["DiemTK"] >= 8.0:
            print(f'{sv["MaSV"]} - {sv["HoTen"]}: {sv["DiemTK"]:.2f}')

def dem_sv_diem_thap(danh_sach):
    count = sum(1 for sv in danh_sach if sv["DiemGK"] < 5 or sv["DiemCK"] < 5)
    print(f"\nSố sinh viên có điểm GK < 5 hoặc CK < 5: {count}")

def in_3_dau_3_cuoi(danh_sach):
    ds_diem_tk = [sv["DiemTK"] for sv in danh_sach]
    print("\nBa điểm tổng kết đầu tiên:", ds_diem_tk[:3])
    print("Ba điểm tổng kết cuối cùng:", ds_diem_tk[-3:])

# Chương trình chính
danh_sach_sv = nhap_danh_sach_sinh_vien()
in_danh_sach(danh_sach_sv)
tim_sv_diem_cao(danh_sach_sv)
dem_sv_diem_thap(danh_sach_sv)
in_3_dau_3_cuoi(danh_sach_sv)
