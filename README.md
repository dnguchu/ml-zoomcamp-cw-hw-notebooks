# 2026 Machine Learning Zoomcamp

Coursework, notes, homework assignments, and projects for the [Machine Learning Zoomcamp](https://github.com/DataTalksClub/machine-learning-zoomcamp) by [DataTalksClub](https://datatalks.club/).

This is my second DataTalksClub course, after completing the [Data Engineering Zoomcamp](https://github.com/DataTalksClub/data-engineering-zoomcamp) in the self-paced track.

## Setup

Requirements:

- Python 3.11 or newer
- [uv](https://docs.astral.sh/uv/getting-started/installation/)

Clone the repository, install the project dependencies, and start JupyterLab:

```bash
git clone https://github.com/dnguchu/ml-zoomcamp-cw-hw-notebooks.git
cd ml-zoomcamp-cw-hw-notebooks
uv sync
source .venv/bin/activate
jupyter lab
```

Open a notebook from the relevant module directory and run its cells. The notebooks download or use the datasets stored alongside them.

## Repository Structure

The repository follows the module structure of the [Machine Learning Zoomcamp](https://github.com/DataTalksClub/machine-learning-zoomcamp):

```text
.
├── M1: Intro to Machine Learning/
│   ├── data.csv
│   └── homework.ipynb
├── M2: Regression/
│   ├── Classwork/
│   │   └── car_price_prediction.ipynb
│   └── Homework/
│       ├── data.csv
│       └── homework.ipynb
├── src/
│   └── ml_zoomcamp_cw_hw_notebooks/
│       └── __init__.py
├── .python-version
├── pyproject.toml
├── README.md
└── uv.lock
```

- `M1` contains introductory machine learning exercises.
- `M2` contains regression classwork and homework.
- `src` contains the installable Python package for the repository.

