import numpy as np
import torch.nn.functional as F
from PIL import Image
import matplotlib.pyplot as plt
from gaussian_2d import *
import torch

from model import *

net_bone=build_model('vgg')

pre_model=torch.load('./pretrained_model/epoch_vgg.pth',map_location=torch.device('cpu'))
net_bone.load_state_dict(pre_model)
for k,v in net_bone.named_parameters():
    print(k,v.size())
for i in net_bone.base.parameters():
    i.requires_grad = False
for j in net_bone.merge1.parameters():
    j.requires_grad = False


for name, param in net_bone.named_parameters():
    if param.requires_grad:
        print("requires_grad: True ", name)
    else:
        print("requires_grad: False ", name)


# net=build_model('resnet')
# for name, parameters in net.named_parameters():
#     print(name, ':', parameters.size())


# sal_img='./eg/imgs/ILSVRC2012_test_00000025.png'
# edge_img='./eg/edge_img/ILSVRC2012_test_00000025.png'
# pre_img='./eg/pre_img/ILSVRC2012_test_00000025.png'
# sal=np.array(Image.open(sal_img)) / 255
# edge=np.array(Image.open(edge_img))[:,:,0] / 255
# pre=np.array(Image.open(pre_img)) / 255
# plt.imshow(sal)
# plt.colorbar()
# plt.show()
# plt.imshow(edge)
# plt.colorbar()
# plt.show()


# gauss_kernel = gauss(3, 2)

# wbce=F.binary_cross_entropy_with_logits(torch.tensor(pre),torch.tensor(sal),reduction='none')
# ed_weight=conv_2d(gauss_kernel,edge)+0.5
# a=torch.tensor([[1,2,3],[1,2,3],[1,2,3]],dtype=torch.float)
# b=torch.tensor([[0,1,1],[1,0,1],[1,0,0]],dtype=torch.float)
# ed_weight=conv_2d(gauss_kernel,b)
# wbc=(F.binary_cross_entropy_with_logits(a,b,reduction='none')*(ed_weight+0.5)).sum(axis=[0,1])
# m=torch.tensor([[1,0,0],[0,0,0],[0,0,1]])
# hh=wbc*(ed_weight + 0.5)
# m=hh.sum(axis=[0,1])
# h=F.binary_cross_entropy_with_logits(a,b,reduction='sum')

# print(a[-1])
# print(1)


# fl_py = conv_2d(gauss_kernel, edge)
# fl_py1=fl_py + 0.5
# plt.imshow(fl_py)
# plt.colorbar()
# plt.show()