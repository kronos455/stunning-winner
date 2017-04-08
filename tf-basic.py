#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 19:07:41 2017

@author: bmitchell
"""

import tensorflow as tf

x = tf.constant(35, name='x')
y = tf.Variable(x+5, name='y')

model = tf.global_variables_initializer()

with tf.Session() as session:
    session.run(model)
    print(session.run(y))
    
