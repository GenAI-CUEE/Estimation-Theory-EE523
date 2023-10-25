## Tutorial 4:  Wiener Filtering and Maximum A Posteriori and their applications 

by *Suwichaya Suwanwimolkul, Ph.D.*

The coding exercies and examples are used as parts of  *Lecture VI: LMSE, Wiener Filtering, Maximum A Posteriori*  in **Estimation Theory EE2102523**. 

The lecture handout for [`Lecture VI: LMSE, Wiener Filtering, Maximum A Posteriori`](https://drive.google.com/drive/folders/1VAEFqNYpjVlbc7dac92entSJlO_gzd-6?usp=drive_link) are attached in Google drive.

Let's start

<a target="_blank" href="https://colab.research.google.com/github/GabbySuwichaya/Estimation-Theory-EE523/blob/master/Tutorial4/main.ipynb">
  <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>
</a>

or you can run `main.ipynb` locally for the coding exercies and examples.

The topics covered in this exercise are:

- [Wiener Filtering](#wiener-filter)  
    - [Initialization](#initial-settings)
    - [Wiener Filter Algorithm](#wiener-filter-algorithm)
    - [Apply Wiener Fitler](#apply-wiener-filter)
- [Maximum A Posteriori Estimation](#maximum-a-posteriori-estimation)
    - [The MAP Algorithm](#map-algorithm)
    - [Extension to estimate parameters in priors](#extend-the-map-estimator-to-update-the-parameters-of-prior-distribution)
    - [Apply to reconstruct compressed data](#apply-map-estimation)


Note: Don't forget to do `pip install -r requirements.txt`
 
 
References:

1. How to check https://online.stat.psu.edu/stat510/
2. Coding (in matlab version): https://dspcookbook.github.io/ ...
 
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