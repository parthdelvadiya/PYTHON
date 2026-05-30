# Transformers

Transformers are Deep Learning models that use **Attention** to understand relationships between words, images, or other data.

They were introduced in:

```python
"Attention Is All You Need" (2017)
```

and power modern AI systems like:

* GPT
* BERT
* LLaMA
* Gemini

---

# Why Transformers?

Older models:

```python
RNN
LSTM
```

processed data sequentially:

```python
Word1 → Word2 → Word3
```

This was:

* Slow
* Difficult for long sequences

Transformers process everything simultaneously:

```python
Word1
Word2
Word3
↓
All Together
```

making training much faster.

---

# Core Idea: Attention

Attention helps the model focus on important information.

Example:

```python
"The dog chased the ball because it was fast."
```

Transformer learns:

```python
it → dog
```

by paying attention to related words.

---

# Self-Attention

Each word looks at every other word.

Example:

```python
I love Machine Learning
```

The word:

```python
Learning
```

can directly understand:

```python
Machine
```

without passing through intermediate words.

---

# Main Components

```python
Input Embeddings
↓
Positional Encoding
↓
Self-Attention
↓
Feed Forward Network
↓
Output
```

---

# Types of Transformers

### Encoder Only

Example:

```python
BERT
```

Used for:

* Classification
* Sentiment Analysis

---

### Decoder Only

Example:

```python
GPT
```

Used for:

* Text Generation
* Chatbots
* Code Generation

---

### Encoder + Decoder

Example:

```python
T5
```

Used for:

* Translation
* Summarization

---

# Advantages

* Fast Training
* Handles Long Context
* Highly Scalable
* State-of-the-Art Performance

---

# Applications

```python
ChatGPT
Machine Translation
Text Summarization
Image Classification
Speech Recognition
Recommendation Systems
```

---

# Interview-Level Summary

```python
Transformer is a deep learning architecture that uses self-attention to process all input elements simultaneously, enabling efficient learning of long-range relationships and powering modern AI models like GPT and BERT.
```

---

# One-Line Analogy

```python
RNN reads a book word-by-word.

Transformer looks at the entire page at once.
```