_base_ = [
    'faster_rcnn_r50_caffe_c4.py',
    'default_runtime.py'
]
model = dict(roi_head=dict(bbox_head=dict(num_classes=1)))

# dataset settings
CLASSES = ('flower',)
dataset_type = 'VOCDataset'
data_root = 'D:/Olive Flowering PicturesVOC2012/'
img_norm_cfg = dict(
    mean=[103.530, 116.280, 123.675], std=[1.0, 1.0, 1.0], to_rgb=False)
train_pipeline = [
    dict(type='LoadImageFromFile'),
    dict(type='LoadAnnotations', with_bbox=True),
    dict(
        type='RandomCrop',
        crop_size=(600,600),
        allow_negative_crop=True),
    dict(type='RandomFlip', flip_ratio=0.5),
    dict(type='Normalize', **img_norm_cfg),
    dict(type='Pad', size_divisor=32),
    dict(type='DefaultFormatBundle'),
    dict(type='Collect', keys=['img', 'gt_bboxes', 'gt_labels']),
]
test_pipeline = [
    dict(type='LoadImageFromFile'),
    dict(
        type='MultiScaleFlipAug',
        scale_factor=1.0,
        flip=False,
        transforms=[
            dict(type='Resize', keep_ratio=True),
            dict(type='RandomFlip'),
            dict(type='Normalize', **img_norm_cfg),
            dict(type='Pad', size_divisor=32),
            dict(type='ImageToTensor', keys=['img']),
            dict(type='Collect', keys=['img']),
        ])
]
data = dict(
    samples_per_gpu=2,
    workers_per_gpu=2,
    train=dict(
        type=dataset_type,
        ann_file=[
            data_root + 'train.txt'
        ],
        img_prefix=[data_root],
        classes = CLASSES,
        pipeline=train_pipeline),
    val=dict(
        type=dataset_type,
        ann_file=data_root + 'val.txt',
        img_prefix=data_root,
        classes = CLASSES,
        pipeline=test_pipeline),
    test=dict(
        type=dataset_type,
        ann_file=data_root  + 'test.txt',
        img_prefix=data_root,
        classes = CLASSES,
        pipeline=test_pipeline))

# optimizer
optimizer = dict(type='SGD', lr=0.02, momentum=0.9, weight_decay=0.0001)
optimizer_config = dict(grad_clip=None)

# learning policy
lr_config = dict(
    policy='step',
    warmup='linear',
    warmup_iters=100,
    warmup_ratio=0.001,
    step=[12000, 16000])

# Runner type
runner = dict(type='IterBasedRunner', max_iters=5000)

checkpoint_config = dict(interval=400)
evaluation = dict(interval=100, metric='mAP')
