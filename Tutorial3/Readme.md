## Tutorial 3: MLE-KL and Application of KL Divergence in VAE 

by *Suwichaya Suwanwimolkul, Ph.D.*

The coding exercies and examples are used as parts of  *Lecture V: MLE-KL, Conditional MLE,  MLE-MSE, MLE-MAE, MMSE*  in **Estimation Theory EE2102523**. 

The topics covered in this exercise are: 
- [KL Divergence](#kl-divergence)  
    - [Central Limit Theorem Example](#central-limit-theorem-clt)
- [Variational Auto Encoder](#variational-auto-encoder-vae)
    - [What is it?](#what-is-variational-auto-encoder-vae)
    - [KL Divergence is used in learning](#why-we-need-kl-divergence-loss)
    - [Training](#training-phase)
    - [Testing](#testing-phase)
    - [Impact of KL Divergence](#how-kl-div-loss-impact-the-encoded-features)


Note: Don't forget to do `pip install -r requirements.txt`

References:

1. We use the example of variational auto encoder from [pytorch/examples](https://github.com/pytorch/examples)
2. Also, we obtain most of the content about the kl loss used in training  variational auto encoder from [This Medium Page](https://medium.com/@outerrencedl/variational-autoencoder-and-a-bit-kl-divergence-with-pytorch-ce04fd55d0d7) ...


### Quick start 


Install dependenies listed in `requirements.txt` by 

```
pip install -r requirements.txt
```

Then, start the jupyternote book [`main.ipynb`](main.ipynb).
 

 
### Final Notes.
-  Don't forget to install the dependency `pip install -r requirements.txt`
- `utils.py` contains the supplenmary implementations for each fucntion used in `main.ipynb` 
- Good luck! 