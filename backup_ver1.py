import os
import time

# 需要备份文件的地址
source = ['D:\\My Documents']

# 备份目录
target_dir = 'D:\\Backup'

# 备份文件打包成zip，文件以时间命名
target = target_dir + os.sep + time.strftime('%Y%m%d%H%M%S') + '.zip'
# 如果目录不存在，创建目录
if not os.path.exists(target_dir):
    os.mkdir(target_dir)
# zip命令打包
zip_command = 'zip -r {0} {1}'.format(target, ' '.join(source))
# 运行
print('Zip command is:')
print(zip_command)
print('Running:')
if os.system(zip_command) == 0:
    print('Successful backup to', target)
else:
    print('Backup FAILED')