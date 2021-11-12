import os
import timeit
import torch, torchvision
from sentence_transformers import SentenceTransformer, CrossEncoder, util
from transformers import (
    AutoModel,
    AutoModelForSequenceClassification,
    AutoTokenizer,
    AutoConfig,
    BartForConditionalGeneration,
    RobertaForSequenceClassification,
    AutoModelForCausalLM,
    GPT2Config,
    GPT2DoubleHeadsModel,
    GPT2Tokenizer,
)


save_dir = "/home/solidsnake/ai/Golden_Group/ai-models/development/sentence-emebeddings/all-mpnet-base-v2"
model_name_or_path = "sentence-transformers/all-mpnet-base-v2"


# Natural Language Intent (Zero-Shot Classification)
config = AutoConfig.from_pretrained(model_name_or_path)
tokenizer = AutoTokenizer.from_pretrained(model_name_or_path)
model = AutoModel.from_pretrained(
    model_name_or_path,
    from_tf=False,
    config=config,
)

# print(config)

# # convAI model
# config = GPT2Config.from_pretrained(config_name, cache_dir=cache_dir)
# tokenizer = GPT2Tokenizer.from_pretrained(tokenizer_name, cache_dir=cache_dir)
# model = GPT2DoubleHeadsModel.from_pretrained(
#     model_name_or_path,
#     from_tf=False,
#     config=config,
#     cache_dir=cache_dir,
# )


# config = AutoConfig.from_pretrained(config_name, cache_dir=cache_dir)
# tokenizer = AutoTokenizer.from_pretrained(tokenizer_name, cache_dir=cache_dir)
# model = AutoModelForCausalLM.from_pretrained(
#     model_name_or_path,
#     from_tf=False,
#     config=config,
#     cache_dir=cache_dir,
# )

config.save_pretrained(save_dir)
model.save_pretrained(save_dir)
tokenizer.save_pretrained(save_dir)


# load model
# config = AutoConfig.from_pretrained(save_dir)
# tokenizer = AutoTokenizer.from_pretrained(save_dir)
# model = AutoModelForSequenceClassification.from_pretrained(save_dir)

# tokenizer = AutoTokenizer.from_pretrained(model_name, config=config)
# model = AutoModelForSequenceClassification.from_pretrained(model_name, config=config)
# model = RobertaForSequenceClassification.from_pretrained(model_name, config=config)
