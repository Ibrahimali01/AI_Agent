
import numpy as np
import os

def train():
    np.random.seed(42)
    weights = np.random.randn(10, 5)
    weights_path = os.path.join(os.path.dirname(__file__), "weights.npy")
    np.save(weights_path, weights)
    print("Training complete. Weights updated.")

if __name__ == "__main__":
    train()
