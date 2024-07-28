 

Our goal is to provide the code-based visualization and exercises to understand the mathematics behind each of lectures in **Estimation Theory EE2102523 Year 2024** by *Suwichaya Suwanwimolkul*.


## Link to handout slides

- Link to [Google Derive](https://drive.google.com/drive/folders/1ay16iXuyqeCj_OQwCk_2MEGkXoVsAEs1?usp=sharing)   
- Link to [MS Team Folder](https://teams.microsoft.com/_#/school/FileBrowserTabApp/General?groupId=2d8dd0eb-8fac-4cdb-8dd7-d70a1e9ab3b4&threadId=19:KkkpzATb2QVQXJ7M_IP5WYUzIkOVGtQLC2BX0QROmd01@thread.tacv2&ctx=channel). 

## Quick start

Before first, you should create a conda environment for this course:

```
conda create -n EE523
```

Install some commonly used packages. 
First activate EE523 environment and install pip into anaconda environment. 

```
conda activate EE523
conda install pip 
```

Then, install the packages by pip... 

``` 
pip install numpy pandas tqdm matplotlib joypy
```

If you have already install these packages, you can skip the first few steps in the notebook.  



### The coding scripts & excercises 



- [x] [Tutorial 1: What is random sampling?* ](Tutorial1/main.ipynb) 

<a target="_blank" href="https://colab.research.google.com/github/GabbySuwichaya/Estimation-Theory-EE523/blob/master/Tutorial1/main.ipynb">
  <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>
</a>

    - Sampling from distirbution
    - Example of estimators (sample mean) 
 
- [x] [Tutorial 2: Estimator properties](Tutorial2/main.ipynb) 

<a target="_blank" href="https://colab.research.google.com/github/GabbySuwichaya/Estimation-Theory-EE523/blob/master/Tutorial2/main.ipynb">
  <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>
</a>

    - Estimator properties, 
    - Bias, MSE, Consistency 
    - Example of estimators (sample mean and sample variance)  
    - Homework 1. Simulation 

- [x] [Tutorial 3: Probabilistic Convergence](Tutorial2/main.ipynb) 

<a target="_blank" href="https://colab.research.google.com/github/GabbySuwichaya/Estimation-Theory-EE523/blob/master/Tutorial2/main.ipynb">
  <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>
</a>

    - Convergence in distribution, 
    - Central limit Theorems, 
    - KL divergence, 
    - Convergence in probability, 
    - Almost sure Convergence simulation. 
    - Homework 4. Simulation. 

- [x] [Tutorial 3: KL-Divergence Loss *to support Lecture V: MLE-KL, Conditional MLE,  MLE-MSE, MLE-MAE, MMSE*](Tutorial3/main.ipynb) 

<a target="_blank" href="https://colab.research.google.com/github/GabbySuwichaya/Estimation-Theory-EE523/blob/master/Tutorial3/main.ipynb">
  <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>
</a>

    - Review about KL Divergence 
    - Variational Auto Encoder
    - Why KL Divergence is used in VAE
    - Apply VAE to reconstruct the image data

- [x] [Tutorial 4: Wiener Filter and MAP Esitmation *to support Lecture VI: LMSE, Wiener Filtering, Maximum A Posteriori*](Tutorial4/main.ipynb)

<a target="_blank" href="https://colab.research.google.com/github/GabbySuwichaya/Estimation-Theory-EE523/blob/master/Tutorial4/main.ipynb">
  <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>
</a>

    - Wiener Filtering
    - Auto/Cross-Correlation Checking 
    - MAP Esitmation 
    - Gaussian-Laplacian conjugate prior and extension to estimate other unknowns in the posteriori distribution
    - Apply to reconstruct image data from compression in compressive sensing.

<!-- - [x] [Coding: System Checking for Jypyter Notebook Grading*](Coding/Step0_Testing.ipynb)

<a target="_blank" href="https://colab.research.google.com/github/GabbySuwichaya/Estimation-Theory-EE523/blob/master/Coding/Step0_Testing.ipynb">
  <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>
</a>

    - Please follow the following steps, so that I can check if the system is working fine for the actual grading. 
    - Please implement your work in the provided `.ipynb` file.   
    - Once you finished, put the current folder that contains your `.ipynb` file into a new folder that has  your student id  as the folder name.  
    - For example,  `6470160121/Coding/Step0_Testing.ipynb` (VERY IMPORTANT) 
    - When you finished, please zip the folder (`6470160121.zip`) and submit it into  `Testing_NotebookGrading` folder in MS Team Folder  -->

<!-- - [x] [Homework 4](Homework4/simulation.ipynb)   

<a target="_blank" href="https://colab.research.google.com/github/GabbySuwichaya/Estimation-Theory-EE523/blob/master/Homework4/simulation.ipynb">
  <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>
</a>  -->

<!-- Total scores is 30 that is to be collected as 20 scores for your Homework 4.  

Please read [Homework4 Readme](Homework4/Readme.md) carefully 

    - You can also visit the simulation homework with the attached google collab link.    
    - Deadline 06/12/2023 
       -->

### Getting Started

1. Relocate to the directory, e.g., `Tutorial` folder.
2. Look for the  instructions (e.g. [Tutorial 1 Readme](Tutorial1/Readme.md)) for installing dependencies. 
3. You may execute the `main` file in python or ipynb fileformat. 

 

### Citation 

```
@book{CUEE523,
  author        = {Suwichaya Suwanwimolkul},
  title         = {{L}ecture {N}otes on {E}stimation {T}heory {EE}523},
  month         = {Semester I},
  year          = {2024},
  publisher     = {Chulalongkorn Univeristy},
  url           = "https://github.com/GabbySuwichaya/Estimation-Theory-EE523"
}
```