# Vòng lặp while:

# while điều_kiện:
  # khối lệnh

# VD1: Mời nhập điểm trung bình, yêu cầu điểm phải nằm trong đoạn [0,10]

# dtb = float(input('Mời nhập điểm trung bình: '))

# while not(0<=dtb and dtb<=10):
#   dtb = float(input('Điểm không hợp lệ. Mời nhập lại: '))
# print(f'Điểm nhập vào là: {dtb}')

# VD2: In ra các số từ 1-10

# count = 1
# while count <= 10:
#   print(count)
#   count += 1
# # VD3: In ra các số từ 10-1

# count = 10
# while count >= 1:
#   print(count)
#   count +- 1

# VD4: In ra các số chia hết cho 3 trong đoạn [1,100]

count = 1
while count <= 100:
  if count % 3 == 0:
    print(count)
  count += 1
