# Introduction
This project is for computing generating sets of permutation groups of arrays induced by reshapes and transpositions for use in [GAP](https://www.gap-system.org/)). This was the topic of my thesis, but for a formally published foundation we refer to [Ronse](https://www.sciencedirect.com/science/article/pii/0012365X83901000)). Without going into unessecary detail the generating sets we compute and provide are for the shapes consisting solely of prime number.

This repository consists of two major parts: 
# Precomputed generating sets
Precomputed generating sets for groups up tot order ~500 are stored in gapcode1.csv and gapcode2.csv. These files are large because our generating sets are exponential is the size of the numbers. This is still managebale for group size up to 1000 or so, but might not work well after that.

Full results of the computations we did can be found in gap.csv.
# Utilities
The python scripts contain utitlies for actually calculating the generating sets and forming a string that GAP can parse. The main entry point is main.py which can be used to either just calculate all generating sets or to specifically calculate the generating set for a specific group.

# Disclaimer
These utilities are provided as is and can be used by anyone however they want, but the goal of this project was not to write enterprise level software. So take care to read any code before running it as some external files are used. Running it in it's own folder is reccomended. For most use cases you will probably need to edit some parts of the files.
