height = float(input('请输入您的身高（m）：'))
weight = float(input('请输入您的体重（kg）：'))

bmi = weight / height ** 2

print(f'您的BMI值为{bmi}')