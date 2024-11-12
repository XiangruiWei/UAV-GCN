# UAV-GCN

This repository implements the method developed by our team **骼固鼎芯** for the [2024 Sixth Global Campus Artificial Intelligence Algorithm Elite Competition - Drone-Based Human Activity Recognition](https://www.saikr.com/vse/50186) --- **Final phase**.

In this repository, we utilize CTRGCN, BlockGCN, CDGCN, InfoGCN, these four GCN-based models to recognize actions according to skeletons. 

## Data Preparation & Procession

You can download the npy format data and processing methods from the competition website [2024 Sixth Global Campus Artificial Intelligence Algorithm Elite Competition - Drone-Based Human Activity Recognition](https://www.saikr.com/vse/50186).







**!!!** CTRGCN，BlockGCN and CDGCN are trained and tested by the **npy** format data; 

**!!!** InfoGCN is trained and tested by the **npz** format data.

## Training & Testing

The details about training these models are demonstrated in the corresponding model folder. You can use following commands to turn to the corresponding model and check details:
```shell
$ cd CTR-GCN
$ cd BlockGCN
$ cd CD-GCN
$ cd InfoGCN
```

Our records about training and testing models are saved in the ``./<model_name>/work_dir`` directories. Due to the space limitation, we upload our ``work_dir`` in the Google Drive

## Score Fusion

We offer methods to find optimal alpha parameters and to ensemble scores:

```bash
$ sh ensemble_find_best.sh 
$ python ensemble_score.py
```

## Logs

To save space, we upload our ``work_dir``  directory in the [Google Drive](https://drive.google.com/file/d/1kOp1rP-w5lSjIP0SGOr0kPcHLvQClG1s/view?usp=drive_link).

## Acknowledgements

This repository is based on the work from [CTR-GCN](https://github.com/Uason-Chen/CTR-GCN), [BlockGCN](https://github.com/ZhouYuxuanYX/BlockGCN), [CD-GCN](https://github.com/sakura1040576710/CD-GCN), [InfoGCN](https://github.com/stnoah1/infogcn).

We also learn the training and alpha searching method from [MS-CTR-GCN](https://github.com/CarefreeSun/MS-CTR-GCN), [ICMEW2024-Track10](https://github.com/liujf69/ICMEW2024-Track10) and [UAV-SAR](https://github.com/happylinze/UAV-SAR). 

We express our gratitude to the original authors for their contributions!

## Language Options

[Switch to 中文版](README.cn.md)
