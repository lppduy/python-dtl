# Section 6 - Lession 21

# Lập trình hướng đối tượng OOP

# Lập trình xoay quanh đối tượng: Mô phỏng, mô tả, 
# thể hiện được chính xác, chân thật nhất có thể các sự vật, hiện tượng 
# trong thực tế cũng như trong tưởng tượng

# Mỗi một đối tượng bao gồm 2 thành phần (member) cơ bản
# - Các đặc điểm đặc trung của đối tượng => Các thuộc tính => sử dụng các biến để lưu trữ 
# - Các hành vi của đối tượng => Các phương thức => Sử dụng các hàm để biểu diễn, mô phỏng, thể hiện

# Sử dụng class (lớp) để làm nơi đặc các thuộc tính, phương thức

# Cú pháp:
# class Tên_Class:
  # khai_báo_các_thuộc_tính
  # định_nghĩa_các_phương_thức

class Animal:
  ID = 1234
  name= 'Moon'
  gender= 'Male'
  age= 1.5

  def move(self):
    print('Run,swim,fly,...')

  def speak(self):
    print('Go go,meo meo, roar,...')
  def inputInfo(self):
    self.ID = input('Input ID: ')
    self.name = input('Input name: ')
    self.gender = input('Input gender: ')
    self.age = float(input('Input age: '))
    while self.age <0:
      self.age = float(input('Re-input age: '))
  def showInfo(self):
    print(f'ID = {self.ID}')
    print(f'name = {self.name}')
    print(f'Gender = {self.gender}')
    print(f'Age = {self.age}')

# Self: Đại diện cho đối tượng hiện thời - đối tượng gọi đến phương thức chứa self
# Tạo đối tượng:
cat = Animal()
# Truy cập các đối tượng: sử dụng toán tử (.)
cat.move()
cat.inputInfo()
cat.showInfo()
# cat.ID = 5678 #set
# print(cat.ID) #get
dog = Animal()
dog.inputInfo() # lúc này self là dog