# Ecommerce Analytics Platform

A portfolio project demonstrating how an ecommerce organization can unify commerce, marketing, and web-analytics data into trusted executive decision support.

## Business questions

- What is driving revenue, margin, conversion, and customer retention?
- Which channels and campaigns create profitable demand?
- Where do marketing, ecommerce, and reporting numbers disagree?

## Data sources

- Commerce data: [Olist Brazilian E-Commerce Public Dataset](https://www.kaggle.com/olistbr/brazilian-ecommerce/home) — public, anonymized order, customer, product, payment, seller, delivery, and review data.
- Synthetic data: marketing spend and web-session files generated for demonstration.
- Optional GA4 reference: Google’s public GA4 BigQuery ecommerce sample.

No employer, client, customer, or proprietary data is included.

## Target architecture

Public and synthetic sources → ingestion → raw layer → modeled commerce and marketing marts → executive KPI layer

## Planned analytical products

- Revenue, margin, AOV, and product performance
- Customer acquisition, repeat purchase, retention, and LTV
- Marketing spend, CAC, and ROAS
- Conversion funnel and data-quality reconciliation

## Repository structure

- data: local or generated data; source data is not republished here
- python: synthetic-data generation and analysis helpers
- sql: staging, intermediate, and mart models
- docs: data model and architecture notes

## Getting started

1. Download the public Olist dataset from its source and review its terms.
2. Generate the synthetic marketing and web-session data.
3. Load the files into a local warehouse or BigQuery/Snowflake sandbox.
4. Build the models and KPI layer.

This project is for public portfolio demonstration only.
