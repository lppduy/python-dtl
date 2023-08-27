# if-else: dùng để kiểm tra một hay một nhóm điều kiện nào đó đúng hay sai

dtb = float(input('Mời nhập điểm trung bình: '))

if dtb >= 9 and dtb <= 10:
  print('Xuất sắc')
elif dtb >= 8 and dtb < 9:
  print('Giỏi')
elif dtb >= 6.5 and dtb < 8:
  print('Khá')
elif dtb >= 5 and dtb < 6.5:
  print('Trung bình')
elif dtb >= 0 and dtb < 5 :
  print('Thi lại')
else:
  print('Điểm không hợp lệ')
  