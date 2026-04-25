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
