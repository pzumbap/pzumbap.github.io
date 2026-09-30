# Resume strategy and job fit

Prepared September 29, 2026. Target confirmed by Pablo: **Data Engineer**. No target employer or individual job description was supplied. Recommendations below are an assessment of the documented experience, not an ATS score or a prediction of hiring outcomes.

## Positioning

Your strongest evidence is production data engineering since June 2023: AWS ingestion, Snowflake, dbt, orchestration, and source-to-report reconciliation. The platform you support spans **15 POS systems and variants, 50+ clients, and tens of gigabytes per day**. These are platform-scale figures you supplied; the resume does not imply that you personally built every integration or acquired those clients.

Prioritize mid-level Data Engineer openings. Some employers may consider you for senior roles, but this resume does not establish mentoring, technical leadership, organization-wide architecture ownership, or a record of independently delivered major initiatives. Data Scientist and ML Engineer are weaker targets because the documented modeling work is academic.

## Top five job titles

These are overlapping job families, ranked by how directly your experience supports them. Titles alone are unreliable; compare the actual responsibilities and required tools.

| Rank | Title | Evidence of fit | Main limitation to address |
| --- | --- | --- | --- |
| 1 | **Data Engineer / Data Engineer II** | Two Data Engineer roles; ingestion through warehouse modeling; AWS, Snowflake, dbt; production data quality and operations. | Document one delivery you owned end to end, including deployment, failure handling, and measurable impact. |
| 2 | **Analytics Engineer** | SQL, dbt, Snowflake, data modeling, and reconciliation that keeps reporting variance below 1%. | The source does not demonstrate dimensional modeling depth, semantic layers, or ownership of production BI products. |
| 3 | **ETL / ELT Developer** | Multi-source ingestion, transformation, orchestration, Python, SQL, and warehouse delivery. | Focus on modern cloud stacks; Informatica, SSIS, and Talend experience is not documented. |
| 4 | **Cloud Data Engineer — AWS** | S3, Glue, Lambda, Kinesis, EventBridge, CloudWatch, EKS, Iceberg, and Airflow are listed skills. | Infrastructure-as-code, IAM implementation, CI/CD, and cost optimization need concrete examples before becoming resume claims. |
| 5 | **Data Integration Engineer** | A platform spanning 15 POS systems and variants; multiple clients; source reconciliation and data management. | Target data pipelines rather than roles centered on Boomi, MuleSoft, Salesforce administration, or healthcare interoperability. |

The ranking is my inference from your experience. Employer descriptions provide useful comparisons: [AHEAD's Data Engineer description](https://jobs.lever.co/thinkahead/a9d8745f-8ba6-4a98-9d90-b7ed3466e032) emphasizes Snowflake/dbt and asks for 3+ years; [Axios's Analytics Engineer description](https://job-boards.greenhouse.io/axios/jobs/7799102) combines SQL/dbt with stronger BI expectations; [Point72's Data Integration Engineer description](https://job-boards.greenhouse.io/point72/jobs/7933631002) includes Python, AWS, Airflow, and SQL. These are role examples, not a vetted shortlist of openings or a finding that every requirement is met.

[TransferGo's Cloud Data Engineer description](https://job-boards.greenhouse.io/transfergo/jobs/6147020004) illustrates the additional infrastructure-as-code and CI/CD requirements common in cloud-focused roles. Its senior scope is a stretch benchmark, not a direct recommendation.

## ATS changes implemented

The PDF uses one column, selectable text, standard section names, inline job dates, and contact information in the document body. The education table was removed. Body text increased from approximately 8 points to 10 points. These choices address formatting problems identified in [Greenhouse's resume-parsing documentation](https://support.greenhouse.io/hc/en-us/articles/200989175-Unsuccessful-resume-parse).

The resume now opens with a Data Engineer headline and short summary, then professional experience. Academic work follows the paid experience and technical skills. A plain-text export uses the same source and section order for application forms.

| Keyword group | Included evidence |
| --- | --- |
| Core role | Data Engineer, data pipelines, data integration, ETL/ELT, data modeling |
| Warehouse and transformations | Snowflake, dbt, SQL, Python, PySpark |
| Cloud | Amazon Web Services (AWS), S3, Glue, Lambda, Kinesis, EventBridge, CloudWatch, EKS, Kubernetes, Apache Iceberg |
| Reliability | Apache Airflow, orchestration, event-driven pipelines, streaming, data quality, reconciliation, monitoring, DataOps |
| Domain | Point-of-sale (POS), multiple systems and clients, reporting reconciliation |
| Academic tools | Apache Spark, Databricks, SQL Server, SQLite, R, Tableau, clearly labeled as academic tools |

ETL/ELT describes the ingestion and transformation work already documented. It does not imply experience with an additional vendor product. No Terraform, Kafka, Docker, Fivetran, CI/CD, certifications, or performance savings were added without evidence.

## What was tightened or omitted

- Preserved the below-1% reporting variance and the existing 25% and 20% outcomes. Team and department outcomes are described as contributions rather than sole personal achievements.
- Removed the undefined “~83% accuracy” claim. A model result needs a named metric, evaluation method, and baseline before it can support a credible achievement.
- Omitted older, less relevant honors, publications, and web/analysis projects from the one-page application resume. They remain listed in [the evidence notes](06-evidence-notes.md).
- Kept official employment titles and dates. The target title does not change past job titles.

## Tailoring each application

Use the employer's exact role title in the headline when it accurately describes your target. Bring the relevant, already-supported tools and accomplishments forward. For an AWS role, emphasize ingestion and orchestration; for a dbt-heavy role, emphasize modeling and reconciliation. Do not copy an entire job description into the skills section.

Follow the application's required file format. Check the fields populated from the uploaded resume, especially employer names, dates, and education. Text extraction is a useful local check; it is not a test inside an employer's ATS. Neither formatting nor keyword coverage guarantees an interview.

Your next useful evidence would be one specific pipeline's runtime before/after, daily volume measured over a defined window, incident recovery time, compute cost, or manual hours saved. Keep the definition, dates, and your contribution with each metric.
