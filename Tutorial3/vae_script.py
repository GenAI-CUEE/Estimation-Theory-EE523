import torch
import torch.utils.data
from torch import  optim 
from torchvision import datasets, transforms 
import matplotlib.pyplot as plt 
from models import VAE, loss_function
from tqdm import tqdm
import os
import numpy as np


if torch.cuda.is_available():
    device = torch.device("cuda")
else:
    device = torch.device("cpu")
 
train_loader = torch.utils.data.DataLoader(
    datasets.MNIST('../data', train=True, download=True,
                   transform=transforms.ToTensor()),
    batch_size=4, shuffle=True)

test_loader = torch.utils.data.DataLoader(
    datasets.MNIST('../data', train=False, transform=transforms.ToTensor()),
    batch_size=1, shuffle=False)
  
os.makedirs('results', exist_ok=True)

model = VAE().to(device)
optimizer = optim.Adam(model.parameters(), lr=1e-3)

model.train()
kl_loss_  = []
bce_loss_ = []
total_loss_ = []

weight = 0.25

train_loss = 0
for epoch in range(4):
    pbar  = tqdm(train_loader)
    for batch_idx, (data, _) in enumerate(pbar):
        data = data.to(device)
        optimizer.zero_grad()
        recon_batch, mu, logvar = model(data)
        
        bce_loss, kl_loss = loss_function(recon_batch, data, mu, logvar)

        loss = (1-weight)*bce_loss + weight*kl_loss
        loss.backward()
        
        train_loss += loss.item()
        bce_loss_.append(bce_loss.item())
        kl_loss_.append(kl_loss.item())
        total_loss_.append(loss.item())
        
        optimizer.step() 

        pbar.set_description('====> Epoch: %d train loss: %.2f ,Average loss: %.4f' % ((epoch, loss.item(), train_loss / len(total_loss_))))


plt.figure(figsize=(12,6))
plt.plot(kl_loss_[:10000], color="blue", linewidth=1, alpha=0.5, label="KL-loss") 
plt.plot(bce_loss_[:10000], color="red", linewidth=1,  alpha=0.5, label="BCE-loss") 
plt.plot(total_loss_[:10000], color="black", linewidth=1,  alpha=0.5, label="Total") 

plt.ylabel("Learning Losses")
plt.xlabel("Iterations")
plt.grid()
plt.legend() 
plt.savefig("results/Learning_Loss_Curve.png")


model.eval()
test_loss = 0
test_bce_loss = 0
test_kl_loss = 0


with torch.no_grad():
    for i, (data, _) in enumerate(test_loader):
        if i < 5:
            data = data.view(-1)
            missing_xy = np.random.randint(28*28, size=int(28*28/2)) 
            data[missing_xy] = 0
            data         = data.view(1,1,28,28).to(device) 
            mu, logvar  = model.encode(data.view(-1, 784))
            z           = model.reparameterize(mu, logvar) 
            recon_batch = model.decode(z)

            test_bce_loss_, test_kl_loss_ = loss_function(recon_batch, data, mu, logvar)
            test_bce_loss += test_bce_loss_.item()
            test_kl_loss  += test_kl_loss_.item()

            intput = data.view(28, 28,1).detach().cpu().numpy()
            output = recon_batch.view(28, 28,1).detach().cpu().numpy()
            
            latent_represent = z.view(4, 5,1).detach().cpu().numpy()

            f, ax = plt.subplots(1,2, figsize=(10, 5))
            ax[0].imshow(intput)
            ax[0].set_title("Input")
            ax[0].axis('off')
            ax[1].imshow(output) 
            ax[1].axis('off')
            ax[1].set_title("Generated Output")
            plt.savefig('results/reconstruction_' + str(i) + '.png')   
            plt.show()               
            plt.close("all")

test_loss /= len(test_loader.dataset)
print('====> Test set loss: {:.4f}'.format(test_loss))
