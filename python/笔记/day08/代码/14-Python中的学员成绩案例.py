# 1、定义学员信息类
class Student():
    # 2、定义学员对象属性
    def __init__(self, name, score):
        self.name = name
        self.score = score

    # 3、定义一个方法，用于打印学员的成绩等级
    def print_grade(self):
        if self.score >= 90:
            print(f'学员姓名：{self.name}，学员成绩：{self.score}，优秀')
        elif self.score >= 80:
            print(f'学员姓名：{self.name}，学员成绩：{self.score}，良好')
        elif self.score >= 70:
            print(f'学员姓名：{self.name}，学员成绩：{self.score}，中等')
        elif self.score >= 60:
            print(f'学员姓名：{self.name}，学员成绩：{self.score}，及格')
        else:
            print(f'学员姓名：{self.name}，学员成绩：{self.score}，不及格')

# 4、实例化对象
tom = Student('Tom', 80)
tom.print_grade()

jennifier = Student('Jennifier', 59)
jennifier.print_grade()