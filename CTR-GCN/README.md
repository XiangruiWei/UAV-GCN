# CTR-GCN

In this directory, we will demonstrate how do we train and test the model

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

## Logs

To save space, we upload our ``work_dir``  directory in the [Google Drive](https://drive.google.com/file/d/1kOp1rP-w5lSjIP0SGOr0kPcHLvQClG1s/view?usp=drive_link).
