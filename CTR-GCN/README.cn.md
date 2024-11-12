# Six-Streams CTR-GCN

该仓库为队伍 **骼固鼎芯** 参加 [2024年第六届全球校园人工智能算法精英大赛 - 基于无人机的人体行为识别](https://www.saikr.com/vse/50186) 初赛提交的参赛代码。

## 数据准备

您可以从比赛网站 [2024年第六届全球校园人工智能算法精英大赛 - 基于无人机的人体行为识别](https://www.saikr.com/vse/50186) 下载所需的数据和处理方法。

在我们的工作中，我们使用 `train` 和 `test_A` 数据集进行模型的训练和测试，而 `test_B` 数据集则用于比赛排名。

我们的工作包含四种模态：关节、骨骼、关节运动和骨骼运动。这些数据集可以从上述网站获取。

## 训练模型

我们提供脚本来训练这六个流：

```
$ sh train_uav_joint.sh
$ sh train_uav_bone.sh
$ sh train_uav_joint_motion.sh
$ sh train_uav_bone_motion.sh
$ sh train_uav_joint_tta.sh
$ sh train_uav_bone_longtail.sh
```

训练日志将保存在 `./work_dir` 目录中。

## 测试模型

我们也提供了脚本来测试这六个流：

```
bash复制代码$ sh test_joint.sh
$ sh test_bone.sh
$ sh test_joint_motion.sh
$ sh test_bone_motion.sh
$ sh test_joint_tta.sh
$ sh test_bone_longtail.sh
```

测试日志同样将保存在 `./work_dir` 目录中。

## 多流集成

我们提供了找到最佳 alpha 参数和集成分数的方法：

```
$ sh ensemble_find_best.sh 
$ python ensemble_score.py
```

## 我们的成果

最佳权重和分数将保存在 `./weights` 目录中。

对于 test_B 数据集的分数，将以 npy 和 pkl 格式存储在 `./scores` 目录中。我们的最终结果 `fused_score.npy` 已提交用于排名。

我们已将work_dir, weights, scores三个文件夹的内容打包上传至Google Drive，请通过下方链接获取：

https://drive.google.com/file/d/1EEOFR_JpSjCZw_2wKhjgIkiOG19sPACd/view?usp=drive_link

## 未来工作

我们期待能够入围全国决赛，并计划探索新模型。请关注我们的后续工作！

## 致谢

该仓库基于 [MS-CTR-GCN](https://github.com/CarefreeSun/MS-CTR-GCN) 和 [ICMEW2024-Track10](https://github.com/liujf69/ICMEW2024-Track10) 的工作。

我们对原作者的贡献表示感谢！