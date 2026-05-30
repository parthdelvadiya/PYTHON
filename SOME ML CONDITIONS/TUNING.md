# Model Tuning Techniques in AI & LLMs

Model tuning means adapting a pre-trained model to a specific task or domain.

Example:

```python
GPT → Medical Chatbot
GPT → Legal Assistant
BERT → Sentiment Analysis
```

Instead of training from scratch, we tune an existing model.

---

# 1. Pretraining

Model learns from massive datasets.

Example:

```python
Books
Websites
Articles
Wikipedia
```

Result:

```python
General Knowledge Model
```

Examples:

* GPT
* BERT
* LLaMA

### Expensive

Requires:

```python
Thousands of GPUs
Huge Datasets
```

---

# 2. Transfer Learning

Use a pretrained model and adapt it to a new task.

Example:

```python
ImageNet Model
↓
Cat vs Dog Classification
```

### Benefit

```python
Less Data
Less Training Time
```

---

# 3. Fine-Tuning

Train all model parameters on your custom dataset.

Example:

```python
GPT
↓
Train on Medical Data
↓
Medical GPT
```

### Advantages

* Highest accuracy
* Domain-specific knowledge

### Disadvantages

* Expensive
* Requires more GPU memory

---

# 4. Feature Extraction

Freeze pretrained model.

Only train final layer.

Example:

```python
BERT
↓
Freeze BERT
↓
Train Classification Layer
```

### Advantages

* Fast
* Cheap

### Disadvantages

* Less flexible

---

# 5. PEFT

Full Form:

```python
Parameter Efficient Fine Tuning
```

Instead of training billions of parameters:

```python
Train only a small subset
```

### Advantages

* Cheap
* Fast
* Popular for LLMs

---

# 6. LoRA

Full Form:

```python
Low Rank Adaptation
```

Most popular PEFT technique.

Idea:

```python
Freeze Original Model
↓
Add Small Trainable Layers
↓
Train Only Them
```

### Advantages

* Very Low Cost
* Small Storage
* Industry Standard

### Most Common LLM Tuning Method

```python
LoRA
```

---

# 7. QLoRA

Quantized LoRA.

Combines:

```python
Quantization
+
LoRA
```

### Advantages

* Less RAM
* Can fine-tune large models on smaller GPUs

### Example

```python
LLaMA 2
Mistral
Gemma
```

---

# 8. Instruction Tuning

Teach model to follow instructions.

Example Dataset:

```python
Question:
What is Python?

Answer:
Python is a programming language.
```

### Result

Model becomes better at:

```python
Chat
Question Answering
Assistants
```

---

# 9. Supervised Fine-Tuning (SFT)

Most common tuning step.

Dataset:

```python
Input → Desired Output
```

Example:

```python
Translate English → French
```

Model learns from labeled examples.

---

# 10. Reinforcement Learning from Human Feedback (RLHF)

Used in modern chatbots.

Process:

```python
Human Feedback
↓
Reward Model
↓
Model Improvement
```

### Goal

Make responses:

```python
Helpful
Safe
Accurate
```

Used in:

* ChatGPT
* Claude
* Gemini

---

# 11. Domain Adaptation

Specialized fine-tuning for a specific field.

Examples:

```python
Healthcare
Finance
Law
Education
```

Result:

```python
Domain Expert Model
```

---

# Comparison

| Technique | Train Parameters |
|------------|------------------|
| Pretraining | All |
| Transfer Learning | Some |
| Fine-Tuning | All |
| Feature Extraction | Final Layers |
| PEFT | Small Subset |
| LoRA | Very Few |
| QLoRA | Very Few |
| SFT | Usually All/PEFT |
| RLHF | Reward-Based |

---

# What Is Used Most Today?

### Small Models

```python
Fine-Tuning
```

### Large Language Models

```python
LoRA
QLoRA
PEFT
```

### ChatGPT-Style Models

```python
SFT
+
RLHF
```

---

# Final Summary

| Technique | Purpose |
|------------|----------|
| Pretraining | Learn General Knowledge |
| Transfer Learning | Reuse Existing Knowledge |
| Fine-Tuning | Adapt Entire Model |
| Feature Extraction | Train Only Last Layer |
| PEFT | Efficient Fine-Tuning |
| LoRA | Most Popular LLM Tuning |
| QLoRA | LoRA + Quantization |
| SFT | Learn from Examples |
| RLHF | Learn from Human Feedback |
| Domain Adaptation | Become Expert in a Domain |
