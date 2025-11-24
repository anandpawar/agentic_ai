# Evaluation Plan

Metrics:
- Precision@5 and nDCG@5 against a curated ground-truth set.
- Mean Average Precision (MAP)
- Summary quality: ROUGE-L and BERTScore vs human-written summaries.
- Latency: p50, p95 end-to-end and per-agent.
- Cost: LLM token usage, embedder compute hours.

Procedure:
1. Create a dataset of 50 topics with human-curated top papers (ground truth).
2. Run the pipeline for each topic, collect top-5.
3. Compute Precision@5 and nDCG@5.
4. Ask human annotators to rate 100 random summaries for factuality and usefulness (1-5).
5. A/B test: change embedding model or ranking formula and compare metrics.

Instrumentation:
- Export Prometheus metrics from FastAPI endpoints and individual agent durations.
- Log token usage from the LLM provider for cost estimates.

