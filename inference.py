""" Stable diffusion model inference example code.
- Author: Bono (qhsh9713@gmail.com)
"""

import argparse


def parse():
    """
    Parse arguments for the inference.
    """
    parser = argparse.ArgumentParser(
        description="Stable Diffusion Model Inference Example"
    )
    parser.add_argument(
        "--device", type=str, default="cuda", help="Device to run the model on."
    )
    return parser.parse_args()


if __name__ == "__main__":
    args = parse()
    print(args)
