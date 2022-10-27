str2 = 'avatar.ppt'
print(str2.endswith('.png'))

if str2.endswith('.png') or str2.endswith('.jpg') or str2.endswith('.gif'):
    print('是一张图片格式的图片')
else:
    print('您上传的文件格式异常')