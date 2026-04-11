import joblib
from pathlib import Path

MODEL_PATH = Path("ml/model.joblib")

def load_model():
    if not MODEL_PATH.exists():
        raise FileNotFoundError(f"Model file not found at {MODEL_PATH}. Run ml/train.py first")
    return joblib.load(MODEL_PATH)


model = load_model()