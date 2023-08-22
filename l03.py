# Nhập liệu (input)
# ***** 1. nhập dữ liệu chuỗi
name = input('Input your name: ')

# = : gán/lưu
# name: biến (variable)  -> do developer tự đặt
# 1. k dc có dấu cách (a b)
# 2. phải bắt đầu bằng ký tự chữ cái hoặc _ (a1, _st,...)
# 3. Không được chứa phép toán 
# 4. Không được trùng từ khoá 
# 5. Không trùng với những tên đã có 

print(f'Your name is {name}')
print('Your name is ' + name)
print('Your name is ' , name)
print(f"""
{name}
""")

# ***** 2. Nhập dữ liệu số nguyên 
number1 = int(input('Input an integer number: '))

print(f'Number1 = {number1}')

# ***** 3. Nhập dữ liệu số thực 
number2 =float(input('Input an real number: '))
print(f"Number2 = {number2}")