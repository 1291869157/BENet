## Introduction
Although deep convolutional networks have achieved good results in the field of salient object detection, most of these methods can not work well near the boundary. This results in poor boundary quality of network predictions, accompanied by a large number of blurred contours and hollow objects. To solve this problem, this paper proposes a Boundary Enhance Network (BENet) for salient object detection, which makes the network pay more attention to salient edge features by fusing auxiliary boundary information of objects. We adopt the Progressive Feature Extraction Module (PFEM) to obtain multi-scale edge and object features of salient objects. In response to the semantic gap problem in feature fusion, we propose an Adaptive Edge Fusion Module (AEFM) to allow the network to adaptively and complementarily fuse edge features and salient object features. The Self Refinement (SR) module further repairs and enhances edge features. Moreover, in order to make the network pay more attention to the boundary, we design an edge enhance loss function, which uses the additional boundary maps to guide the network to learn rich boundary features at the pixel level. Experimental results show that our proposed method outperforms state-of-the-art methods on five benchmark datasets.

## Proposed Method

<div align="center">
  <img src="https://github.com/1291869157/BENet/blob/main/fig11.png">
</div>

In this paper, we propose a novel boundary enhance network. The model contains multiple sub-networks. The Progressive Feature Extraction Module (PFEM) is used to capture the boundary features and salient object features of salient objects at multiple scales. The Edge Enhance Module (EEM) consists of a series of Adaptive Edge Fusion Modules (AEFM) to balance the fusion of edge features and salient object features. To make the network pay more attention to the details of the boundary region, we design a edge enhancement loss to give higher weights near the boundary. 

## Experiment
#### Visual Comparison
<div align="center">
  <img src="https://github.com/1291869157/BENet/blob/main/fig12.png">
</div>
Since the methods of comparison lack sufficient boundary information, other's prediction boundaries are blurred. While our method balances and strengthens the boundary information, which can better identify interest points near the boundary.

#### Quantitative Comparison
<div align="center">
  <img src="https://github.com/1291869157/BENet/blob/main/fig13.jpg" width="60%">
</div>


