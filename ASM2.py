#!/usr/bin/env python
# coding: utf-8

# In[30]:


import json
import os

class HanhChinh:
    def __init__(self, ma_nv, ten, luong):
        self.ma_nv = ma_nv
        self.ten = ten
        self.luong = luong

    def tinh_thu_nhap(self):
        return self.luong - self.tinh_thue()

    def tinh_thue(self):
        thu_nhap = self.luong
        if thu_nhap < 9000000:
            return 0
        elif 9000000 <= thu_nhap <= 15000000:
            return (thu_nhap - 9000000) * 0.1
        else:
            return (6000000 * 0.1) + (thu_nhap - 15000000) * 0.12

    def xuat(self):
        return {
            'Mã nhân viên': self.ma_nv,
            'Tên nhân viên': self.ten,
            'Lương': self.luong,
            'Thuế': self.tinh_thue(),
            'Thu nhập': self.tinh_thu_nhap(),
        }

class TiepThi(HanhChinh):
    def __init__(self, ma_nv, ten, luong, doanhso_banhang, hoa_hong):
        super().__init__(ma_nv, ten, luong)
        self.doanhso_banhang = doanhso_banhang
        self.hoa_hong = hoa_hong

    def tinh_thu_nhap(self):
        return (self.luong + self.doanhso_banhang * self.hoa_hong) - self.tinh_thue()

    def xuat(self):
        data = super().xuat()
        data.update({
            'Doanh số bán hàng': self.doanhso_banhang,
            'Tiền hoa hồng': self.hoa_hong,
            'Thu nhập': self.tinh_thu_nhap(),
        })
        return data

class TruongPhong(HanhChinh):
    def __init__(self, ma_nv, ten, luong, luong_trachnhiem):
        super().__init__(ma_nv, ten, luong)
        self.luong_trachnhiem = luong_trachnhiem

    def tinh_thu_nhap(self):
        return (self.luong + self.luong_trachnhiem) - self.tinh_thue()

    def xuat(self):
        data = super().xuat()
        data.update({
            'Lương trách nhiệm': self.luong_trachnhiem,
            'Thu nhập': self.tinh_thu_nhap(),
        })
        return data


# In[31]:


def nhap_nv():
    danhsach_nv = doc_danh_sach_nv_tu_file()
    print("Gồm 3 loại nhân viên:\n1. Nhân viên hành chính \n2. Nhân viên tiếp thị \n3. Trưởng phòng\n*Nhập 's' để dừng lại.")
    
    while True:
        loai = input("Chọn loại nhân viên: ")
        if loai.lower() == 's':
            break
        ma_nv = input("Nhập mã nhân viên (bắt đầu bằng MNV): ")
        ten = input("Nhập họ và tên: ")
        luong = float(input("Nhập lương hàng tháng: "))

        if loai == '1':
            thongtin = HanhChinh(ma_nv, ten, luong)
        elif loai == '2':
            doanhso_banhang = int(input("Nhập doanh số bán hàng: "))
            hoa_hong = float(input("Nhập tiền hoa hồng được nhận: "))
            thongtin = TiepThi(ma_nv, ten, luong, doanhso_banhang, hoa_hong)
        elif loai == '3':
            luong_trachnhiem = float(input("Nhập lương trách nhiệm: "))
            thongtin = TruongPhong(ma_nv, ten, luong, luong_trachnhiem)
        else:
            print("Loại nhân viên không hợp lệ, vui lòng nhập lại.")
            continue

        danhsach_nv.append(thongtin.xuat())

    with open("danhsach_nhanvien.json", "w", encoding="utf-8") as f:
        json.dump(danhsach_nv, f, ensure_ascii=False, indent=4)  

    print("Thông tin nhân viên đã được lưu vào file danhsach_nhanvien.json.")


# In[32]:


def doc_danh_sach_nv_tu_file():

    if os.path.exists("danhsach_nhanvien.json"):
        with open("danhsach_nhanvien.json", "r", encoding="utf-8") as f:
            try:
                return json.load(f)  
            except json.JSONDecodeError:
                return [] 
    return []  


# In[33]:


def tim_nv_theo_ma():
    ma_nv_tim = input("Nhập mã nhân viên cần tìm: ")  
    danhsach_nv = doc_danh_sach_nv_tu_file() 
    nhanvien = next((nv for nv in danhsach_nv if nv['Mã nhân viên'] == ma_nv_tim), None)
    
    if nhanvien:
        print("Nhân viên tìm thấy:")
        print(json.dumps(nhanvien, ensure_ascii=False, indent=4))  
    else:
        print(f"Không tìm thấy nhân viên có mã: {ma_nv_tim}")


# In[34]:


def xoa_nv_theo_ma():
    ma_nv_xoa = input("Nhập mã nhân viên cần xóa (MNV): ")
    danhsach_nv = doc_danh_sach_nv_tu_file()
    nhanvien_can_xoa = next((nv for nv in danhsach_nv if nv['Mã nhân viên'] == ma_nv_xoa), None)
    if nhanvien_can_xoa:
        danhsach_nv.remove(nhanvien_can_xoa)
        with open("danhsach_nhanvien.json", "w", encoding="utf-8") as f:
            json.dump(danhsach_nv, f, ensure_ascii=False, indent=4)  
        print(f"Đã xóa nhân viên có mã: {ma_nv_xoa}")
    else:
        print(f"Không tìm thấy nhân viên có mã: {ma_nv_xoa}")


# In[35]:


def tim_luong_nv():
    luong_min = float(input("Nhập lương tối thiểu: "))
    luong_max = float(input("Nhập lương tối đa: "))
    danhsach_nv = doc_danh_sach_nv_tu_file()
    
    nhanvien_trongkhoang = [
        nv for nv in danhsach_nv
        if luong_min <= nv['Lương'] <= luong_max
    ]
    if nhanvien_trongkhoang:
        print(f"Nhân viên có lương trong khoảng từ {luong_min} đến {luong_max}:")
        for nv in nhanvien_trongkhoang:
            print(json.dumps(nv,ensure_ascii = False, indent = 4))
    else:
        print(f"Không tìm thấy nhân viên trong khoảng từ {luong_min} đến {luong_max}")


# In[36]:


def sap_xep_nv():
    danhsach_nv = doc_danh_sach_nv_tu_file()
    danhsach_nv_sapxep = sorted(danhsach_nv,key = lambda nv:nv['Tên nhân viên'])
    print('Danh sách sau khi được sắp xếp họ và tên: ')
    for nv in danhsach_nv_sapxep:
        print(json.dumps(nv,ensure_ascii = False,indent = 4))


# In[38]:


def sap_xep_thu_nhap():
    danhsach_nv = doc_danh_sach_nv_tu_file()
    danhsach_nv_sapxep_thunhap = []

    for nv in danhsach_nv:
        ma_nv = nv['Mã nhân viên']
        ten = nv['Tên nhân viên']
        luong = nv['Lương']
        
        if 'Doanh số bán hàng' in nv:  # Nếu là nhân viên tiếp thị
            doanhso_banhang = nv['Doanh số bán hàng']
            hoa_hong = nv['Tiền hoa hồng']
            nhanvien = TiepThi(ma_nv, ten, luong, doanhso_banhang, hoa_hong)
        elif 'Lương trách nhiệm' in nv: 
            luong_trachnhiem = nv['Lương trách nhiệm']
            nhanvien = TruongPhong(ma_nv, ten, luong, luong_trachnhiem)
        else:  
            nhanvien = HanhChinh(ma_nv, ten, luong)

        danhsach_nv_sapxep_thunhap.append(nhanvien.xuat())

    danhsach_nv_sapxep_thunhap = sorted(danhsach_nv_sapxep_thunhap, key=lambda nv: nv['Thu nhập'])

    print('Danh sách sau khi được sắp xếp theo thu nhập: ')
    for nv in danhsach_nv_sapxep_thunhap:
        print(json.dumps(nv, ensure_ascii=False, indent=4))


# In[40]:


def xuat_5_nv_thu_nhap_cao_nhat():
    danhsach_nv = doc_danh_sach_nv_tu_file()
    danhsach_nv_sapxep_thunhap = []

    for nv in danhsach_nv:
        ma_nv = nv['Mã nhân viên']
        ten = nv['Tên nhân viên']
        luong = nv['Lương']
        
        if 'Doanh số bán hàng' in nv: 
            doanhso_banhang = nv['Doanh số bán hàng']
            hoa_hong = nv['Tiền hoa hồng']
            nhanvien = TiepThi(ma_nv, ten, luong, doanhso_banhang, hoa_hong)
        elif 'Lương trách nhiệm' in nv:
            luong_trachnhiem = nv['Lương trách nhiệm']
            nhanvien = TruongPhong(ma_nv, ten, luong, luong_trachnhiem)
        else:
            nhanvien = HanhChinh(ma_nv, ten, luong)

        danhsach_nv_sapxep_thunhap.append(nhanvien.xuat())

    danhsach_nv_sapxep_thunhap = sorted(danhsach_nv_sapxep_thunhap, key=lambda nv: nv['Thu nhập'], reverse=True)

    top_5_nv = danhsach_nv_sapxep_thunhap[:5]

    print('5 nhân viên có thu nhập cao nhất: ')
    for nv in top_5_nv:
        print(json.dumps(nv, ensure_ascii=False, indent=4))


# In[ ]:




