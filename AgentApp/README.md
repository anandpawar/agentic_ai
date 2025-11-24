# Crewai Top5 Papers

Production-ready multi-agent blueprint to fetch top-5 AI/ML/GenAI research papers, summarize and present them.

Included:
- FastAPI backend (backend/app)
- MCP microservice for external API adapters (mcp)
- ChromaDB adapter and sentence-transformers embeddings
- Angular frontend scaffold (minimal)
- Docker Compose for local dev
- Evaluation plan (docs/evaluation.md)

See .env.example for required environment variables.

Quickstart:
1. Copy `.env.example` to `.env` and fill keys.
2. `docker-compose up --build`
3. Backend: http://localhost:8000/docs
4. Frontend: http://localhost:4200 (if you run `npm install` and `ng serve` in frontend)

Evaluation:

# Evaluation Framework for Top-5 Research Paper Retrieval System

This document describes a complete, production-grade evaluation methodology for the multi-agent architecture that retrieves, ranks, summarizes, and outputs Top-5 AI/ML/GenAI research papers.

---

# 1. Overview

Evaluating the system requires assessing multiple layers:

1. Retrieval Quality (SearchAgent + MCP Server)
2. Semantic Ranking Quality (RankAgent)
3. Summarization Quality (SummarizeAgent)
4. End-to-End Agent Performance
5. Vector Database (ChromaDB) Performance
6. System-Level KPIs (Latency, availability, cost)

Each layer is tested using metrics, tools, and benchmark datasets.

---

# 2. Retrieval Quality Evaluation

## 2.1 Metrics

* **Recall@N**: Measures whether the system retrieves known relevant papers.
* **Coverage**: Number of papers retrieved per source.
* **API Reliability**: Error rates from MCP-arXiv and MCP-Semantic Scholar.
* **Freshness**: Are newly published papers included?

## 2.2 Method

* Construct a benchmark dataset of 10–20 AI/ML topics.
* For each topic, compile a small list of authoritative papers.
* Run system searches and calculate Recall@20.

---

# 3. Ranking Quality Evaluation (Semantic Similarity)

## 3.1 Metrics

* **nDCG@5**: Normalized Discounted Cumulative Gain.
* **MAP@5**: Mean Average Precision.
* **MRR**: Mean Reciprocal Rank.
* **Embedding Model Latency**: Speed per embedding.

## 3.2 Method

* Create gold-standard ranking for each topic.
* Compare system ranking vs. gold ranking using IR metrics.

## 3.3 Embedding Model Comparisons

Evaluate candidates:

* all-MiniLM-L6-v2
* BAAI/bge-small-en
* gte-small

Measure:

* accuracy (nDCG)
* latency
* memory footprint

---

# 4. Summarization Quality Evaluation

## 4.1 Evaluation Methods

### LLM-as-a-Judge (Automated)

Use an LLM to evaluate summaries based on:

* Accuracy
* Faithfulness to the abstract
* Completeness
* Readability
* Hallucination risk

### Human Evaluation

Experts rate summaries on the same axes.

## 4.2 Metrics

* Average score per dimension (1–10)
* Hallucination percentage (LLM-detected)
* Readability score (LLM)

---

# 5. End-to-End Pipeline Evaluation

## 5.1 Metrics

* **End-to-End Relevance Score (E2E-RS)**: Human rating of the final Top-5 list.
* **Consistency Score**: Jaccard similarity across repeated runs of same query.
* **End-to-End Latency**: Time from request to response.
* **Pipeline Failure Rate**: Errors per 100 queries.

## 5.2 Methods

* Run each benchmark query multiple times.
* Compute stability of final results.

---

# 6. ChromaDB Evaluation

## Metrics

* **Insert Latency**
* **Query Latency (kNN)**
* **Cosine Accuracy**: Compare vs. offline numpy cosine.
* **Index Size**

## Method

Benchmark storing and querying embeddings for 500–5,000 research papers.

---

# 7. System-Level Evaluation

## 7.1 Latency Breakdown

Measure:

* MCP retrieval time
* Embedding time
* Rank computation time
* LLM summarization time
* Total request time

## 7.2 Availability & Reliability

* Uptime %
* MCP external API failure fallback behavior

## 7.3 Cost Metrics

Track tokens per summary.

Formulas:

```
Cost per query = (input_tokens + output_tokens) * model_price_per_token
```

---

# 8. Tools & Evaluation Frameworks

| Tool                         | Purpose                       |
| ---------------------------- | ----------------------------- |
| Locust                       | Load testing                  |
| k6                           | API-level performance testing |
| OpenAI evals / LiteLLM evals | LLM evaluation                |
| pytest                       | Unit testing for agents       |
| Jupyter                      | Calculating nDCG/MAP/MRR      |
| Prometheus + Grafana         | System metrics dashboards     |
| Weights & Biases             | Experiment tracking           |

---

# 9. Benchmark Dataset Construction

A recommended dataset:

### Example Topics

* Large Language Model Efficiency
* Transformer Architectures
* Vector Databases
* Diffusion Models
* Responsible AI
* Reinforcement Learning
* Self-Supervised Learning
* Retrieval-Augmented Generation
* Multi-Agent Systems
* Graph Neural Networks

For each, prepare:

* Gold standard relevant papers
* High-quality human-curated ranking (optional)

---

# 10. Evaluation Automation Scripts

Recommended scripts to include:

* `scripts/eval_retrieval.py`
* `scripts/eval_ranking.py`
* `scripts/eval_summary_quality.py`
* `scripts/eval_end_to_end.py`

These can be integrated with CI.

---

# 11. Reporting

Generate:

* Evaluation CSV metrics
* Summary charts
* Leaderboards of embedding models
* LLM summary quality statistics
* Latency distribution graphs

---

# 12. Conclusions

This evaluation suite ensures:

* High-quality retrieval
* Strong ranking performance
* Faithful, readable summaries
* Stable agent pipeline
* Measurable cost and latency

A complete evaluation gives clear visibility into system accuracy, robustness, and production readiness.


