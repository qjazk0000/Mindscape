import os
from datasets import load_dataset

# GoEmotions 데이터셋 다운로드
dataset = load_dataset("go_emotions")

# 디렉토리 설정
raw_dir = os.path.join("data", "raw", "goemotions")
processed_dir = os.path.join("data", "processed", "goemotions")

os.makedirs(raw_dir, exist_ok=True)
os.makedirs(processed_dir, exist_ok=True)

# 각 split을 CSV 파일로 저장
for split in ["train", "validation", "test"]:
    # 원본 JSON 저장 (raw)
    raw_path = os.path.join(raw_dir, f"{split}.json")
    dataset[split].to_json(raw_path)
    
    # 전처리된 csv 저장 (text + label만 추출, processed)
    df = dataset[split].to_pandas()[["text", "labels"]]
    processed_path = os.path.join(processed_dir, f"{split}.csv")
    df.to_csv(processed_path, index=False)