# -*- coding: utf-8 -*-
# @Time    : 18-3-24 上午10:36
# @Author  : Zwl
# @Email   : 944951481@qq.com
# @File    : 常量与变量.py
# @Software: PyCharm
import tensorflow as tf
# TODO 初始化常量
x = tf.constant(1.0)
y = tf.constant(2.0)
# TODO 进行加和
z = tf.add(x,y)

with tf.Session(graph=tf.get_default_graph()) as sess:
	z = sess.run(z)
	print(z)