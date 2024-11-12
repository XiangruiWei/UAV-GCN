# Scores

The scores we use to fuse are saved in this directory, here we list them below:

| model_modality     | val_accuracy |
| :----------------- | ------------ |
| ctrgcn_joint       | 43.90        |
| ctrgcn_joint_tta   | 44.45        |
| blockgcn_bone      | 44.55        |
| cdgcn_joint        | 43.85        |
| cdgcn_bone         | 44.25        |
| infogcn_k_6        | 43.90        |
| infogcn_128Frame_6 | 43.80        |

We provide the code to fuse the score:

```shell
python ensemble_score.py
```

The result will be saved as pred.npy
