import numpy as np 
import matplotlib.pyplot as plt 
import numpy as np
from scipy.linalg import toeplitz 
import pdb

import torch
import torch.utils.data
from torch import nn, optim
from torch.nn import functional as F
from torchvision import datasets, transforms
from torchvision.utils import save_image


def sample_mean(data2D):
    mean_2d = np.mean(data2D, axis=2)    
    return mean_2d

def sample_variance(data2D):
    sample_variance_2d =  np.std(data2D, ddof=0, axis=2)**2   
    return sample_variance_2d

def update_b(data2D):
    mean_2d = np.mean(data2D, axis=2)
    b = np.mean(np.abs(data2D - mean_2d.reshape(28,28,1)), axis=2) 
    return b


def LassoEstimator(y, A, sigma_v, lambda_gamm, mu_gamma): 

    dff = sigma_v/(2*lambda_gamm  )
 
    X   = (y.transpose().dot(A)).transpose()

    x_return = np.zeros_like(X) 
    value_a = X - dff   

    case_a  = (value_a > mu_gamma) *(value_a > 0 )
    x_return[case_a] = value_a[case_a]
 
    value_b = X + dff  
    case_b  = (value_b < mu_gamma ) *(value_b > 0 )
    x_return[case_b] = value_b[case_b]
     
    return x_return

def loopy_LassoEstimation(y, A, sigma_v, lambda_gamm, mu_gamma, num_iteration):
    mu_gamma_updated    = mu_gamma
    lambda_gamm_updated = lambda_gamm
    Num_samples = y.shape[1]
    x_return_list = [] 
    for i in range(num_iteration):
        x_return = LassoEstimator(y, A, sigma_v, lambda_gamm_updated, mu_gamma_updated)  
        data2D_update       = x_return.reshape(28,28, Num_samples) 
        mu_gamma_updated    = sample_mean(data2D_update) 
        mu_gamma_updated    = mu_gamma_updated.reshape(28*28,1)

        lambda_gamm_updated = update_b(data2D_update) 
        lambda_gamm_updated = lambda_gamm_updated.reshape(28*28,1)
        x_return_list.append(x_return)
  
        
    return x_return_list


if __name__ == "__main__":
 

    test_loader = torch.utils.data.DataLoader(
        datasets.MNIST('../data', train=False, download=True,
                    transform=transforms.ToTensor()), batch_size=1, shuffle=False)

    data_vect = []
    label_vect_ = []
    for i, (data, label) in enumerate(test_loader):
        data_vect.append(data.view(28,28).numpy())
        label_vect_.append(label.numpy()[0])

    label_vect  = np.array(label_vect_)
    data2D      = np.stack(data_vect, axis=-1)
    Num_samples = data2D.shape[2]
    
    
    mu_gamma_    = sample_mean(data2D)
    mu_gamma    =  mu_gamma_.reshape(28*28,1)

    sample_variance_ = update_b(data2D) #sample_variance(data2D)
    lambda_gamm      = sample_variance_.reshape(28*28,1)
 

    sigma_v           = 1e-10
    num_iteration     = 5
    compression_ratio = 0.5

    n_compressed_data = int(compression_ratio*28*28) 
    A                 = np.random.randn(n_compressed_data, 28*28)/np.sqrt(n_compressed_data)  
    v                 = sigma_v*np.random.randn(1, 1)  
    yA                = A.dot(data2D.reshape(28*28,-1)).reshape(n_compressed_data,-1)  

    y                 = yA  + v 

    x_hat_list        = loopy_LassoEstimation(y, A,  0.01, lambda_gamm, mu_gamma, num_iteration)    
    
    Num_samples       = y.shape[1]

    x_hat_2D_6    = x_hat_list[-5].reshape(28,28, Num_samples)[:,:,0]    
    x_hat_2D_7    = x_hat_list[-4].reshape(28,28, Num_samples)[:,:,0]    
    x_hat_2D_8    = x_hat_list[-3].reshape(28,28, Num_samples)[:,:,0]    
    x_hat_2D_9    = x_hat_list[-2].reshape(28,28, Num_samples)[:,:,0]  
    x_hat_2D_10   = x_hat_list[-1].reshape(28,28, Num_samples)[:,:,0] 
    
    fig, ax = plt.subplots(nrows=2,ncols=5)

    ax[0,0].imshow(data2D[:,:,0] ) 
    ax[0,0].set_title("Original")
    ax[0,1].imshow(y[:,0].reshape(-1,28)) 
    ax[0,1].set_title("Compressed")

    ax[0,0].set_axis_off()
    ax[0,1].set_axis_off()
    ax[0,2].set_axis_off()
    ax[0,3].set_axis_off()
    ax[0,4].set_axis_off()
 

    ax[1,0].imshow(x_hat_2D_6)
    ax[1,1].imshow(x_hat_2D_7)
    ax[1,2].imshow(x_hat_2D_8)
    ax[1,3].imshow(x_hat_2D_9)
    ax[1,4].imshow(x_hat_2D_10)

    ax[1,0].set_axis_off()
    ax[1,1].set_axis_off()
    ax[1,2].set_axis_off()
    ax[1,2].set_title("Reconstructed")
    ax[1,3].set_axis_off()
    ax[1,4].set_axis_off()
    

    plt.show()
    pdb.set_trace()

     