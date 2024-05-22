## BENet (MMM2023)
BENet: Boundary Enhance Network for Salient Object Detection

## Trained Model
Please download the trained model and put it in "pretrained_model":

Link: https://pan.baidu.com/s/19_AijbRIuKAV6dSnEB_zNw,  &nbsp;  code: grap 

Please download the initial model and put it in "initial_model":

Link: https://pan.baidu.com/s/17mzR8tkZnX5--zuUJFkT9A, &nbsp;  code: 4y4q  

## Introduction
Although deep convolutional networks have achieved good results in the field of salient object detection, most of these methods can not work well near the boundary. This results in poor boundary quality of network predictions, accompanied by a large number of blurred contours and hollow objects. To solve this problem, this paper proposes a Boundary Enhance Network (BENet) for salient object detection, which makes the network pay more attention to salient edge features by fusing auxiliary boundary information of objects. We adopt the Progressive Feature Extraction Module (PFEM) to obtain multi-scale edge and object features of salient objects. In response to the semantic gap problem in feature fusion, we propose an Adaptive Edge Fusion Module (AEFM) to allow the network to adaptively and complementarily fuse edge features and salient object features. The Self Refinement (SR) module further repairs and enhances edge features. Moreover, in order to make the network pay more attention to the boundary, we design an edge enhance loss function, which uses the additional boundary maps to guide the network to learn rich boundary features at the pixel level. Experimental results show that our proposed method outperforms state-of-the-art methods on five benchmark datasets.

## Proposed Method

<div align="center">
  <img src="https://github.com/1291869157/BENet/blob/main/fig11.png" width="90%">
</div>

In this paper, we propose a novel boundary enhance network. The model contains multiple sub-networks. The Progressive Feature Extraction Module (PFEM) is used to capture the boundary features and salient object features of salient objects at multiple scales. The Edge Enhance Module (EEM) consists of a series of Adaptive Edge Fusion Modules (AEFM) to balance the fusion of edge features and salient object features. To make the network pay more attention to the details of the boundary region, we design a edge enhancement loss to give higher weights near the boundary. 

## Experiment
### Visual Comparison
<div align="center">
  <img src="https://github.com/1291869157/BENet/blob/main/fig12.png" width="80%">
</div>
Since the methods of comparison lack sufficient boundary information, other's prediction boundaries are blurred. While our method balances and strengthens the boundary information, which can better identify interest points near the boundary.

### Quantitative Comparison
<div align="center">
  <img src="https://github.com/1291869157/BENet/blob/main/fig13.jpg" width="60%">
</div>
We qualitatively compare the methods from the two metrics. As shown in table, we can see that our BENet model achieves the best metrics on most datasets, which shows that our model is effective and robust.
<br>
<br>

We provide saliency maps of our model on five benchmark saliency dataset (DUT, DUTS, ECSSD, HKU-IS, PASCAL-S) as below:
Link: https://pan.baidu.com/s/1pd-C1prTDrv1asw5M0LpBg, &nbsp;   code: vc87 

## Our Bib:
Please cite our paper if necessary:
```
@inproceedings{yan2023benet,
  title={BENet: Boundary Enhance Network for Salient Object Detection},
  author={Yan, Zhiqi and Liang, Shuang},
  booktitle={International Conference on Multimedia Modeling},
  pages={228--239},
  year={2023},
  organization={Springer}
}
```

## Contact
Please drop me an email for further problems or discussion: 1291869157@qq.com

