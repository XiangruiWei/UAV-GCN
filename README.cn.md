# UAV-GCN

本仓库实现了我们团队**骼固鼎芯**在[2024第六届全球校园人工智能算法精英大赛-无人机人体行为识别赛道](https://www.saikr.com/vse/50186) **决赛阶段**的解决方案。

我们整合了四个基于GCN的先进模型 - CTRGCN、BlockGCN、CDGCN和InfoGCN，用于基于骨架的动作识别。

## 数据准备与处理

比赛数据集（.npy格式）和处理方法可以从官方比赛网站[2024第六届全球校园人工智能算法精英大赛-无人机人体行为识别赛道](https://www.saikr.com/vse/50186)下载。

要将训练数据处理成.npz格式，请按顺序执行以下脚本：

```bash
python get_raw_skes_data.py
python get_raw_denoise_data.py
python seq_transformation.py
```

如需处理测试集，只需在这些脚本中相应修改数据路径即可。

**重要说明：**

- CTRGCN、BlockGCN和CDGCN使用**npy**格式数据
- InfoGCN需要使用**npz**格式数据

## 训练与测试

每个模型的详细训练说明都在其各自的文件夹中提供。使用以下命令导航到特定模型目录：

```bash
$ cd CTR-GCN
$ cd BlockGCN
$ cd CD-GCN
$ cd InfoGCN
```

训练和测试日志存储在`./<model_name>/work_dir`目录中。由于大小限制，我们已将完整的`work_dir`上传到Google Drive。

## Alpha参数优化

`weights`目录包含了我们确定分数融合最优alpha参数的方法。

## 分数融合

执行分数融合：

```bash
$ cd scores
$ python ensemble_score.py
```

## 日志

由于空间限制，我们的完整`work_dir`目录已上传至[Google Drive](https://drive.google.com/file/d/1kOp1rP-w5lSjIP0SGOr0kPcHLvQClG1s/view?usp=drive_link)。

## 致谢

本工作基于以下优秀的代码仓库：

- [CTR-GCN](https://github.com/Uason-Chen/CTR-GCN)
- [BlockGCN](https://github.com/ZhouYuxuanYX/BlockGCN)
- [CD-GCN](https://github.com/sakura1040576710/CD-GCN)
- [InfoGCN](https://github.com/stnoah1/infogcn)

我们同时也从以下工作中获得启发：

- [MS-CTR-GCN](https://github.com/CarefreeSun/MS-CTR-GCN)
- [ICMEW2024-Track10](https://github.com/liujf69/ICMEW2024-Track10)
- [UAV-SAR](https://github.com/happylinze/UAV-SAR)

在此向所有原作者的宝贵贡献表示衷心的感谢！

## 语言选项

[Switch to English](README.md)