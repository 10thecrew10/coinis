# class User:
#     def __init__(self):
#         print('User init')
#
#     def who_am_i(self):
#         print('I am User')
#
#     def login(self):
#         print('User Login')
#
#
# class Admin(User):
#     def __init__(self):
#         super()
#         print('Admin init')
#
#     def who_am_i(self):
#         print('I am admin')
#
#     def delete_user(self):
#         print('I can delete User')
#
# u1 = User()
# a1 = Admin()
#
# u1.who_am_i()
# a1.who_am_i()
#
# a1.login()

# class Rectangle:
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width
#
#     def area(self):
#         return self.length * self.width
#
#     def perimeter(self):
#         return 2 * (self.length + self.width)
#
#
# class Square(Rectangle):
#     def __init__(self, length):
#         super().__init__(length, length)
#
#
# r1 = Rectangle(4, 2)
# print(r1.area())
# print(r1.perimeter())
#
# s1 = Square(4)
# print(s1.area())
# print(s1.perimeter())


# class Book:
#     def __init__(self, title, author, pages):
#         self.title = title
#         self.author = author
#         self.pages = pages
#
#     def __str__(self):
#         return f'{self.title} - {self.author}'
#
#     def __len__(self):
#         return self.pages
#
#     def __del__(self):
#         print(f'Book "{self.title}" deleted')
#
#     def __gt__(self, other):
#         return self.pages > other.pages
#
#
# b1 = Book('1984', 'D. Oruel', 500)
# b2 = Book('Atlas Shrugged', 'Ayn Rand', 3000)
# b3 = Book('How to turn 5 dollars into 50 billion', 'Robert G. Hagstrom', 800)
#
# l = [b1, b2, b3]
# print(len(l[0]))
# print(l[0] > l[1])
# for x in l:
#     print(x)
#
# print(l[0] < l[1])


f = open('week-5/file.txt')
f.read()
f.read() # пустое содержание, поскольу указатель в конце файла f.seek(0)
f.close()

# import os
# os.remove("file_name")
# os.remove("directory_name")