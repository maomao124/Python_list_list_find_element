"""
 * Project name(项目名称)：Python_list列表查找元素
 * Package(包名): 
 * File(文件名): test1
 * Author(作者）: mao
 * Author QQ：1296193245
 * GitHub：https://github.com/maomao124/
 * Date(创建日期)： 2022/3/22 
 * Time(创建时间)： 11:08
 * Version(版本): 1.0
 * Description(描述)：
 Python 列表（list）提供了 index() 和 count() 方法，它们都可以用来查找元素。
index() 方法
index() 方法用来查找某个元素在列表中出现的位置（也就是索引），如果该元素不存在，
则会导致 ValueError 错误，所以在查找之前最好使用 count() 方法判断一下。
list name.index(obj, start, end)
其中，list name 表示列表名称，obj 表示要查找的元素，start 表示起始位置，end 表示结束位置。
start 和 end 参数用来指定检索范围：
start 和 end 可以都不写，此时会检索整个列表；
如果只写 start 不写 end，那么表示检索从 start 到末尾的元素；
如果 start 和 end 都写，那么表示检索 start 和 end 之间的元素。

count()方法
count() 方法用来统计某个元素在列表中出现的次数
list name.count(obj)

其中，list name 代表列表名，obj 表示要统计的元素。

如果 count() 返回 0，就表示列表中不存在该元素，所以 count() 也可以用来判断列表中的某个元素是否存在。

 """

if __name__ == '__main__':
    num = list(range(0, 21))
    print(num)
    # 检索列表中的所有元素
    print(num.index(8))
    # 检索3~7之间的元素
    print(num.index(5, 3, 7))
    print(num.count(3))
    print(num.count(31))

    input()
