from transformers import AutoTokenizer
from transformers import AutoModelForSeq2SeqLM

MODEL_NAME = "google/flan-t5-base"

tokenizer = None
model = None


def load_model():
    global tokenizer
    global model

    if tokenizer is None:
        print("Loading tokenizer...")
        tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)

    if model is None:
        print("Loading model...")
        model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_NAME)


def generate_answer(prompt):
    load_model()

    inputs = tokenizer(
        prompt,
        return_tensors="pt",
        truncation=True,
        max_length=512
    )

    outputs = model.generate(
        **inputs,
        max_new_tokens=100
    )

    return tokenizer.decode(
        outputs[0],
        skip_special_tokens=True
    )