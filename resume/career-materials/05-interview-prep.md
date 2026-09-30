# Data Engineer interview preparation

Ten likely questions, tailored to AWS, Snowflake, dbt, and multi-source POS data. Answers use **Situation, Task, Action, Result (STAR)** and are intended for roughly 45–90 seconds of delivery.

Questions 1–5 use documented experience at the level of detail currently available. Questions 6–10 are explicitly hypothetical technical scenarios: their results are acceptance criteria, not achievements being claimed. For a question asking what you actually did, use a real incident and replace the scenario with its verified actions and outcome. Do not turn “I would” into “I did” without evidence.

## 1. Walk me through a data pipeline you build or maintain.

**Evidence-based answer**

**S:** At CDAI, I work on a POS data platform serving 50+ clients across 15 systems and variants, processing tens of gigabytes daily. **T:** My work is to build and maintain pipelines that make this data usable for analytics and data science. **A:** I connect AWS ingestion with Snowflake warehousing and dbt transformations, and support the surrounding orchestration and operations. **R:** The platform supports those clients and volumes, while my reconciliation work maintains reporting variance below 1% against POS portals.

Be ready to draw one actual integration and identify your contribution, the services it uses, its refresh schedule, and where failures are handled. The scope above describes the platform, not one pipeline.

## 2. How do you know your pipeline's output is correct?

**Evidence-based answer**

**S:** Our POS pipelines feed reporting, so successful execution alone does not establish that the output matches the source. **T:** I need to validate pipeline outputs against POS reporting portals. **A:** I reconcile the resulting data with those source reports as part of my data-quality work. **R:** The documented outcome is reporting variance below 1%. That is a reconciliation measure; I would not describe it as a guarantee that every field or record is correct.

Prepare the exact metric definition: which totals are compared, the denominator, date window, treatment of refunds/taxes, and whether the threshold is per client or aggregate. Those details were not supplied. Do not invent them.

## 3. Tell me about your experience supporting the full data lifecycle.

**Evidence-based answer**

**S:** At E15 Group, my work supported analytics and data science use cases. **T:** I needed to contribute across the pipeline lifecycle, including the systems required to operate it. **A:** I built and maintained pipelines and developed ingestion, data models, orchestration, and infrastructure, with security and data management considered in ongoing operations. **R:** I helped provide a maintained data foundation for analytics and data science, with responsibilities spanning ingestion through ongoing operations.

Strengthen this answer with one specific implementation and its observable outcome. No measured cost or runtime improvement for E15 was supplied.

## 4. Tell me about a database you designed.

**Evidence-based answer — academic project**

**S:** In an academic project, I worked on a database for an inmate reintegration program. **T:** I needed to design and implement a relational database for that use case. **A:** I used draw.io for the database design and Microsoft SQL Server for implementation. **R:** I produced a SQL Server database implementation and gained hands-on experience with relational modeling that I later applied professionally.

Bring the actual diagram. Explain the real entities, grain, relationships, and one design tradeoff from the project; these details are not established by the resume alone.

## 5. Describe a measurable operational improvement you contributed to.

**Evidence-based answer**

**S:** At Crothall Healthcare, I supported the Clinical Engineering department's maintenance work. **T:** My responsibilities included preventive maintenance on Stryker ICU beds and stretchers and tracking work orders and incidents. **A:** I supported the maintenance work and monitored and analyzed records in CMMS software. **R:** My preventive-maintenance work contributed to a 25% improvement in the department KPI. I describe that as a contribution to a department result, not an improvement I delivered alone.

Know the KPI's actual name, baseline, and measurement period before using the percentage in an interview. If you cannot explain the measure, describe the contribution without the percentage.

## 6. How would you onboard a POS source with a different schema?

**Hypothetical design scenario**

**S:** Suppose a new POS vendor reports orders, payments, and refunds differently from the existing feeds. **T:** I would need to integrate it without changing the meaning of existing reports. **A:** I would agree on each dataset's grain and metric definitions, preserve the raw input, and map vendor fields into source-specific staging models before shared transformations. I would test representative edge cases and reconcile a bounded period with the source portal. **R:** I would consider onboarding complete when keys, relationships, totals, and agreed freshness requirements pass validation; I would not promise zero discrepancies before testing.

## 7. How would you handle duplicate deliveries and late-arriving records?

**Hypothetical design scenario**

**S:** Suppose source retries resend transactions and corrections arrive after the first load. **T:** I would need reruns to preserve correct totals while accepting legitimate changes. **A:** I would use stable source identifiers, deterministic deduplication, and an update-aware incremental strategy. I would test uniqueness and null keys, then use a source-informed lookback or change tracking, with a backfill path for older corrections. **R:** Success means rerunning identical input adds no duplicates and a late correction updates the intended record without dropping unrelated history.

AWS recommends idempotent handling of duplicate events. dbt's incremental behavior depends on the adapter, strategy, filter, and key configuration; a `unique_key` setting alone does not validate uniqueness. [AWS Lambda guidance](https://docs.aws.amazon.com/lambda/latest/dg/best-practices.html), [dbt incremental models](https://docs.getdbt.com/docs/build/incremental-models).

## 8. A SQL join doubles reported sales. How would you investigate?

**Hypothetical debugging scenario**

**S:** Suppose sales totals increase unexpectedly after orders are joined with payment data. **T:** I would need to find and correct the multiplication without discarding legitimate rows. **A:** I would compare counts and totals before and after the join, check key uniqueness, and inspect the cardinality. If an order has multiple payments, I would aggregate each side to the intended reporting grain or model the relationship explicitly. I would add key and reconciliation checks. **R:** The corrected output should match the intended grain and source totals; a blanket `DISTINCT` would not establish correctness.

dbt supplies tests for uniqueness, nulls, relationships, and accepted values; reconciliation still needs checks specific to the business measure. [dbt data tests](https://docs.getdbt.com/docs/build/data-tests).

## 9. A daily pipeline fails before a reporting deadline. What would you do?

**Hypothetical incident scenario**

**S:** Suppose a failed load leaves a report incomplete near its deadline. **T:** I would need to establish impact, restore trustworthy data, and keep affected users informed. **A:** I would identify the failed stage and affected sources and dates, inspect logs and the last successful run, and communicate the known scope. After fixing the cause, I would replay the affected input with duplicate-safe handling, reconcile the output, and record the cause and prevention work. **R:** Recovery means both the data and its freshness pass validation, with users told when the report is usable again.

For a past-incident question, choose a real failure. Do not invent an outage duration, recovery time, alert, or postmortem you have not actually handled.

## 10. How would you improve pipeline performance or reduce cost?

**Hypothetical optimization scenario**

**S:** Suppose daily data growth makes a warehouse transformation slower or more expensive. **T:** I would need to improve the limiting stage while preserving output correctness. **A:** I would establish runtime and cost baselines and inspect the query plan and scanned data. Depending on the bottleneck, I would test narrower inputs, corrected joins, or incremental processing with a safe path for historical changes. I would compare output keys and business totals with the baseline. **R:** I would report the measured change in runtime and cost only after correctness and freshness checks pass.

Incremental processing can avoid rebuilding all history, but its filtering and update strategy must reflect how the source changes. [dbt incremental models](https://docs.getdbt.com/docs/build/incremental-models).

## Preparation priorities

The largest interview gap is detailed evidence, not additional tool names. Prepare one architecture diagram, one reconciliation example, one production incident, and one modeling decision. For each, record the specific problem, your contribution, tradeoffs, and result. Keep client details anonymized when discussing examples publicly.

Useful questions for the interviewer: Which sources create the most reconciliation work? How are freshness and correctness measured? What does a Data Engineer own after deployment? What would successful delivery look like in the first 90 days?
