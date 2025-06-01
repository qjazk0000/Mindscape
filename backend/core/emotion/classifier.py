# core/emotion/classifier.py

from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import torch.nn.functional as F
from typing import Union, List
import os

# 모델 전역 캐싱 변수
_tokenizer = None
_model = None
_id2label = None

def load_model():
    global _tokenizer, _model, _id2label
    
    if _tokenizer is not None and _model is not None:
        return _tokenizer, _model, _id2label
    
    try:
        model_name = os.getenv("GOEMOTIONS_MODEL", "monologg/bert-base-cased-goemotions-original")
        _tokenizer = AutoTokenizer.from_pretrained(model_name)
        _model = AutoModelForSequenceClassification.from_pretrained(model_name)
        _id2label = _model.config.id2label
    except Exception as e:
        raise RuntimeError(f"모델 로딩 실패: {str(e)}")
    
    return _tokenizer, _model, _id2label



def classify_emotions(
    text_input: Union[str, List[str]],
    top_n: int=5
    ) -> Union[List[dict], List[List[dict]]]:
    """
    감정 분류 함수: 단일 문자열 또는 문자열 리스트 입력 가능
    
    
    Args:
        text_input (str or list of str): 분석할 문장 또는 문장 리스트
        top_n (int): 상위 N개의 감정 반환
        
    Returns:
        List of dict (단일입력) or List of List of dict (다중 입력)
        
    """
    
    tokenizer, model, id2label = load_model()
    
    if isinstance(text_input, str):
       texts = [text_input]
    elif isinstance(text_input, list):
        if not all(isinstance(t, str) for t in text_input):
            raise ValueError("리스트 내 모든 요소는 문자열이어야 합니다.")
        text = text_input
    else:
        raise TypeError("text_input은 문자열 또는 문자열 리스트여야 합니다.")
    
    results = []
    
    for text in texts:
        if not text.strip():
            results.append([{"label": "empty_input", "score":1.0}])
            continue
        
        inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)
        
        try:
            with torch.no_grad():
                outputs = model(**inputs)
            
            probs = F.softmax(outputs.logits, dim=-1).squeeze()
            
            sample_result = [
                {"label": id2label[i], "score": round(p.item(), 4)}
                for i, p in enumerate(probs)
            ]
            sorted_result = sorted(sample_result, key=lambda x: x["score"], reverse=True)[:top_n]
            results.append(sorted_result)
            
        except Exception as e:
            results.append([{"label": "error", "score": 1.0, "detail": str(e)}])
            
    
    # 단일 문자열 입력이었다면 첫 결과만 반환
    return results[0] if isinstance(text_input, str) else results
