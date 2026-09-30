# Object_Annotation


#  Object Annotation & Automated Quality Assurance

A structured **vehicle object-annotation and dataset quality-assurance project** built around the **YOLO object-detection annotation format**.

The project focuses on preparing a multi-class vehicle dataset, validating annotation files programmatically, generating dataset statistics, and maintaining a reproducible annotation workflow using **CVAT**.

---

##  Project Overview

Object detection depends heavily on the quality and consistency of training annotations. This project provides a structured workflow for preparing and validating vehicle annotations before they are used for downstream computer-vision model development.

The dataset contains six vehicle categories:

*  **Car**
*  **Cycle**
*  **Truck**
*  **Bike**
*  **Scooty**
*  **Auto**

Annotations are maintained in **YOLO format**, while `Automatic_QA.py` performs automated technical validation and generates Excel-based reports for annotation quality and dataset statistics.

> **Scope:** The current repository primarily covers dataset annotation, annotation validation, and reporting. Model training and inference are potential future extensions.

---

##  Objectives

* Prepare a structured vehicle object-detection dataset.
* Maintain annotations using the YOLO format.
* Use consistent class IDs across the dataset.
* Automatically identify technically invalid annotations.
* Validate annotation structure, coordinates, class IDs, and bounding-box dimensions.
* Generate object-level QA reports.
* Generate dataset-level statistics.
* Provide sample dataset images and a CVAT annotation reference.
* Establish a reusable foundation for future object-detection model training.

---

##  Dataset Summary

| Metric                      | Value |
| --------------------------- | ----: |
| **Total Images**            |    66 |
| **Total Annotated Objects** |   644 |
| **Number of Classes**       |     6 |
| **Annotation Format**       |  YOLO |

### Class Mapping

| Class ID | Vehicle Class |
| -------: | ------------- |
|        0 | Car           |
|        1 | Cycle         |
|        2 | Truck         |
|        3 | Bike          |
|        4 | Scooty        |
|        5 | Auto          |

The class mapping is defined in the project's class-name configuration and is used by the QA pipeline.

---

##  Project Workflow

```text
                Vehicle Images
                       │
                       ▼
              CVAT Annotation
                       │
                       ▼
             YOLO Label Files
                       │
                       ▼
             Automated QA Script
                       │
          ┌────────────┼────────────┐
          ▼            ▼            ▼
      Format       Class ID      Bounding Box
      Checks        Checks          Checks
          │            │            │
          └────────────┼────────────┘
                       ▼
                Validation Results
                       │
              ┌────────┴────────┐
              ▼                 ▼
     annotation_qa.xlsx   dataset_statistics.xlsx
```

---

##  Project Structure

```text
Object_Annotation/
│
├── data/
│   ├── obj_train_data/
│   │   ├── image files
│   │   └── annotation files
│   │
│   ├── obj.names
│   └── train.txt
│
├── backup/
│
├── images/
│   ├── 15.jpg
│   ├── 16.jpg
│   ├── 17.jpg
│   ├── 18.jpg
│   ├── 19.jpg
│   ├── 20.jpg
│   ├── 21.jpg
│   └── 22.jpg
│
├── Automatic_QA.py
├── annotation_qa.xlsx
├── dataset_statistics.xlsx
├── obj.data
└── README.md
```

---

#  YOLO Annotation Format

Each object is represented using five values:

```text
<class_id> <x_center> <y_center> <width> <height>
```

### Example

```text
0 0.512 0.438 0.245 0.312
```

### Fields

| Field      | Description                              |
| ---------- | ---------------------------------------- |
| `class_id` | Numeric ID representing the object class |
| `x_center` | Normalized horizontal center coordinate  |
| `y_center` | Normalized vertical center coordinate    |
| `width`    | Normalized bounding-box width            |
| `height`   | Normalized bounding-box height           |

The coordinate and bounding-box values are expected to be normalized between **0 and 1**.

---

#  Automated Annotation Quality Assurance

The project includes `Automatic_QA.py`, a Python-based validation pipeline designed to identify common technical issues in YOLO annotation files.

## QA Checks

### 1. Empty Annotation Check

Detects annotation files that contain no object records.

### 2. YOLO Format Check

Ensures that each annotation contains exactly five values:

```text
class_id x_center y_center width height
```

### 3. Numeric Validation

Checks whether class IDs and bounding-box values contain valid numeric values.

### 4. Class ID Validation

Checks whether the class ID belongs to the configured class range:

```text
0 – 5
```

### 5. Coordinate Validation

Checks whether normalized coordinates and bounding-box values remain within:

```text
0 ≤ value ≤ 1
```

### 6. Bounding-Box Validation

Checks that bounding-box width and height are greater than zero.

---

#  Annotation QA Report

The generated `annotation_qa.xlsx` file provides object-level validation results.

### Report Fields

| Field           | Description                        |
| --------------- | ---------------------------------- |
| **Image ID**    | Source image identifier            |
| **Object ID**   | Object number within an annotation |
| **Issue Type**  | Type of detected issue             |
| **Description** | Explanation of the issue           |
| **Correction**  | Suggested correction               |
| **Status**      | Validation result                  |

Typical status values are:

```text
Passed
Needs Review
```

A `Passed` result means that the annotation satisfied the technical validation rules implemented in the script.

> **Important:** Technical QA does not independently verify whether a bounding box is visually positioned around the correct object. Visual annotation review is still required for semantic correctness.

---

#  Dataset Statistics

The `dataset_statistics.xlsx` report provides a high-level summary of the dataset, including:

* Total number of images
* Total number of annotated objects
* Object counts by vehicle class

### Current Dataset Distribution

| Vehicle Class | Objects |
| ------------- | ------: |
| Car           |     596 |
| Cycle         |      12 |
| Truck         |       6 |
| Bike          |      20 |
| Scooty        |       8 |
| Auto          |       2 |
| **Total**     | **644** |

---

#  Sample Dataset Images

The repository includes sample images representing the type of vehicle content used in the annotation dataset.

### Sample 15

### Sample 16

### Sample 17

### Sample 18

### Sample 19

### Sample 20

### Sample 21

### Sample 22

> These images are included as dataset samples. They should not be interpreted as model predictions unless prediction bounding boxes are explicitly displayed.

---

#  CVAT Annotation Workflow

The annotation workflow is associated with a **CVAT** job used for creating and managing object annotations.

**CVAT Annotation Job:**

[Open CVAT Annotation Job](https://app.cvat.ai/auth/login?next=/tasks/2624513/jobs/4516329)

CVAT provides the annotation environment, while the Python QA pipeline performs automated technical validation of the resulting label files.

---

# Installation

## 1. Clone the Repository

```bash
git clone https://github.com/kirthi953/Object_Annotation.git
cd Object_Annotation
```

## 2. Install Dependencies

```bash
pip install pandas openpyxl
```

### Requirements

```text
Python 3.x
pandas
openpyxl
```

### Is Pillow Required?

**No.**

The current `Automatic_QA.py` script does not open, resize, process, or manipulate images, so **Pillow is not required**.

---

#  Running the QA Pipeline

Before execution, update the annotation-folder path in `Automatic_QA.py` if the dataset is stored in a different location.

Run:

```bash
python Automatic_QA.py
```

### Processing Flow

The script:

1. Locates annotation files.
2. Reads YOLO annotation records.
3. Validates annotation structure.
4. Validates numeric values.
5. Validates class IDs.
6. Validates normalized coordinates.
7. Validates bounding-box dimensions.
8. Calculates dataset statistics.
9. Generates the annotation QA report.
10. Generates the dataset statistics report.

---

#  Generated Reports

## `annotation_qa.xlsx`

Contains object-level annotation validation results.

## `dataset_statistics.xlsx`

Contains dataset-level statistics and class counts.

These reports make it easier to review annotation quality and understand the composition of the dataset.

---

#  Technologies Used

| Technology      | Purpose                                     |
| --------------- | ------------------------------------------- |
| **Python**      | QA automation and dataset processing        |
| **Pandas**      | Data processing and Excel report generation |
| **OpenPyXL**    | XLSX file support                           |
| **YOLO Format** | Object-detection annotation structure       |
| **CVAT**        | Image annotation workflow                   |
| **Excel/XLSX**  | QA and statistics reporting                 |

---

#  Potential Applications

The prepared dataset can serve as a foundation for future computer-vision applications such as:

* Vehicle detection
* Vehicle classification
* Traffic monitoring
* Road-scene analysis
* Traffic analytics
* Intelligent transportation systems
* Object-detection model training

> These represent potential downstream applications; the current repository focuses on annotation and annotation quality assurance.

---

#  Future Enhancements

Possible improvements include:

* Visual bounding-box verification
* Image-to-label consistency checks
* Duplicate annotation detection
* Overlapping or suspicious bounding-box detection
* Class-distribution visualization
* Automated train/validation/test splitting
* YOLO model training integration
* Model evaluation using precision, recall, and mAP
* Confusion-matrix generation
* Configurable dataset paths through command-line arguments
* Automated unit tests
* CI/CD-based annotation QA

---

#  Key Features

| Feature                     | Description                               |
| --------------------------- | ----------------------------------------- |
| **YOLO Annotations**        | Standard object-detection label structure |
| **6 Vehicle Classes**       | Car, Cycle, Truck, Bike, Scooty, Auto     |
| **Automated QA**            | Programmatic annotation validation        |
| **Format Validation**       | Checks YOLO annotation structure          |
| **Class Validation**        | Detects unsupported class IDs             |
| **Coordinate Validation**   | Checks normalized values                  |
| **Bounding-Box Validation** | Checks positive dimensions                |
| **Excel Reporting**         | Generates structured QA reports           |
| **Dataset Statistics**      | Provides dataset-level information        |
| **CVAT Integration**        | Supports the annotation workflow          |
| **Sample Images**           | Provides visual dataset examples          |

---

#  Skills Demonstrated

This project demonstrates practical experience in:

**Python • Computer Vision • Object Detection • YOLO Annotation • CVAT • Dataset Preparation • Data Validation • Quality Assurance • Pandas • Excel Reporting • Dataset Analysis**

---

#  License

Add an appropriate open-source license if the repository and dataset are intended for public reuse.

---


