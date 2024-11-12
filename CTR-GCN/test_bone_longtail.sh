# CUDA_VISIBLE_DEVICES=0 python main.py 
# --config ./config/uav/test_joint.yaml 
# --phase test 

# CUDA_VISIBLE_DEVICES=0 python main.py --config ./config/uav/test_joint.yaml --phase test --save-score True

#!/bin/bash

# 测试阶段设置为 'test'
PHASE="test"

# 工作目录
WORK_DIR="./work_dir/test_bone_longtail"

# 模型保存名称（可自定义）
# MODEL_SAVED_NAME="joint_model"

# 配置文件路径
CONFIG="./config/uav/test_bone_longtail.yaml"

# 随机种子
SEED=1

# 打印日志
PRINT_LOG=True

# 测试批次大小
TEST_BATCH_SIZE=256

# 使用的模型
MODEL="model.ctrgcn.Model"  # 自定义模型名称

# 设备，使用CPU还是GPU
DEVICE=0  # 如果使用GPU则设置为对应的GPU ID

# 加载的权重
WEIGHTS="./weights/bone_longtail/runs-61-15616.pt"  # 指定预训练模型的权重文件路径

# 输出结果的Top K
SHOW_TOPK="1 5"

# 开始运行测试命令
python main.py \
  --phase $PHASE \
  --work-dir $WORK_DIR \
  --config $CONFIG \
  --seed $SEED \
  --print-log $PRINT_LOG \
  --test-batch-size $TEST_BATCH_SIZE \
  --model $MODEL \
  --device $DEVICE \
  --weights $WEIGHTS \
  --show-topk $SHOW_TOPK
