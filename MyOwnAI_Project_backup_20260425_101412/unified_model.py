# --- From file: model.py ---
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


# --- From file: dataset.py ---

import torch
from torch.utils.data import Dataset
import re

class TextDataset(Dataset):
    def __init__(self, file_path, seq_length=50):
        with open(file_path, 'r', encoding='utf-8') as f:
            text = f.read()

        # بناء المفردات البسيطة
        self.chars = sorted(list(set(text)))
        self.char_to_idx = {ch: i for i, ch in enumerate(self.chars)}
        self.idx_to_char = {i: ch for i, ch in enumerate(self.chars)}
        self.vocab_size = len(self.chars)

        self.data = text
        self.seq_length = seq_length
        self.data_len = len(text)

    def __len__(self):
        return max(0, self.data_len - self.seq_length)

    def __getitem__(self, idx):
        chunk = self.data[idx:idx + self.seq_length + 1]
        input_seq = [self.char_to_idx.get(ch, 0) for ch in chunk[:-1]]
        target_seq = [self.char_to_idx.get(ch, 0) for ch in chunk[1:]]
        return torch.tensor(input_seq, dtype=torch.long), torch.tensor(target_seq, dtype=torch.long)


# --- From file: train.py ---

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


# --- From file: chat.py ---
import torch
import torch.nn as nn
import os
from model import SmallTransformer

def chat():
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    # 1. تحميل القاموس
    if not os.path.exists('vocab.pth'):
        print("خطأ: ملف vocab.pth غير موجود!")
        return
    vocab = torch.load('vocab.pth')
    inv_vocab = {v: k for k, v in vocab.items()}
    vocab_size = len(vocab)

    # 2. بناء وتعريف النموذج بنفس الإعدادات السابقة
    model = SmallTransformer(vocab_size=vocab_size, d_model=64, nhead=4).to(device)

    # 3. تحميل الأوزان
    if os.path.exists('best_model.pth'):
        model.load_state_dict(torch.load('best_model.pth', map_location=device))
        print("تم تحميل العقل الذكي بنجاح!")
    else:
        print("خطأ: ملف best_model.pth غير موجود!")
        return

    model.eval()

    print("\n--- مرحباً بك في دردشة الوحش الصغير ---")
    print("(اكتب 'exit' للخروج)\n")

    while True:
        text = input("أنت: ")
        if text.lower() == 'exit': break

        # تحويل النص لأرقام (Tokenization)
        input_ids = [vocab.get(ch, 0) for ch in text]
        input_tensor = torch.tensor([input_ids]).to(device)

        # التوقع (Inference)
        with torch.no_grad():
            output = model(input_tensor)
            # اختيار الحرف الأكثر احتمالاً لكل موقع
            predicted_indices = torch.argmax(output, dim=-1)[0].tolist()
            response = "".join([inv_vocab.get(idx, "") for idx in predicted_indices])

        print(f"الوحش الصغير: {response}")

if __name__ == "__main__":
    chat()


