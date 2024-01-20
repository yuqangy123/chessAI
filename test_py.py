# coding=utf-8
import numpy as np
import copy
import time
from config import CONFIG
from collections import deque   # 这个队列用来判断长将或长捉
import d2l.torch as d2l
import torch
import torch.nn.functional as F


que = deque(maxlen=2)

def softmax(X):
    exp_X = torch.exp(X)
    partition = exp_X.sum(dim=1, keepdim=True)
    return exp_X/partition

for i in range(4):
    tensor = torch.randn(size=(4,4)).to(d2l.try_gpu())
    tensor = tensor.clone()
    que.append(tensor)


policy = torch.randn(size=(4,4)).to(d2l.try_gpu())
print(policy)
a=softmax(policy)
print(a.sum(dim=1), a)
print(F.log_softmax(policy))
nnsoftmax=torch.nn.LogSoftmax()
a = nnsoftmax(policy)
print(a.sum(dim=1), a)
a = torch.exp(a)
print(a.sum(dim=1), a)#e^(log(softmax))


a = 0