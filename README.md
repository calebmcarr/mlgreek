# mlgreek
A repository for training and generating AI models to compose Greek Prose.  See the wiki for more info.
## Getting started
These instructions will get a working copy of the project on your local machine.
### Prerequisites
What you'll need:
1. [Python v3+](https://www.python.org/downloads/)
2. [Tensorflow](https://www.tensorflow.org/install)
3. [*If using GPU-accelerated system*] [Tensorflow with GPU support](https://www.tensorflow.org/install/gpu)
4. [*If using GPU-accelerated system*] NVIDIA® GPU card with CUDA® Compute Capability 3.5 or higher

Once you have these, progress to install and test run
## Installing and Running Test 
*Highly recommended you run this in a virtual environment for python version control*
1. clone the repository
```
git clone https://github/calebmcarr/mlgreek.git
```
2. cd to the mlgreek repo
```
cd ./mlgreek
```
3. run the model script
[for CPU]
```
python model_cpu.py
```
4. [for GPU]
```
python model_gpu.py
```
### Generation test
When prompted:
```
Train or Generate: Generate
File name (without extension): Novum Testamentum
```
When complete, the model will spit out some text and save it to ./training_checkpoints/Novum Testamentum
### Training test
When prompted:
```
Train or Generate: Train
Number of Training Epochs: 20 [if CPU, 120 if GPU]
File name (without extension): Novum Testamentum
```
When complete, the model will spit out some text and save it to ./training_checkpoints/Novum Testamentum
## Authors
* **Caleb Carr** - Programmer and Documentation Author - [calebmcarr](https://github.com/calebmcarr)
* **Samuel Huskey** - Initial work - [sjhuskey](https://github.com/sjhuskey)
## License
This project is licensed under the GNU GPL v3.  Can be viewed at [LICENSE.txt](LICENSE.txt)

## Acknowledgements
* Homer
* Plato
* Paul of Tarsus
