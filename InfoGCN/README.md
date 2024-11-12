# InfoGCN

In this directory, we will demonstrate how do we train and test the model

## Training the Model

We provide scripts for convenient training:

```bash
# FR_Head
$ sh train_head_1.sh
$ sh train_head_2.sh
$ sh train_head_6.sh

# 32 Frames
$ sh train_head_1_frame_32.sh
$ sh train_head_2_frame_32.sh
$ sh train_head_6_frame_32.sh

# 128 Frames
$ sh train_head_1_frame_128.sh
$ sh train_head_2_frame_128.sh
$ sh train_head_6_frame_128.sh
```

Training logs will be saved in the `./work_dir` directory.

## Testing the Model

Testing scripts are also provided for convenience:

```bash
# FR_Head
$ sh test_head_1.sh
$ sh test_head_2.sh
$ sh test_head_6.sh

# 32 Frames
$ sh test_head_1_frame_32.sh
$ sh test_head_2_frame_32.sh
$ sh test_head_6_frame_32.sh

# 128 Frames
$ sh test_head_1_frame_128.sh
$ sh test_head_2_frame_128.sh
$ sh test_head_6_frame_128.sh
```

However, we did not use all the training models, so some testing scripts is missing. Following scripts is commonly used for testing:

```bash
python main.py --config <config path> --work-dir <work-dir path> --phase test --save_score True --weights <weights path>
```

Testing logs will likewise be saved in the `./work_dir` directory.

## Logs

To save space, we upload our ``work_dir``  directory in the [Google Drive](https://drive.google.com/file/d/1kOp1rP-w5lSjIP0SGOr0kPcHLvQClG1s/view?usp=drive_link).
