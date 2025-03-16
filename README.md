# Latex Equation Parser

We have developed a **math equation parser** that extracts equations written in LaTeX format directly from document-sized images. Unlike traditional pipelines that involve multiple stages (equation detection followed by OCR extraction), our approach uses an **End-to-End model** to detect and extract equations in a **single step**, eliminating the risk of module-to-module error propagation.

We have fine-tuned and optimized the **Vision-to-Text DONUT model** specifically for this task.  
**Training, evaluation codes, and the MathVQA dataset** are available in our other repository (link below).  
This repository focuses on providing:

- **Inference code wrapped in a REST API using Flask**
- **Containerized Docker image for deployment**
- **Sample test images & outputs for demonstration**

---

## Techniques & Tools Used

- **Computer Vision (Visual Document Understanding)**
- **OCR-Free Equation Extraction**
- **Vision-to-Text Transformer (DONUT model)**
- **REST API (Flask)**
- **Docker Containerization**

---

## Repository Contents

| File/Folder        | Purpose                                                    |
|--------------------|------------------------------------------------------------|
| `app.py`           | Flask API to serve model inference                          |
| `requirements.txt` | Python dependencies                                        |
| `Dockerfile`       | Dockerfile for building the container                       |
| `samples/`         | Example input images and corresponding LaTeX outputs        |
| `Inferences/`       | Have the inferences for the project (model output)         |
| `README.md`        | Project documentation                                      |
| `.dockerignore`    | Prevent unnecessary files in Docker image                  |

---

## Quick Start

### 1. Clone the Repository:
```bash
git clone https://github.com/yourusername/latex-equation-parser.git
cd latex-equation-parser
