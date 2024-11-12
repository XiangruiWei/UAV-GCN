# UAV-GCN

This repository implements the method developed by our team **骼固鼎芯** for the [2024 Sixth Global Campus Artificial Intelligence Algorithm Elite Competition - Drone-Based Human Activity Recognition](https://www.saikr.com/vse/50186) --- **Final phase**.

In this repository, we utilize CTRGCN, BlockGCN, CDGCN, these three GCN models to recogonize actions according to skeletons. 

## Data Preparation & Procession

You can download the npy format data and processing methods from the competition website [2024 Sixth Global Campus Artificial Intelligence Algorithm Elite Competition - Drone-Based Human Activity Recognition](https://www.saikr.com/vse/50186).







!!! CTRGCN，BlockGCN and CDGCN are trained and tested by the **npy** format data; 

​    InfoGCN is trained and tested by the **npz** format data

## Training & Testing

The details about training these models are demonstrated in the model folder. You can use following commands to turn to the corresponding model and check details:
```shell
$ cd CTR-GCN
$ cd BlockGCN
$ cd CD-GCN
$ cd InfoGCN
```

Our records about training and testing models are saved in the ``./<model_name>/work_dir`` directories. Due to the space limitation, we upload our ``work_dir`` in the Google Drive

## Scores Fusion

We offer methods to find optimal alpha parameters and to ensemble scores:

```bash
$ sh ensemble_find_best.sh 
$ python ensemble_score.py
```

## Our Results

The best weights and scores (in pkl format) for all streams are saved in the `./weights` directory. 

Scores for the test_B dataset are stored in both npy and pkl formats in the `./scores` directory. Our final result, `fused_score.npy`, is submitted for ranking.

## Where to get details

To save space, we upload our ``work_dir``, ``weights`` and ``scores`` directories in the Google Drive.

https://drive.google.com/file/d/1EEOFR_JpSjCZw_2wKhjgIkiOG19sPACd/view?usp=drive_link

## Acknowledgements

This repository is based on the work from [MS-CTR-GCN](https://github.com/CarefreeSun/MS-CTR-GCN) and [ICMEW2024-Track10](https://github.com/liujf69/ICMEW2024-Track10). 

We express our gratitude to the original authors for their contributions!

## Language Options

[Switch to 中文版](README.cn.md)
