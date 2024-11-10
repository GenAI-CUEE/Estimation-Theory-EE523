## Tutorial 4: Maximum A Posteriori Estimation

by *Suwichaya Suwanwimolkul, Ph.D.*

The coding exercies and examples are used as parts of  *Lecture V: Maximum A Posteriori Estimation*  in **Estimation Theory EE2102523**. 

The lecture handout for [`Lecture V: Maximum A Posteriori Estimation`](https://drive.google.com/drive/folders/1VAEFqNYpjVlbc7dac92entSJlO_gzd-6?usp=drive_link) are attached in Google drive.

Let's start
<a target="_blank" href="https://colab.research.google.com/github/GabbySuwichaya/Estimation-Theory-EE523/blob/master/Tutorial4/main.ipynb)">
  <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>
</a>

or you can run `main.ipynb` locally for the coding exercies and examples.

The topics covered in this exercise are: 
- [Maximum A Posteriori Estimation](#maximum-a-posteriori-estimation)
  - [The MAP Algorithm](#map-algorithm)
  - [Extension to estimate parameters in priors](#extend-the-map-estimator-to-update-the-parameters-of-prior-distribution)
  - [Apply to reconstruct compressed data using MAP](#apply-map-estimation)
  - [Apply to reconstruct compressed data using MLE](#what-if-there-is-no-prior--using-mle)
  - [Compairison](#plot-outputs)



Note: Don't forget to do `pip install -r requirements.txt`

  

### Quick start 

You can also try everything on your local machine by installing dependenies listed in `requirements.txt` with 

```
pip install -r requirements.txt
```

Then, start the jupyternote book [`main.ipynb`](main.ipynb).
 

 
### Final Notes.
-  Don't forget to install the dependency `pip install -r requirements.txt`
- `utils.py` contains the supplenmary implementations for each fucntion used in `main.ipynb` 
- Good luck! 