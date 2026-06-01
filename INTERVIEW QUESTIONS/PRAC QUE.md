# AI/ML Interview Questions & Answers (Practical Scenarios)

---

# 1. You built a RAG chatbot. A user uploads a PDF. How do you handle it?

### Answer

The workflow would be:

1. Upload PDF
2. Extract text using PyPDFLoader
3. Split text into chunks
4. Generate embeddings for chunks
5. Store embeddings in a vector database
6. Convert user query into embedding
7. Retrieve relevant chunks
8. Send retrieved context + user query to LLM
9. Generate final answer

### Example

User uploads a 100-page company policy document and asks:

> "What is the leave policy?"

Instead of sending all 100 pages to the LLM, I retrieve only the chunks containing leave policy information and pass those chunks to the model.

### Why?

- Faster response
- Lower token cost
- Better accuracy
- Reduces hallucination

---

# 2. What if the uploaded PDF contains scanned images instead of text?

### Answer

Normal PDF extraction won't work.

I would use OCR tools such as:

- Tesseract OCR
- EasyOCR
- Azure Document Intelligence
- Google Vision OCR

### Workflow

PDF → Image Extraction → OCR → Text → Chunking → Embedding → Vector DB

---

# 3. What if the PDF is 10,000 pages?

### Answer

I would:

- Process asynchronously
- Create chunks in batches
- Generate embeddings in batches
- Store incrementally

### Why?

Large PDFs can exceed memory limits and increase processing time.

---

# 4. How do you reduce hallucinations in a RAG system?

### Answer

Methods:

1. Better chunking
2. Better embeddings
3. Re-ranking retrieved documents
4. Similarity score filtering
5. Prompt engineering
6. Return "I don't know" if confidence is low

### Example

If retrieved similarity score < threshold:

```python
if score < 0.7:
    return "Information not found in uploaded documents."
```

---

# 5. What if users upload multiple PDFs?

### Answer

Store metadata along with embeddings.

Example metadata:

```json
{
    "file_name": "policy.pdf",
    "page": 15,
    "department": "HR"
}
```

This allows filtering during retrieval.

---

# 6. What if two PDFs contain conflicting information?

### Answer

I would:

- Return source references
- Show confidence score
- Mention both sources

### Example

Document A says 20 leaves.

Document B says 25 leaves.

Response:

> "Document A mentions 20 leaves while Document B mentions 25 leaves. Please verify the latest version."

---

# 7. How would you evaluate a RAG system?

### Answer

Metrics:

- Context Precision
- Context Recall
- Faithfulness
- Answer Relevance
- Retrieval Accuracy

Tools:

- RAGAS
- DeepEval
- LangSmith

---

# 8. Your model performs well on training data but poorly on test data. Why?

### Answer

This is Overfitting.

The model memorized patterns instead of learning generalized relationships.

### Symptoms

Training Accuracy:

```text
98%
```

Validation Accuracy:

```text
70%
```

---

# 9. How do you reduce Overfitting?

### Answer

Methods:

1. More training data
2. Regularization
3. Dropout
4. Early Stopping
5. Cross Validation
6. Data Augmentation
7. Simpler model

---

# 10. What is Early Stopping?

### Answer

Training stops when validation loss stops improving.

### Example

```text
Epoch 1 -> Val Loss 0.8
Epoch 2 -> Val Loss 0.6
Epoch 3 -> Val Loss 0.5
Epoch 4 -> Val Loss 0.49
Epoch 5 -> Val Loss 0.52
Epoch 6 -> Val Loss 0.56
```

Best model = Epoch 4

No need to continue training.

---

# 11. What is Underfitting?

### Answer

Model is too simple to learn patterns.

### Symptoms

```text
Training Accuracy = 55%
Validation Accuracy = 52%
```

Both are poor.

---

# 12. How do you fix Underfitting?

### Answer

- Increase model complexity
- Train longer
- Add features
- Reduce regularization
- Use better algorithms

---

# 13. You have only 500 samples. What will you do?

### Answer

Options:

1. Cross Validation
2. Data Augmentation
3. Transfer Learning
4. Synthetic Data Generation

### Example

For image classification:

Use pretrained ResNet50 and fine-tune.

---

# 14. How do you handle class imbalance?

### Example

Fraud Detection

```text
Normal Transactions = 99%
Fraud Transactions = 1%
```

### Solutions

1. SMOTE
2. Oversampling
3. Undersampling
4. Class Weights
5. F1 Score instead of Accuracy

---

# 15. Why is Accuracy bad for imbalanced datasets?

### Example

```text
1000 samples

990 Normal
10 Fraud
```

Model predicts all Normal.

Accuracy:

```text
99%
```

But fraud detection is useless.

Use:

- Precision
- Recall
- F1 Score

---

# 16. A customer says your chatbot is slow. What would you investigate?

### Answer

Check:

1. PDF retrieval time
2. Embedding search time
3. LLM inference time
4. API latency
5. Network latency

### Optimizations

- Cache embeddings
- Smaller models
- Better vector DB indexing
- Parallel processing

---

# 17. What happens if chunk size is too small?

### Example

Chunk:

```text
"The employee is eligible..."
```

Missing surrounding context.

### Result

Poor retrieval quality.

---

# 18. What happens if chunk size is too large?

### Example

2000-3000 tokens per chunk.

Problems:

- More noise
- Higher cost
- Less relevant retrieval

---

# 19. Why use embeddings instead of keyword search?

### Example

User asks:

```text
How many vacation days do employees get?
```

Document says:

```text
Employees are entitled to annual leave.
```

Keyword search may fail.

Embeddings understand semantic meaning.

---

# 20. Why choose Vector Database?

### Answer

Vector DBs are optimized for similarity search.

Examples:

- FAISS
- ChromaDB
- Pinecone
- Weaviate
- Qdrant

Without vector databases, retrieval becomes very slow for large datasets.

---

# 21. Explain an ML project end-to-end.

### Answer

1. Problem Understanding
2. Data Collection
3. Data Cleaning
4. EDA
5. Feature Engineering
6. Train-Test Split
7. Model Training
8. Hyperparameter Tuning
9. Evaluation
10. Deployment
11. Monitoring

---

# 22. How do you know your model is ready for deployment?

### Answer

Checklist:

- Good validation metrics
- Stable cross-validation results
- No data leakage
- Handles edge cases
- Monitored in staging environment
- Business requirements satisfied

---

# 23. What is Data Leakage?

### Example

Predicting house prices.

Feature:

```text
Final Selling Price
```

Target:

```text
House Price
```

The model indirectly sees the answer.

Result:

Unrealistically high accuracy.

---

# 24. What would you monitor after deployment?

### Answer

1. Prediction Accuracy
2. Latency
3. Error Rate
4. Data Drift
5. Concept Drift
6. Resource Usage

---

# 25. What is Data Drift?

### Example

Training Data:

```text
Age: 20-40
```

Production Data:

```text
Age: 50-80
```

Input distribution changed.

Model performance may drop.

---

# 26. What is Concept Drift?

### Example

Customer behavior changes over time.

Relationship between features and target changes.

Old model becomes less accurate.

---

# 27. Why would you use ResNet50 instead of training a CNN from scratch?

### Answer

- Already trained on millions of images
- Faster training
- Better accuracy
- Works well with small datasets

This approach is called Transfer Learning.

---

# 28. What is the most common mistake in ML projects?

### Answer

Data Leakage.

Many models achieve:

```text
98%-99% accuracy
```

but fail in production because future information leaked into training.

---

# 29. What is your approach when model performance suddenly drops in production?

### Answer

Check:

1. Data Drift
2. Concept Drift
3. Pipeline Failures
4. Missing Features
5. Distribution Changes

Then retrain or update the model.

---

# 30. Explain your RAG project in one minute.

### Sample Answer

"I built a RAG-based chatbot where users upload PDF documents. The system extracts text, creates chunks, generates embeddings, and stores them in a vector database. When a user asks a question, relevant chunks are retrieved using similarity search and passed to an LLM along with the query. This improves accuracy, reduces hallucinations, and allows the chatbot to answer based on user-provided documents rather than relying only on the model's training data."