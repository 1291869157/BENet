## Introduction
Although deep convolutional networks have achieved good results in the field of salient object detection, most of these methods can not work well near the boundary. This results in poor boundary quality of network predictions, accompanied by a large number of blurred contours and hollow objects. To solve this problem, this paper proposes a Boundary Enhance Network (BENet) for salient object detection, which makes the network pay more attention to salient edge features by fusing auxiliary boundary information of objects. We adopt the Progressive Feature Extraction Module (PFEM) to obtain multi-scale edge and object features of salient objects. In response to the semantic gap problem in feature fusion, we propose an Adaptive Edge Fusion Module (AEFM) to allow the network to adaptively and complementarily fuse edge features and salient object features. The Self Refinement (SR) module further repairs and enhances edge features. Moreover, in order to make the network pay more attention to the boundary, we design an edge enhance loss function, which uses the additional boundary maps to guide the network to learn rich boundary features at the pixel level. Experimental results show that our proposed method outperforms state-of-the-art methods on five benchmark datasets.

## Proposed Method

<div align="center">
  <img src="https://github.com/1291869157/BENet/blob/main/fig11.png" width="90%">
</div>

In this paper, we propose a novel boundary enhance network. The model contains multiple sub-networks. The Progressive Feature Extraction Module (PFEM) is used to capture the boundary features and salient object features of salient objects at multiple scales. The Edge Enhance Module (EEM) consists of a series of Adaptive Edge Fusion Modules (AEFM) to balance the fusion of edge features and salient object features. To make the network pay more attention to the details of the boundary region, we design a edge enhancement loss to give higher weights near the boundary. 

## Experiment
#### Visual Comparison
<div align="center">
  <img src="https://github.com/1291869157/BENet/blob/main/fig12.png" width="80%">
</div>
Since the methods of comparison lack sufficient boundary information, other's prediction boundaries are blurred. While our method balances and strengthens the boundary information, which can better identify interest points near the boundary.

#### Quantitative Comparison
<div align="center">
  <img src="https://github.com/1291869157/BENet/blob/main/fig13.jpg" width="60%">
</div>
We qualitatively compare the methods from the two metrics. As shown in table, we can see that our BENet model achieves the best metrics on most datasets, which shows that our model is effective and robust.

## References
1. Zhao, J.X., Liu, J.J., Fan, D.P., et al.: EGNet: edge guidance network for salient object detection. In: Proceedings of the IEEE/CVF International Conference on Computer Vision, pp. 8779–8788 (2019)
2. Qin, X., Zhang, Z., Huang, C., et al.: Basnet: boundary-aware salient object detection. In: Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition, pp. 7479–7489 (2019)
3. Li, X., Yang, F., Cheng, H., et al.: Contour knowledge transfer for salient object detection. In: Proceedings of the European Conference on Computer Vision (ECCV), pp. 355–370 (2018)
4. Canny, J.: A computational approach to edge detection. IEEE Trans. Pattern Anal. Mach. Intell. 6, 679–698 (1986)
5. Ronneberger, O., Fischer, P., Brox, T.: U-net: convolutional networks for biomedical image segmentation. In: Navab, N., Hornegger, J., Wells, W.M., Frangi, A.F. (eds.) MICCAI 2015. LNCS, vol. 9351, pp. 234–241. Springer, Cham (2015).
6. Zhao, T., Wu, X.: Pyramid feature attention network for saliency detection. In: Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition, pp. 3085–3094 (2019)
7. Wang, W., Zhao, S., Shen, J., et al.: Salient object detection with pyramid attention and salient edges. In: Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition, pp. 1448–1457 (2019)
8. Hou, Q., Cheng, M.M., Hu, X., et al.: Deeply supervised salient object detection with short connections. In: Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition, pp. 3203–3212 (2017)
9. Zhao, R., Ouyang, W., Li, H., et al.: Saliency detection by multi-context deep learning. In: Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition, pp. 1265–1274 (2015)
10. Long, J., Shelhamer, E., Darrell, T.: Fully convolutional networks for semantic segmentation. In: Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition, pp. 3431–3440 (2015)
11. Lee, G., Tai, Y.W., Kim, J.: Deep saliency with encoded low level distance map and high level features. In: Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition, pp. 660–668 (2016)
12. Chen, Z., Xu, Q., Cong, R., et al.: Global context-aware progressive aggregation network for salient object detection. In: Proceedings of the AAAI Conference on Artificial Intelligence, vol. 34, no. 07, pp. 10599–10606 (2020)
13. Liu, J.J., Hou, Q., Cheng, M.M., et al.: A simple pooling-based design for real-time salient object detection. In: Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition, pp. 3917–3926 (2019)
14. Zhou, L., Gu, X.: Embedding topological features into convolutional neural network salient object detection. Neural Netw. 121, 308–318 (2020)
15. Wu, Z., Su, L., Huang, Q.: Cascaded partial decoder for fast and accurate salient object detection. In: Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition, pp. 3907–3916 (2019)
16. Wei, J., Wang, S., Huang, Q.: F3Net: fusion, feedback and focus for salient object detection. In: Proceedings of the AAAI Conference on Artificial Intelligence, vol. 34, no. 07, pp. 12321–12328 (2020)
17. Li, J., Su, J., Xia, C., et al.: Salient object detection with purificatory mechanism and structural similarity loss. IEEE Trans. Image Process. 30, 6855–6868 (2021)
18. Deng, Z., Hu, X., Zhu, L., et al.: R3net: recurrent residual refinement network for saliency detection. In: Proceedings of the 27th International Joint Conference on Artificial Intelligence, Menlo Park, CA, USA, AAAI Press, pp. 684–690 (2018)
19. Zhang, P., Wang, D., Lu, H., et al.: Amulet: aggregating multi-level convolutional features for salient object detection. In: Proceedings of the IEEE International Conference on Computer Vision, pp. 202–211 (2017)
20. Liu, N., Han, J., Yang, M.H.: Picanet: learning pixel-wise contextual attention for saliency detection. In: Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition, pp. 3089–3098 (2018)
21. Zhao, X., Pang, Y., Zhang, L., Lu, H., Zhang, L.: Suppress and balance: a simple gated network for salient object detection. In: Vedaldi, A., Bischof, H., Brox, T., Frahm, J.-M. (eds.) ECCV 2020. LNCS, vol. 12347, pp. 35–51. Springer, Cham (2020)
22. Mohammadi, S., Noori, M., Bahri, A., et al.: CAGNet: content-aware guidance for salient object detection. Pattern Recogn. 103, 107303 (2020)
23. Liu, Y., Zhang, Q., Zhang, D., et al.: Employing deep part-object relationships for salient object detection. In: Proceedings of the IEEE/CVF International Conference on Computer Vision, pp. 1232–1241 (2019)

