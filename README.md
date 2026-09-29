# Object_Annotation

# 🚗 Vehicle Object Annotation & Automated Quality Assurance

A structured **vehicle object annotation and annotation-quality-assurance project** based on the YOLO annotation format. The project contains a labeled vehicle dataset, class definitions, training-image configuration, and a Python-based automated QA pipeline for validating annotation files and generating dataset statistics.

## 📌 Project Overview

This project focuses on preparing and validating an object-detection dataset containing different types of vehicles.

The dataset uses **YOLO-format annotations**, where each annotated object is represented using:

```text
<class_id> <x_center> <y_center> <width> <height>
```

An automated Python quality-assurance script checks the annotation files for common technical issues such as invalid YOLO formatting, invalid numeric values, unsupported class IDs, out-of-range coordinates, empty annotation files, and invalid bounding-box dimensions.

The validation results and dataset statistics are exported to Excel files for further inspection and reporting.

---

## 🎯 Objectives

* Create a structured vehicle object-detection dataset.
* Maintain annotations in YOLO format.
* Define and organize multiple vehicle classes.
* Validate annotation files automatically.
* Detect malformed or technically invalid annotations.
* Generate dataset-level statistics.
* Export QA results into Excel for review.
* Prepare a clean dataset for downstream object-detection workflows.

---

## 📊 Dataset Summary

| Metric                  | Value |
| ----------------------- | ----: |
| Total Images            |    66 |
| Total Annotated Objects |   644 |
| Number of Classes       |     6 |
| Annotation Format       |  YOLO |

### Vehicle Classes

| Class ID | Class  |
| -------: | ------ |
|        0 | Car    |
|        1 | Cycle  |
|        2 | Truck  |
|        3 | Bike   |
|        4 | Scooty |
|        5 | Auto   |

The class mapping is explicitly defined in the QA pipeline and corresponds to the project's `.names` configuration.

### Class Distribution

| Class     | Objects |
| --------- | ------: |
| Car       |     596 |
| Cycle     |      12 |
| Truck     |       6 |
| Bike      |      20 |
| Scooty    |       8 |
| Auto      |       2 |
| **Total** | **644** |

---

## 🗂️ Project Structure

```text
Object_Annotation/
│
├── data/
│   ├── obj_train_data/
│   │   ├── *.jpg
│   │   ├── *.png
│   │   └── *.avif
│   │
│   ├── obj.names
│   └── train.txt
│
├── backup/
│
├── Automatic_QA.py
├── annotation_qa.xlsx
├── dataset_statistics.xlsx
├── obj.data
└── README.md
```

The training configuration points to `data/train.txt`, defines six classes, references the class-name file, and specifies a backup directory.

The training list contains the dataset image paths under `data/obj_train_data/`.

---

## 🔍 YOLO Annotation Format

Each annotation file follows the YOLO object-detection structure:

```text
class_id x_center y_center width height
```

For example:

```text
0 0.512 0.438 0.245 0.312
```

Where:

* `class_id` — Numeric identifier of the vehicle class.
* `x_center` — Normalized horizontal center coordinate.
* `y_center` — Normalized vertical center coordinate.
* `width` — Normalized bounding-box width.
* `height` — Normalized bounding-box height.

The QA script verifies that each annotation contains exactly five values before processing the annotation further.

---

# 🧪 Automated Annotation Quality Assurance

The project includes `Automatic_QA.py`, a Python script developed to automatically inspect YOLO annotation files.

### QA Workflow

```text
YOLO Annotation Files
        │
        ▼
Read Annotation Files
        │
        ▼
Validate Annotation Format
        │
        ▼
Validate Numeric Values
        │
        ▼
Validate Class IDs
        │
        ▼
Validate Coordinates
        │
        ▼
Validate Bounding Boxes
        │
        ▼
Generate QA Results
        │
        ├──────────────► annotation_qa.xlsx
        │
        └──────────────► dataset_statistics.xlsx
```

## ✅ Validation Checks

The QA system performs the following checks:

### 1. Empty Annotation Check

Detects annotation files that contain no objects and marks them as:

```text
Empty Annotation
Needs Review
```

The recommended correction is to add the required object annotations.

### 2. YOLO Format Validation

Checks whether every annotation contains exactly five values:

```text
class_id x_center y_center width height
```

Invalid records are reported as `Invalid Format`.

### 3. Numeric Value Validation

The script attempts to convert class IDs and bounding-box values into numeric types. Non-numeric values are reported as `Invalid Number`.

### 4. Class ID Validation

Only the configured class IDs from `0` to `5` are accepted.

Invalid class IDs are reported as:

```text
Invalid Class
```

and marked for review.

### 5. Coordinate Validation

The script verifies that normalized bounding-box values remain within the range:

```text
0 ≤ value ≤ 1
```

This validation is applied to the center coordinates, width, and height.

### 6. Bounding-Box Validation

Bounding-box width and height must be greater than zero.

Invalid dimensions are reported as:

```text
Invalid Bounding Box
```

## with the recommendation to set positive width and height values.

# 📈 Quality Assurance Results

The generated QA report contains:

* Image ID
* Object ID
* Issue Type
* Description
* Correction
* Status

The current QA output contains **644 annotation records**, all marked:

```text
Passed
```

The script assigns `Passed` when the annotation has valid coordinates and a positive bounding-box size.

### Current QA Summary

| QA Metric                  | Result |
| -------------------------- | -----: |
| Annotation Records Checked |    644 |
| Passed                     |    644 |
| Needs Review               |      0 |

> **Note:** The QA process validates the technical structure of the annotation files. It does not independently determine whether a bounding box is visually correct for the object in the image.

---

# 📊 Dataset Statistics

The `Automatic_QA.py` script generates `dataset_statistics.xlsx` containing:

* Total Images
* Total Objects
* Per-class object counts

The statistics are calculated programmatically from the processed annotation files.

The generated report contains:

```text
Total Images: 66
Total Objects: 644

Car: 596
Cycle: 12
Truck: 6
Bike: 20
Scooty: 8
Auto: 2
```

---

# 🛠️ Technologies Used

* **Python**
* **Pandas**
* **Excel / XLSX**
* **YOLO Annotation Format**
* **Object Detection Dataset Preparation**
* **Automated Data Quality Assurance**

## The QA script uses Python's `pathlib` for file handling and Pandas for creating the QA and statistics dataframes and exporting them to Excel.

# ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/kirthi953/Object_Annotation.git
```

Navigate into the project:

```bash
cd Object_Annotation
```

Install the required Python dependency:

```bash
pip install pandas openpyxl
```

---

# ▶️ Running the QA Pipeline

Before running the script, update the annotation-folder path in:

```text
Automatic_QA.py
```

The current script uses a local annotation directory:

```python
labels_folder = Path("C:/Users/keert/Downloads/Bounded_Vehicles/labels/obj_train_data")
```

For a different environment, replace this with the appropriate dataset annotation path.

Run:

```bash
python Automatic_QA.py
```

The script will:

1. Locate the annotation files.
2. Read each YOLO annotation.
3. Validate annotation structure.
4. Validate numeric values.
5. Validate class IDs.
6. Validate normalized coordinates.
7. Validate bounding-box dimensions.
8. Calculate class statistics.
9. Generate the QA report.
10. Generate the dataset statistics report.

---

# 📁 Generated Reports

### `annotation_qa.xlsx`

Contains object-level QA results:

```text
Image ID
Object ID
Issue Type
Description
Correction
Status
```

### `dataset_statistics.xlsx`

Contains dataset-level statistics:

```text
Metric
Value
```

## The script explicitly writes both reports to Excel after completing the annotation checks.

# 🚀 Potential Applications

This dataset and validation workflow can support future computer-vision applications such as:

* Vehicle detection
* Traffic monitoring
* Road-scene analysis
* Vehicle classification
* Intelligent transportation systems
* Traffic analytics
* Computer-vision model training

These represent potential downstream uses of the annotated dataset rather than functionality implemented directly by the current repository.

---

# 🔮 Future Improvements

Potential extensions to the project include:

* Add automated image-to-label consistency checks.
* Visualize bounding boxes directly on images.
* Add duplicate annotation detection.
* Detect overlapping or suspicious bounding boxes.
* Generate class-distribution charts.
* Add dataset train/validation/test splitting.
* Add automated annotation summaries.
* Integrate YOLO model training and evaluation.
* Add precision, recall, mAP, and confusion-matrix reporting.
* Improve the QA pipeline with configurable dataset paths.
* Add command-line arguments instead of hard-coded paths.
* Add automated tests for the QA functions.
* Integrate the QA process into a CI/CD workflow.

---

# 📌 Key Features

| Feature                 | Description                              |
| ----------------------- | ---------------------------------------- |
| YOLO Annotations        | Structured object-detection labels       |
| 6 Vehicle Classes       | Car, Cycle, Truck, Bike, Scooty, Auto    |
| Automated QA            | Programmatic annotation validation       |
| Format Checking         | Validates five-value YOLO records        |
| Class Validation        | Detects unsupported class IDs            |
| Coordinate Validation   | Checks normalized values                 |
| Bounding-Box Validation | Checks positive dimensions               |
| Excel Reporting         | Generates QA and statistics reports      |
| Dataset Statistics      | Provides image, object, and class counts |

---

# 👩‍💻 Project Purpose

The primary purpose of this project is to demonstrate a **systematic approach to preparing and validating an object-detection dataset**. Instead of relying only on manual inspection, the project introduces an automated quality-assurance process that identifies technical annotation problems and produces structured reports for dataset review.

---


# ⭐ Acknowledgement

This project demonstrates practical skills in:

**Python • Data Validation • Object Detection • YOLO Annotation • Dataset Preparation • Quality Assurance • Data Analysis • Excel Reporting**
