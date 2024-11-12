# Six-Streams CTR-GCN

This repository implements the method developed by our team **骼固鼎芯** for the [2024 Sixth Global Campus Artificial Intelligence Algorithm Elite Competition - Drone-Based Human Activity Recognition](https://www.saikr.com/vse/50186).

## Data Preparation

You can download the necessary data and processing methods from the competition website [2024 Sixth Global Campus Artificial Intelligence Algorithm Elite Competition - Drone-Based Human Activity Recognition](https://www.saikr.com/vse/50186).

For our approach, we utilize the `train` and `test_A` datasets for training and model testing, while the `test_B` dataset is used for competition ranking.

In our work, we incorporate four modalities: joint, bone, joint motion, and bone motion. These datasets can be obtained from the aforementioned website.

## Training the Model

We provide scripts for convenient training of the six streams:

```bash
$ sh train_uav_joint.sh
$ sh train_uav_bone.sh
$ sh train_uav_joint_motion.sh
$ sh train_uav_bone_motion.sh
$ sh train_uav_joint_tta.sh
$ sh train_uav_bone_longtail.sh
```

Training logs will be saved in the `./work_dir` directory.

## Testing the Model

Testing scripts for the six streams are also provided for convenience:

```bash
$ sh test_joint.sh
$ sh test_bone.sh
$ sh test_joint_motion.sh
$ sh test_bone_motion.sh
$ sh test_joint_tta.sh
$ sh test_bone_longtail.sh
```

Testing logs will likewise be saved in the `./work_dir` directory.

## Multi-Stream Ensemble

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

## Future Work

We anticipate participating in the national finals soon, where we plan to explore new models. Stay tuned for our future endeavors!

## Acknowledgements

This repository is based on the work from [MS-CTR-GCN](https://github.com/CarefreeSun/MS-CTR-GCN) and [ICMEW2024-Track10](https://github.com/liujf69/ICMEW2024-Track10). 

We express our gratitude to the original authors for their contributions!

## Language Options

[Switch to 中文版](README.cn.md)
