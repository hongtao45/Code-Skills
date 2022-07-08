import sys
 
# 获取脚本名字
print('The name of this program is: %s' %(sys.argv[0]))
# 获取参数列表
print('The command line arguments are:')
for i in sys.argv:
    print(i)
# 统计参数个数
print('There are %s arguments.'%(len(sys.argv)-1))