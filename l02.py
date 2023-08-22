# In có định dạng:

number = 12.3456
print('%.2f' % number)
print('%10.2f' % number) # 10 khoảng từ phải qua trái
print('%010.2f' % number) # thay dấu cách bằng số 0
print('%-010.2f' % number) # dữ liệu in từ bên trái

print(f"{'%-010.2f' % number}")
print(f"{'%010.2f' % number}")

number2 = 6789
print('%10d' % number2)
print('%010.2d' % number2)
# f-float d-decimal