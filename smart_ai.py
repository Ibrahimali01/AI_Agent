
import re
import math
import random

def similarity(s1, s2):
    s1 = s1.lower()
    s2 = s2.lower()
    len1 = len(s1)
    len2 = len(s2)
    if len1 == 0 or len2 == 0:
        return 0.0
    d = [[0]*(len2+1) for _ in range(len1+1)]
    for i in range(len1+1):
        d[i][0] = i
    for j in range(len2+1):
        d[0][j] = j
    for i in range(1, len1+1):
        for j in range(1, len2+1):
            if s1[i-1] == s2[j-1]:
                cost = 0
            else:
                cost = 1
            d[i][j] = min(d[i-1][j] + 1, d[i][j-1] + 1, d[i-1][j-1] + cost)
    max_len = max(len1, len2)
    return 1.0 - (d[len1][len2] / max_len)

knowledge_base = [
    ("مرحبا|أهلا|هلا", ["مرحباً بك في Termux AI!", "أهلاً وسهلاً، كيف يمكنني مساعدتك؟"]),
    ("كيف حالك|كيف الك|شكبرك", ["أنا بخير، شكراً لسؤالك!", "حالي جيد، وأنت كيف حالك؟"]),
    ("ما اسمك|من أنت", ["أنا Termux AI، مساعدك الذكي.", "أنا نموذج ذكاء اصطناعي يعمل في بيئة Termux."]),
    ("شكرا|شكراً|مشكور", ["عفواً، ديدتي.", "لا شكر على واجب، سررت بالمساعدة."]),
    ("وداعا|مع السلامة|باي", ["إلى اللقاء، أتمنى لك يوماً سعيداً.", "مع السلامة، أراك قريباً."]),
    ("ساعة|الوقت|التاريخ", ["للأسف، لا أملك صلاحية الوصول للوقت الحالي في هذا الكود البسيط.", "يمكنك استخدام أمر date في Termux."]),
    ("سور القرآن|القرآن", ["القرآن الكريم هو كتاب الله، أنزله على نبينا محمد صلى الله عليه وسلم.", "القرآن الكريم يتكون من 114 سورة."]),
]

def get_response(user_input):
    user_input = user_input.strip()
    best_sim = 0
    best_response = "عذراً، لم أفهم سؤالك. هل يمكنك إعادة الصياغة أو استخدام كلمات مفتاحية؟"
    for keywords, responses in knowledge_base:
        if re.search(keywords, user_input, re.IGNORECASE):
            return random.choice(responses)
        for keyword in keywords.split('|'):
            sim = similarity(user_input, keyword)
            if sim > best_sim and sim > 0.6:
                best_sim = sim
                best_response = random.choice(responses)
    return best_response

def main():
    print("مرحباً! أنا Termux AI، مساعدك الذكي. اكتب 'خروج' للإنهاء.")
    while True:
        user_input = input("أنت: ")
        if user_input.lower() in ['خروج', 'exit', 'quit']:
            print("مع السلامة!")
            break
        response = get_response(user_input)
        print("Termux AI:", response)

if __name__ == "__main__":
    main()
