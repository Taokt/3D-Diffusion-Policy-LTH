import torch
print("CUDA available:", torch.cuda.is_available())
print("cuDNN version:", torch.backends.cudnn.version())
print("Is cuDNN available?", torch.backends.cudnn.is_available())
