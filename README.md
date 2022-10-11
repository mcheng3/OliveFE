# OliveFE


## Requirements
Download **Anaconda** [here](https://www.anaconda.com/)

```
$ python OliveFE.py <config .py file> <model .pth file> <images directory>
```
Olive FE requires the following dependencies:
```
$ conda install -c anaconda tk 
$ conda install -c conda-forge matplotlib 
$ conda install -c esri mmcv-full 
$ conda install -c pytorch torchvision 
$ conda install pandas
```
OliveFE also requires mmdetection: [installation instructions](https://github.com/open-mmlab/mmdetection/blob/master/docs/en/get_started.md/#Installation).

## How to use


To run OliveFE GUI, run the following command: 
```
$ python OliveFE.py <config .py file> <model .pth file> <images directory>
```
If your computer does not have a CUDA GPU available, use this command instead:
```
$ python OliveFE.py --device cpu <config .py file> <model .pth file> <images directory>
```

Example with arguments
```
$ python OliveFE.py configs/faster_rcnn.py /latest.pth dataVOC2012/test_images
```
