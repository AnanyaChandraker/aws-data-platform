Data platform architecture notes.
Layers:
- Raw: immutable landing zone (S3)
- Processed: normalized parquet datasets
- Curated: business-ready tables
Security:
- Use Lake Formation and IAM for fine-grained access
Observability:
- CloudWatch, Spark UI, EMR logs, OpenSearch for logs
