# LLM (Large Language Model) Interview Questions & Answers

---

# 1. What is an LLM?

### Answer

LLM (Large Language Model) is a neural network trained on massive amounts of text data to understand and generate human-like language.

### Examples

- GPT
- Llama
- Gemini
- Claude
- Mistral

### Real Life Example

Input:

```text
Translate "Hello" into French.
```

Output:

```text
Bonjour
```

---

# 2. How does an LLM work internally?

### Answer

Workflow:

```text
Text
 ↓
Tokenization
 ↓
Embeddings
 ↓
Transformer Layers
 ↓
Attention Mechanism
 ↓
Next Token Prediction
 ↓
Generated Response
```

The model predicts one token at a time until the response is complete.

---

# 3. What are Tokens?

### Answer

Tokens are smaller pieces of text processed by the model.

### Example

```text
Hello World
```

May become:

```text
["Hello", "World"]
```

or

```text
["Hel", "lo", "World"]
```

depending on tokenizer.

---

# 4. Why do LLMs use Tokens instead of Words?

### Answer

Benefits:

- Handle unknown words
- Support multiple languages
- Better vocabulary efficiency
- Reduce model size

---

# 5. What are Embeddings?

### Answer

Embeddings are numerical vector representations of text.

### Example

```text
Cat → [0.12, 0.55, -0.34 ...]
Dog → [0.15, 0.50, -0.30 ...]
```

Since cat and dog are similar, their vectors are close.

---

# 6. What is Attention?

### Answer

Attention allows the model to focus on important words while generating responses.

### Example

```text
The animal didn't cross the road because it was tired.
```

The word:

```text
it
```

refers to:

```text
animal
```

Attention helps the model understand that relationship.

---

# 7. What is Self-Attention?

### Answer

Each word looks at every other word in the sentence to understand context.

### Example

```text
I deposited money in the bank.
```

vs

```text
I sat near the river bank.
```

Self-attention helps identify the correct meaning of "bank".

---

# 8. What is the Transformer Architecture?

### Answer

Transformers replaced RNNs and LSTMs.

Main components:

1. Attention
2. Feed Forward Network
3. Layer Normalization
4. Positional Encoding

Benefits:

- Faster training
- Parallel processing
- Better long-context understanding

---

# 9. Why were Transformers introduced?

### Answer

Problems with RNNs:

- Slow training
- Vanishing gradients
- Poor long-range memory

Transformers solve these using attention mechanisms.

---

# 10. What is Context Window?

### Answer

Maximum number of tokens a model can process at once.

### Example

Context Window:

```text
128k tokens
```

The model can see up to 128k tokens simultaneously.

---

# 11. What happens if input exceeds context length?

### Answer

Older information gets truncated.

### Example

Context Window:

```text
8k tokens
```

Input:

```text
12k tokens
```

Some content will be removed before processing.

---

# 12. Why do LLMs Hallucinate?

### Answer

LLMs predict likely text.

They do not verify facts automatically.

### Example

If asked:

```text
Who won the FIFA World Cup in 2034?
```

The model may invent an answer.

---

# 13. How do you reduce Hallucinations?

### Answer

Methods:

1. RAG
2. Better prompts
3. Fine-tuning
4. Source grounding
5. Confidence filtering

---

# 14. What is Prompt Engineering?

### Answer

Designing prompts to get better outputs.

### Example

Bad Prompt:

```text
Explain Python
```

Better Prompt:

```text
Explain Python to a beginner with examples in under 100 words.
```

---

# 15. What is Zero-Shot Prompting?

### Answer

No examples are provided.

### Example

```text
Translate English to French:
Hello
```

---

# 16. What is One-Shot Prompting?

### Answer

One example is given.

### Example

```text
Dog → Animal

Cat →
```

Model predicts:

```text
Animal
```

---

# 17. What is Few-Shot Prompting?

### Answer

Multiple examples are given before the task.

### Example

```text
Dog → Animal
Cat → Animal
Rose → Plant

Tulip →
```

Output:

```text
Plant
```

---

# 18. What is Chain of Thought Prompting?

### Answer

Model is encouraged to reason step-by-step.

### Example

```text
Solve step by step:
A train travels...
```

This often improves reasoning performance.

---

# 19. What is Temperature?

### Answer

Controls randomness.

### Example

Temperature:

```text
0
```

Very deterministic.

Temperature:

```text
1.5
```

More creative and random.

---

# 20. When would you use Temperature = 0?

### Answer

Tasks requiring accuracy:

- Code generation
- SQL generation
- Data extraction
- Classification

---

# 21. When would you use Higher Temperature?

### Answer

Creative tasks:

- Story writing
- Marketing content
- Brainstorming
- Idea generation

---

# 22. What is Fine-Tuning?

### Answer

Training a pretrained LLM on domain-specific data.

### Example

General LLM:

```text
Knows medicine broadly.
```

Fine-Tuned Model:

```text
Specialized in radiology reports.
```

---

# 23. When should you use Fine-Tuning instead of RAG?

### Answer

Use Fine-Tuning for:

- Writing style
- Specialized behavior
- Domain-specific responses

Use RAG for:

- Frequently changing information
- Document search
- Knowledge retrieval

---

# 24. Why not Fine-Tune for Company Documents?

### Answer

Problems:

- Expensive
- Retraining required
- Slow updates

RAG is usually better.

---

# 25. What is RAG?

### Answer

Retrieval-Augmented Generation.

Workflow:

```text
User Question
 ↓
Embedding Search
 ↓
Retrieve Documents
 ↓
Send Context + Query to LLM
 ↓
Generate Answer
```

---

# 26. Why is RAG better than directly asking an LLM?

### Answer

Benefits:

- Less hallucination
- Uses company data
- Up-to-date information
- Source-based responses

---

# 27. What is a Vector Database?

### Answer

Stores embeddings for similarity search.

Examples:

- FAISS
- Chroma
- Pinecone
- Qdrant
- Weaviate

---

# 28. How do you evaluate an LLM?

### Answer

Metrics:

- Accuracy
- BLEU
- ROUGE
- Perplexity
- Human Evaluation
- Faithfulness

---

# 29. What is Perplexity?

### Answer

Measures how well a model predicts text.

Lower perplexity generally means better predictions.

---

# 30. What is Quantization?

### Answer

Reducing model precision.

Example:

```text
FP32 → INT8
```

Benefits:

- Smaller models
- Faster inference
- Lower memory usage

---

# 31. What is Model Distillation?

### Answer

A smaller model learns from a larger model.

### Example

Teacher:

```text
70B model
```

Student:

```text
7B model
```

Benefits:

- Faster
- Cheaper
- Easier deployment

---

# 32. A user says your chatbot gives wrong answers. How would you debug it?

### Answer

Check:

1. User query
2. Retrieved chunks
3. Embedding quality
4. Prompt template
5. LLM output
6. Source documents

Determine whether the issue is:

- Retrieval problem
- Prompt problem
- Model problem

---

# 33. What is AI Agent?

### Answer

An AI Agent can:

1. Reason
2. Plan
3. Use tools
4. Take actions

### Example

Travel Agent:

```text
User asks for flight.
↓
Search flights.
↓
Compare prices.
↓
Book ticket.
↓
Send confirmation.
```

---

# 34. What is Function Calling?

### Answer

Allows LLMs to invoke external tools.

### Example

User:

```text
What's the weather?
```

LLM:

```text
Calls Weather API
```

Returns live data.

---

# 35. Explain your GenAI project in one minute.

### Sample Answer

"I built a RAG-based chatbot where users upload PDFs. The system extracts text, chunks documents, generates embeddings, and stores them in a vector database. When a user asks a question, relevant chunks are retrieved through similarity search and passed to the LLM along with the query. This helps reduce hallucinations and enables accurate answers based on uploaded documents."