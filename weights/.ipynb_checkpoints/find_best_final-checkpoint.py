import argparse  
import pickle  
import os  
import numpy as np  
from tqdm import tqdm  # 导入 tqdm
from skopt import gp_minimize
from skopt.space import Integer

def objective(alpha, r1, r2, r3, r4, r5, r6, r7, label, pbar):  
    """  
    目标函数，用于贝叶斯优化  
    """  
    right_num = 0  
    total_num = 0  
    
    # 将 alpha 还原为精度为 0.01 的浮动值
    alpha = [a / 100.0 for a in alpha]  # 恢复为小数精度
    
    for i in range(len(label)):  
        l = label[i]  
        # 获取每个模型的预测值
        _, r1_pred = r1[i]  
        _, r2_pred = r2[i]  
        _, r3_pred = r3[i]  
        _, r4_pred = r4[i]  
        _, r5_pred = r5[i] 
        _, r6_pred = r6[i]
        _, r7_pred = r7[i]
 
        # 加权求和
        r = (r1_pred * alpha[0] + r2_pred * alpha[1] + r3_pred * alpha[2] + r4_pred * alpha[3] + r5_pred * alpha[4] + r6_pred * alpha[5] + r7_pred * alpha[6])  
        
        r = np.argmax(r)  
        right_num += int(r == int(l))  
        total_num += 1  
   
    # 更新进度条
    pbar.update(1)
    
    # 计算准确率  
    acc = right_num / total_num if total_num > 0 else 0  
    return -acc  # 返回负准确率以进行最小化  

def find_best_alpha(r1, r2, r3, r4, r5, r6, r7, label):  
    """  
    寻找最佳的 alpha 参数组合  
    参数:  
    r1, r2, ..., r8 (np.ndarray): 23个模型的预测结果  
    label (np.ndarray): 真实标签  
    返回:  
    best_alpha (list): 最佳的 alpha 参数组合  
    best_acc (float): 最佳的准确率  
    """  
     # 定义 alpha 参数的离散搜索范围，步长为 1（即 0.01 的精度）
    space = [Integer(20, 120, name=f'alpha_{i}') for i in range(7)]  # 离散的搜索空间，[20, 120] 对应 [0.2, 1.2] 
    
     # 创建进度条对象，设置总的迭代次数
    with tqdm(total=150) as pbar:  # 200 是总的调用次数，根据 n_calls 来设置
        # 执行贝叶斯优化  
        result = gp_minimize(lambda alpha: objective(alpha, r1, r2, r3, r4, r5, r6, r7, label, pbar), 
                              space, 
                              n_calls=150, 
                              random_state=0)
    
    best_alpha = [a / 100.0 for a in result.x]  # 恢复为小数精度
    best_acc = -result.fun  # 取负值以获得最佳准确率 

    return best_alpha, best_acc  

if __name__ == "__main__":  
 
    with open('/root/Six_Streams_CTR_GCN/data/val_label.pkl', 'rb') as f:  
        label = pickle.load(f)  
        
    with open('./weights/ctrgcn_joint/best_score.pkl', 'rb') as r1:
        r1 = list(pickle.load(r1).items())
        
    with open('./weights/ctrgcn_joint_tta/best_score.pkl', 'rb') as r2:
        r2 = list(pickle.load(r2).items())

    with open('./weights/blockgcn_bone/best_score.pkl', 'rb') as r3:
        r3 = list(pickle.load(r3).items())
    
    with open('./weights/cdgcn_bone/best_score.pkl', 'rb') as r4:
        r4 = list(pickle.load(r4).items())
        
    with open('./weights/cdgcn_joint/best_score.pkl', 'rb') as r5:
        r5 = list(pickle.load(r5).items())
        
    with open('./weights/infogcn_head_6/best_score.pkl', 'rb') as r6:
        r6 = list(pickle.load(r6).items())
        
    with open('./weights/infogcn_head_6_frame_128/best_score.pkl', 'rb') as r7:
        r7 = list(pickle.load(r7).items())
    
    # 寻找最佳的 alpha
    best_alpha, best_acc = find_best_alpha(r1, r2, r3, r4, r5, r6, r7, label)  
    print(f"Best alpha: {best_alpha}")  
    print(f"Best accuracy: {best_acc:.5f}")
