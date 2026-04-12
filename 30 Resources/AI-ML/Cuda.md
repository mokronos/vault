

# Connection to C++

- https://stackoverflow.com/questions/9846523/explanation-of-cuda-c-and-c
# General

- need to synchronize after unified memory allocation kernel call because kernels are called asynchronously. For normal allocation and cudaMemCopy the cudaMemCopy call for copying back to the host device automatically syncs.