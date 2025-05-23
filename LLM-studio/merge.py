import torch
from peft import PeftModel
from transformers import AutoTokenizer, AutoModelForCausalLM, AutoConfig

# 定义模型路径
base_model_path = "主模型路径"
checkpoint_path = "lora训练载点权重"
output_path = "合并模型保存路径"

def apply_lora(model_name_or_path, output_path, lora_path):
    print(f"Loading the base model from {model_name_or_path}")
    base = AutoModelForCausalLM.from_pretrained(
        model_name_or_path, torch_dtype=torch.bfloat16, low_cpu_mem_usage=True, trust_remote_code=True
    )
    
    print(f"Loading the LoRA adapter from {lora_path}")
    lora_model = PeftModel.from_pretrained(
        base,
        lora_path,
        torch_dtype=torch.bfloat16,
    )
 
    print("Applying the LoRA")
    model = lora_model.merge_and_unload()
 
    print(f"Saving the target model to {output_path}")
    model.save_pretrained(output_path)

    print(f"Loading the tokenizer from {model_name_or_path}")
    base_tokenizer = AutoTokenizer.from_pretrained(
        model_name_or_path, use_fast=True, padding_side="left", trust_remote_code=True
    )
    
    print(f"Saving the tokenizer to {output_path}")
    base_tokenizer.save_pretrained(output_path)

    print(f"Updated model and tokenizer saved to {output_path}")

# 调用函数合并并保存模型
apply_lora(base_model_path, output_path, checkpoint_path)