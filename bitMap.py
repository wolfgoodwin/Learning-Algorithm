
### 第一个函数是对Bitmap的一些简单应用。
### 第二个函数是利用Bitmap对大数据的一些处理

#!/usr/bin/env python
#coding: utf8

class Bitmap(object):
    def __init__(self, max):
        self.size  = self.calcElemIndex(max, True)
        self.array = [ 0 for i in range(self.size)]

    def calcElemIndex(self, num, up=False):
        '''up为True则为向上取整, 否则为向下取整'''
        if up:
            return int((num + 31 - 1) / 31) #向上取整
        return int(num / 31)

    def calcBitIndex(self, num):
        return num % 31

    def set(self, num):
        elemIndex = self.calcElemIndex(num)
        byteIndex = self.calcBitIndex(num)
        elem      = self.array[elemIndex]
        self.array[elemIndex] = elem | (1 << byteIndex)

    def clean(self, i):
        elemIndex = self.calcElemIndex(i)
        byteIndex = self.calcBitIndex(i)
        elem = self.array[elemIndex]
        self.array[elemIndex] = elem & (~ (1 << byteIndex))

    def test(self, i):
        elemIndex = self.calcElemIndex(i)
        byteIndex = self.calcBitIndex(i)
        if self.array[elemIndex] & (1 << byteIndex):
            return True
        return False


if __name__ == '__main__':
    bitmap = Bitmap(90)
    bitmap.set(47)
    print ('数组需要 %d 个元素。' % bitmap.size)
    print ('47 应存储在第 %d 个数组元素上。' % bitmap.calcElemIndex(47))
    print('47 应存储在第 %d 个数组元素的第 %d 位上。' % (bitmap.calcElemIndex(47), bitmap.calcBitIndex(47),))

    print(bitmap.array)
    bitmap.set(5)
    bitmap.clean(5)
    print(bitmap.array)
    print(bitmap.test(5))



import random
import time

class Bitmap(object):
    def __init__(self, max):
        self.size = self.calcElemIndex(max, True)
        self.array = [0 for i in range(self.size)]

    def calcElemIndex(self, num, up=False):
        '''up为True则为向上取整, 否则为向下取整'''
        if up:
            return int((num + 31 - 1) / 31)  # 向上取整
        return int(num / 31)

    def calcBitIndex(self, num):
        return num % 31

    def set(self, num):
        elemIndex = self.calcElemIndex(num)
        byteIndex = self.calcBitIndex(num)
        elem = self.array[elemIndex]
        self.array[elemIndex] = elem | (1 << byteIndex)

    def clean(self, i):
        elemIndex = self.calcElemIndex(i)
        byteIndex = self.calcBitIndex(i)
        elem = self.array[elemIndex]
        self.array[elemIndex] = elem & (~(1 << byteIndex))

    def test(self, i):
        elemIndex = self.calcElemIndex(i)
        byteIndex = self.calcBitIndex(i)
        if self.array[int(elemIndex)] & (1 << byteIndex):
            return True
        return False


if __name__ == '__main__':
    MAX = 100000001
    list = random.sample(range(1,100000001),100000000)
    t0 = time.time()
    result = []
    bitmap = Bitmap(MAX)
    for num in list:
        bitmap.set(num)

    for i in range(MAX + 1):
        if bitmap.test(i):
            result.append(i)
    t1 = time.time()
    #print('原始数组为:    %s' % list)
    #print( '排序后的数组为: %s' % result)
    print(t1-t0)

