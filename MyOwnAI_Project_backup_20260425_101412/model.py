import torch
import torch.nn as nn

import numpy as np

class SimpleModel:
    def __init__(self, weights_path):
        self.weights = np.load(weights_path)
    
    def predict(self, x):
        return np.dot(x, self.weights)


class SmallTransformer(nn.Module):
    def __init__(self, vocab_size, d_model=64, nhead=4, num_layers=2, dim_feedforward=256, dropout=0.1):
        super().__init__()
        self.d_model = d_model
        self.embedding = nn.Embedding(vocab_size, d_model)
        encoder_layer = nn.TransformerEncoderLayer(d_model=d_model, nhead=nhead,
                                                   dim_feedforward=dim_feedforward,
                                                   dropout=dropout, batch_first=True)
        self.transformer_encoder = nn.TransformerEncoder(encoder_layer, num_layers=num_layers)
        self.fc_out = nn.Linear(d_model, vocab_size)

    def forward(self, x):
        x = self.embedding(x) * (self.d_model ** 0.5)
        x = self.transformer_encoder(x)
        x = self.fc_out(x)
        return x
