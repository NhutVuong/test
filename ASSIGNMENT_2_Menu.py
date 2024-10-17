#!/usr/bin/env python
# coding: utf-8

# In[4]:


from ASM2 import nhap_nv,doc_danh_sach_nv_tu_file,tim_nv_theo_ma,xoa_nv_theo_ma,tim_luong_nv,sap_xep_nv,sap_xep_thu_nhap,xuat_5_nv_thu_nhap_cao_nhat
def menu():
    while True:
        print(
'''+----------------------------------------------------------------------------------+
|1.Nhập danh sách nhân viên.Lưu thông tin vào file.                                |
|2.Đọc thông tin nhân viên từ file và xuất ra danh sách nhân viên ra màn hình.     |
|3.Tìm và hiển thị nhân viên theo mã nhập từ bàn phím.                             |
|4.Xóa nhân viên theo mã nhập từ bàn phím.Cập nhật file dữ liệu.                   | |
|5.Tìm các nhân viên theo khoảng lương nhập từ bàn phím.                           | 
|6.Sắp xếp nhân viên theo họ và tên.                                               |
|7.Sắp xếp nhân viên theo thu nhập.                                                |
|8.Xuất 5 nhân viên có thu nhập cao nhất.                                          |
|0.Kết thúc chương trình.                                                         |
+----------------------------------------------------------------------------------+        ''')
        chon = input("Chọn chức năng: ")
        match chon:
            case '1':
                nhap_nv()
                
            case '2':
                danh_sach = doc_danh_sach_nv_tu_file()
                for nv in danh_sach:
                    print(nv)

            case '3':
                tim_nv_theo_ma()
                
            case '4':
                xoa_nv_theo_ma()
                
            case '5':
                tim_luong_nv()
                
            case '6':
                sap_xep_nv()
                
            case '7':
                sap_xep_thu_nhap()
                
            case '8':
                xuat_5_nv_thu_nhap_cao_nhat()
                
            case '0':
                print("Kết thúc chương trình.")
                break
                
            case _:
                print("Chọn sai chức năng.Vui lòng chọn lại")
if __name__=="__main__":
    menu()
          
        

