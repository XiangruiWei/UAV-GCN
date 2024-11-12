import numpy as np

# 加载 .npy 文件
data = np.load('fused_score_ctrgcn_blockgcn.npy')

# 查看数据的形状
print(data.shape)