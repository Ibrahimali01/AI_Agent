
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
