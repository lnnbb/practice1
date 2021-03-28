print('hello,world!')
# a = int(input('1.请输入：'))
# b = int(input('2.请输入：'))   
# print('a + b =',a+b)          #ctrl+/

print('I love you')  #字符串
print('I love you '*10)
print('I love you','Me,too')
print(len('I love you'))  #len()计算字符串长度
# '''请分别输入两段字符串，并计算器其长度和'''
# a1 = input('请输入：')
# a2 = input('请输入：')
# print('长度和为：',len(a1)+len(a2))

print(233)         #整数 int型
print(2.33)        #小数 float型
a = float(244)     #数据类型转换 int(),float()
print(a)           #244.0

print(True)        #布尔值 True/False；打印True

b = (1,2,3,'哈哈','哈哈','哈哈',True)  #元组tuple
print(b)           #元组tuple；打印(1,2,3,'哈哈','哈哈','哈哈',True)
print(b.index(1))  #打印0
print(b.count('哈哈'))  #count()计数；打印3

print(b[3])        #下标；打印哈哈
print(b[1:6])      #左闭右开，打印第二个数到第六个数，从0开始计数；
print(b[:5:2])     #切片，间隔为2
c = (b,'嘻嘻','abc',23.0)  #二维元组;c中有四个元素
print(c[0][2])     # 打印二维数组；打印b中的3

d = ['abc reading','嗨',1.0,False,37]  #数组list,同元组方法一样：index()、count()，切片；
print(d)           #数组list;打印['abc reading','嗨',1.0,False,37]
d.append('sorry')  #在数组末尾添加元素‘sorry’；
print(d)
d.insert(2,985)
print(d)
e = d.pop(3)           #相当于剪切，取出数组中的某个值
print(e)
d.extend(['hhh','996',0])  #在数组后添加数组
print(d)
d.remove('996‘)        #删除某值 


# print({})      #字典dict；