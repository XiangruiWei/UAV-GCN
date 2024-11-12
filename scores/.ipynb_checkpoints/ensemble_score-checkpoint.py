import numpy as np

score1 = np.load('ctrgcn_joint_score.npy')
score2 = np.load('ctrgcn_joint_tta_score.npy')

score3 = np.load('blockgcn_bone_score.npy')

score4 = np.load('cdgcn_bone_score.npy')
score5 = np.load('cdgcn_joint_score.npy')

score6 = np.load('infogcn_head_6_score.npy')
score7 = np.load('infogcn_head_6_frame_128_score.npy')



# 定义权重
weights = [0.49, 0.5, 0.4, 0.98, 0.46, 0.2, 0.99]

# 计算加权平均
fused_score = np.zeros_like(score1)

for i in range(score1.shape[0]):
    for j in range(score1.shape[1]):
        fused_score[i, j] = (  
        score1[i, j] * weights[0] +  
        score2[i, j] * weights[1] +  
        score3[i, j] * weights[2] +  
        score4[i, j] * weights[3] +  
        score5[i, j] * weights[4] +  
        score6[i, j] * weights[5] +
        score7[i, j] * weights[6]) / sum(weights)

# 保存融合后的结果
np.save('fused_score_final.npy', fused_score)
print('Fusion complete. Saved to fused_score.npy')
