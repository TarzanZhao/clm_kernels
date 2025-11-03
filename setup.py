from setuptools import setup
from torch.utils.cpp_extension import CUDAExtension, BuildExtension

setup(
    name="clm_kernels",
    packages=['clm_kernels'],
    ext_modules=[
        CUDAExtension(
            name="clm_kernels._C",
            sources=[
                "clm_kernels.cu",
                "ssim.cu",
                "adam.cu",
                "ext.cpp"
            ],
            extra_compile_args={
                "nvcc": ["-O3"]
            }
        )
    ],
    cmdclass={
        'build_ext': BuildExtension
    }
)