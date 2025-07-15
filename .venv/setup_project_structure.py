import os

# Define your folders
folders = {
    "data/incoming": None,
    "data/processed": None,
    "data/final": None,
    "etl": "__init__.py",
    "models": "__init__.py",
    "notebooks": ".keep",
    "powerbi": ".keep",
    "sql": ".keep"
}

# Gitignore content
gitignore_content = """
# Byte-compiled / cache
__pycache__/
*.py[cod]
*.pyo
*.pyd

# Virtual environments
venv/
env/
.venv/
.env/

# Jupyter Notebook checkpoints
.ipynb_checkpoints

# Data files
data/incoming/
data/processed/
data/final/

# PyCharm
.idea/

# OS files
.DS_Store
Thumbs.db
"""

# README content
readme_content = """# 🏠 Housing Price ETL & Analytics Project

This project performs an automated ETL pipeline on a housing prices dataset using:

- **Kaggle API** for data extraction
- **Pandas + PyODBC** for transformation and load
- **Microsoft SQL Server** for storage
- **Power BI** for visualization

### Structure
- `data/`: raw, processed, and final datasets
- `etl/`: Python ETL scripts for Bronze, Silver, Gold layers
- `models/`: future machine learning models
- `notebooks/`: EDA and prototyping
- `sql/`: DDL or SQL-based transformations
- `powerbi/`: BI dashboards or connector templates

> Built as a data engineering + analytics capstone.
"""

def create_project():
    print("🚀 Creating project folders and files...\n")
    for path, file in folders.items():
        os.makedirs(path, exist_ok=True)
        if file:
            with open(os.path.join(path, file), 'w') as f:
                f.write("")
        print(f"📁 Created: {path}")

    # Add .gitignore
    with open(".gitignore", "w") as f:
        f.write(gitignore_content.strip())
    print("✅ .gitignore created.")

    # Add README.md
    with open("README.md", "w", encoding="utf-8") as f:
        f.write(readme_content.strip())
    print("✅ README.md created.")

    print("\n🎯 Project is GitHub-ready!")

if __name__ == "__main__":
    create_project()
