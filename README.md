# chessAI
# 使用alphazero算法打造属于你自己的象棋AI


## 一、深度学习框架及项目说明：
pytorch和paddle

使用蒙特卡洛树+象棋逻辑+神经网络推理出最佳走子，并记录每一步棋局，棋局作为样本用于神经网络训练策略网络和价值网络，labels为棋局走子，策略推理+神经网络两者相辅相成。
神经网络骨干网络主要是残差块堆叠+卷积抽取以棋盘棋局连续走子表示成的多层的图的特征，策略网络输出层为2086个所有走子集合，价值网络输出当前最佳走子后的价值。
蒙特卡洛树一次走子要用升级网络进行上千次的推理，所以必须要使用GPU训练！


## 二、项目为多进程同步训练。
用redis存储博弈棋局用于训练，训练时，在终端运行python collect.py用于自我对弈产生数据，这个可以多开，我开了4个。

然后，在终端运行python train.py用于模型训练，这个终端只用开一个。

## 三、训练现状
截止提交项目时已训练了3000 batchs， totoal loss在2.0出头， 策略网络价值0.9+(满值为1)。
AI已经学会了弃子保将，并且开局几步有了一定的走棋棋风，还需要继续训练下去，训练batch一般以万为单位。

问题：强化学习需要AI进行大量的试错，博弈树也对训练至关重要，前期无法快速形成较高的棋力，有先用专家棋谱进行模仿训练快速提升棋力的想法，但目前找不到大量的专家样本。

## 四、相关资源链接

知乎文章：https://zhuanlan.zhihu.com/p/528824058?


## 五、reference
1、程世东 https://zhuanlan.zhihu.com/p/34433581 （中国象棋cchesszero ）

2、AI在打野 https://aistudio.baidu.com/aistudio/projectdetail/1403398 （用paddle打造的五子棋AI）

3、junxiaosong https://github.com/junxiaosong/AlphaZero_Gomoku (五子棋alphazero)

4、书籍：边做边学深度强化学习：PyTorch 程序设计实践

5、书籍：强化学习第二版
】
