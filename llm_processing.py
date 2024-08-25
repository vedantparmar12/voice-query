from transformers import AutoTokenizer, AutoModelForCausalLM
from config import LLM_MODEL_NAME

tokenizer = AutoTokenizer.from_pretrained(LLM_MODEL_NAME)
model = AutoModelForCausalLM.from_pretrained(LLM_MODEL_NAME)

def generate_response(input_text, max_sentences=2):
    if "Error in speech recognition" in input_text:
        return "I'm sorry, there was an error in speech recognition. Please try again."
    
    prompt = f"Human: {input_text}\nAI:"
    inputs = tokenizer(prompt, return_tensors="pt")
    outputs = model.generate(**inputs, max_new_tokens=100, num_return_sequences=1)
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    
    sentences = response.split('.')[:max_sentences]
    return '.'.join(sentences) + '.'