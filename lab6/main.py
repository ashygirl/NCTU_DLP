import os
import torch
from torch.utils.data import DataLoader

from datahelper import CLEVRDataset
from model import Generator,Discriminator
from train import train


device=torch.device('cuda' if torch.cuda.is_available() else 'cpu')
z_dim=100
c_dim=24
image_shape=(64,64,3)
epochs=100
lr=0.0002
batch_size=64
test_path=os.path.join('dataset','test.json')


if __name__=='__main__':

    # load training data
    dataset_train=CLEVRDataset(img_path='iclevr',json_path=os.path.join('dataset','train.json'))
    loader_train=DataLoader(dataset_train,batch_size=batch_size,shuffle=True,num_workers=2)

    # create generate & discriminator
    generator=Generator(z_dim,c_dim).to(device)
    discrimiator=Discriminator(image_shape,c_dim).to(device)


    # train
    train(loader_train,generator,discrimiator,z_dim,c_dim,epochs,lr,test_path)

