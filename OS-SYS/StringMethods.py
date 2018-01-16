# 字符串的用法

import string, sys, os, subprocess, glob
#
# mystr = '  wo yao shi xian zi wo tu po  '
#
#
# print(mystr.find('yao'))
#
# print('wo' in mystr)
#
# print(mystr.strip())                #去除两边空格
#
# print(mystr.replace('wo', 'ni'))
#
# print(mystr.upper())
#
# print(string.ascii_lowercase)
#
# print(string.ascii_uppercase)
#
# print(string.ascii_letters)
#
# mystr = 'aaa,bbb,ccc'
#
# print(mystr.split(','))
#
# print(''.join(['aaa', 'bbb', 'ccc']))
#
# print(list(mystr.replace(',', '')))
#
# print(int('42'), eval('42'), str(42), repr(42))
#
# print("42"+str(1), 42+1)
#
# with open('file') as f:
#     print(f.read())
#     # print(f.read(15))                  #生成字符串
#     # print(f.readline())                #读一行
#     # print(f.readlines())               #按行生成列表
#
# # dir(sys)
# # help(sys)
#
# print(sys.platform)
# print(sys.version)
# sys.path.append('/root')
# print(sys.path)
# print(sys.modules)              # 被导入的模块
# print(sys.getrefcount(string))  # string被引用次数
# print(sys.exc_info())           # 最近异常信息
#
#
# print(os.getcwd())                                      #当前目录
# print(os.getpid())
# # os.chdir('/home/wenduzi')                               #转换目录
# print(os.getcwd())
# # os.chdir('/home/wenduzi/PycharmProjects/OS-SYS')
# print(os.path.exists('file'))                           # file是否存在
# print(os.path.getsize('file'))                          # file大小
# # print(os.path.split('/home/wenduzi/examples.desktop'))  # 分离文件名
# print(os.path.join('/root','wenduzi'))                  # 合成文件名
# print(os.sep)                                           # 目录分隔符，无关底层操作系统

# print(os.system('python Hello.py'))                     # 执行系统命令

# print(os.mkdir())
# print(os.remove())
# print(os.execlp())
# print(os.fork())
# print(os.environ)
import glob

# for (directory, subdirectory, file) in os.walk('/PycharmProjects/Package-Module/'):
#     print(directory)
#     for name in file:
#         path = os.path.join(directory, name)
#         print(path)

dirname = '/PycharmProjects/Package-Module/OS-SYS'


for file in glob.glob(dirname + '/*'):
    a, b = os.path.split(file)
    # print(a,b)
    if b.endswith('.py'):
        print(b)

# print('\n')
# print('\n')
#
# for file in os.listdir(dirname):
#     a = os.path.join(dirname,file)
#     print(a)
#
# print(sys.getdefaultencoding())
# print(sys.getfilesystemencoding())







