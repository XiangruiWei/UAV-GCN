# UAV-GCN

This repository implements our team **骼固鼎芯**'s solution for the [2024 Sixth Global Campus Artificial Intelligence Algorithm Elite Competition - Drone-Based Human Activity Recognition](https://www.saikr.com/vse/50186) **Final Phase**.

We integrate four state-of-the-art GCN-based models - CTRGCN, BlockGCN, CDGCN, and InfoGCN - for skeleton-based action recognition.

## Data Preparation & Processing

The competition dataset (in .npy format) and processing methods can be downloaded from the official competition website [2024 Sixth Global Campus Artificial Intelligence Algorithm Elite Competition - Drone-Based Human Activity Recognition](https://www.saikr.com/vse/50186).

To process the training data into .npz format, execute the following scripts sequentially:

```bash
python get_raw_skes_data.py
python get_raw_denoise_data.py
python seq_transformation.py
```

For processing the test set, simply modify the data paths in these scripts accordingly.

**Important Notes:**
- CTRGCN, BlockGCN and CDGCN use the **npy** format data
- InfoGCN requires the **npz** format data

## Training & Testing

Detailed training instructions for each model are provided in their respective folders. Navigate to specific model directories using:

```bash
$ cd CTR-GCN
$ cd BlockGCN
$ cd CD-GCN
$ cd InfoGCN
```

Training and testing logs are stored in `./<model_name>/work_dir` directories. Due to size constraints, we have uploaded our complete `work_dir` to Google Drive.

## Alpha Parameter Optimization

The `weights` directory contains our methodology for determining optimal alpha parameters for score fusion.

## Score Fusion

To perform score ensemble:

```bash
$ cd scores
$ python ensemble_score.py
```

## Logs

Our complete `work_dir` directory is available on [Google Drive](https://drive.google.com/file/d/1kOp1rP-w5lSjIP0SGOr0kPcHLvQClG1s/view?usp=drive_link) due to size limitations.

## Acknowledgements

This work builds upon several excellent repositories:
- [CTR-GCN](https://github.com/Uason-Chen/CTR-GCN)
- [BlockGCN](https://github.com/ZhouYuxuanYX/BlockGCN)
- [CD-GCN](https://github.com/sakura1040576710/CD-GCN)
- [InfoGCN](https://github.com/stnoah1/infogcn)

We also drew inspiration from:
- [MS-CTR-GCN](https://github.com/CarefreeSun/MS-CTR-GCN)
- [ICMEW2024-Track10](https://github.com/liujf69/ICMEW2024-Track10)
- [UAV-SAR](https://github.com/happylinze/UAV-SAR)

We extend our sincere gratitude to all the original authors for their valuable contributions!

## Language Options

[切换至中文版](README.cn.md)

