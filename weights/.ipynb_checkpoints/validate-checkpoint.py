import pickle
import numpy as np

# 加载pkl文件
with open('val_label.pkl', 'rb') as f:
    val_label = pickle.load(f)

with open('mixformer_2/best_score.pkl', 'rb') as f:
    best_score = pickle.load(f)

# 初始化正确预测的计数
correct_predictions = 0

# 遍历每个样本，获取预测的类别并与实际标签比较
for i, (sample_id, scores) in enumerate(best_score.items()):
    # 获取模型预测的类别（Top-1预测）
    predicted_label = np.argmax(scores)
    
    # 获取实际标签
    actual_label = val_label[i]
    
    # 比较预测和实际标签
    if predicted_label == actual_label:
        correct_predictions += 1

# 计算Top-1准确率
top1_accuracy = correct_predictions / len(val_label)

print(f'Top-1 Accuracy: {top1_accuracy * 100:.2f}%')
