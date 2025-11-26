Directory structure for project setup

aws-data-platform/
│
├── ingestion/
│   ├── kinesis_stream_setup.py
│   ├── lambda_processor.py
│   └── firehose_to_s3_delivery_config.json
│
├── emr/
│   ├── bootstrap.sh
│   ├── spark_app/
│   │   ├── config.yaml
│   │   ├── main_etl.py
│   │   └── utils.py
│   └── emr_cluster_config.json
│
├── glue/
│   ├── glue_job_script.py
│   └── glue_catalog_setup.py
│
├── orchestration/
│   ├── mwaa_dag.py
│   └── step_function_state_machine.json
│
├── dq_framework/
│   ├── dq_rules.yaml
│   ├── dq_runner.py
│   └── metrics_publisher.py
│
├── architecture/
│   ├── data_platform_aws.drawio
│   └── README.md
│
└── README.md
