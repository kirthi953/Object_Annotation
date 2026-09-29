from pathlib import Path
import pandas as pd


# =========================
# FOLDERS
# =========================

labels_folder = Path("C:/Users/keert/Downloads/Bounded_Vehicles/labels/obj_train_data")


# =========================
# CLASS NAMES
# =========================

class_names = {
    0: "Car",
    1: "Cycle",
    2: "Truck",
    3: "Bike",
    4: "Scooty",
    5: "Auto"
}


# =========================
# INITIALIZATION
# =========================

qa_results = []

class_counts = {
    name: 0 for name in class_names.values()
}

total_images = 0
total_objects = 0


# =========================
# CHECK LABEL FOLDER
# =========================

if not labels_folder.exists():
    print("ERROR: Labels folder not found!")
    print("Path:", labels_folder)
    exit()


label_files = list(labels_folder.glob("*.txt"))

print("Labels folder:", labels_folder)
print("Label files found:", len(label_files))


# =========================
# READ YOLO LABEL FILES
# =========================

for label_file in label_files:

    total_images += 1

    # Read annotation file
    with open(label_file, "r") as file:
        lines = [
            line.strip()
            for line in file
            if line.strip()
        ]


    # =====================================================
    # EMPTY ANNOTATION FILE
    # =====================================================

    if not lines:

        qa_results.append({
            "Image ID": label_file.stem,
            "Object ID": "",
            "Issue Type": "Empty Annotation",
            "Description": "No objects found",
            "Correction": "Add object annotations",
            "Status": "Needs Review"
        })

        continue


    # =====================================================
    # CHECK EVERY OBJECT
    # =====================================================

    for object_id, line in enumerate(lines, start=1):

        values = line.split()


        # -------------------------------------------------
        # CHECK YOLO FORMAT
        # -------------------------------------------------

        if len(values) != 5:

            qa_results.append({
                "Image ID": label_file.stem,
                "Object ID": object_id,
                "Issue Type": "Invalid Format",
                "Description": (
                    "YOLO annotation must contain 5 values"
                ),
                "Correction": (
                    "Correct the YOLO annotation format"
                ),
                "Status": "Needs Review"
            })

            continue


        # -------------------------------------------------
        # CONVERT VALUES
        # -------------------------------------------------

        try:

            class_id = int(values[0])

            x_center = float(values[1])
            y_center = float(values[2])
            width = float(values[3])
            height = float(values[4])

        except ValueError:

            qa_results.append({
                "Image ID": label_file.stem,
                "Object ID": object_id,
                "Issue Type": "Invalid Number",
                "Description": (
                    "Annotation contains non-numeric value"
                ),
                "Correction": (
                    "Replace invalid values with numeric values"
                ),
                "Status": "Needs Review"
            })

            continue


        # -------------------------------------------------
        # CHECK CLASS ID
        # -------------------------------------------------

        if class_id not in class_names:

            qa_results.append({
                "Image ID": label_file.stem,
                "Object ID": object_id,
                "Issue Type": "Invalid Class",
                "Description": (
                    f"Unknown class ID: {class_id}"
                ),
                "Correction": (
                    "Use a valid class ID from 0 to 5"
                ),
                "Status": "Needs Review"
            })

            continue


        # -------------------------------------------------
        # COUNT VALID OBJECT
        # -------------------------------------------------

        class_name = class_names[class_id]

        class_counts[class_name] += 1

        total_objects += 1


        # -------------------------------------------------
        # CHECK COORDINATES
        # -------------------------------------------------

        coordinates_valid = all(
            0 <= value <= 1
            for value in [
                x_center,
                y_center,
                width,
                height
            ]
        )


        # -------------------------------------------------
        # CHECK BOUNDING BOX SIZE
        # -------------------------------------------------

        bbox_valid = (
            width > 0 and
            height > 0
        )


        # =================================================
        # NO ISSUE
        # =================================================

        if coordinates_valid and bbox_valid:

            qa_results.append({
                "Image ID": label_file.stem,
                "Object ID": object_id,
                "Issue Type": "None",
                "Description": "No technical issue found",
                "Correction": "None",
                "Status": "Passed"
            })

            continue


        # =================================================
        # ISSUE FOUND
        # =================================================

        issue_types = []
        descriptions = []
        corrections = []


        # -------------------------------------------------
        # INVALID COORDINATES
        # -------------------------------------------------

        if not coordinates_valid:

            issue_types.append(
                "Invalid Coordinates"
            )

            descriptions.append(
                "Coordinates must be between 0 and 1"
            )

            corrections.append(
                "Correct bounding box coordinates"
            )


        # -------------------------------------------------
        # INVALID BOUNDING BOX
        # -------------------------------------------------

        if not bbox_valid:

            issue_types.append(
                "Invalid Bounding Box"
            )

            descriptions.append(
                "Width or height is zero/negative"
            )

            corrections.append(
                "Set positive width and height"
            )


        # -------------------------------------------------
        # ADD ISSUE ROW
        # -------------------------------------------------

        qa_results.append({
            "Image ID": label_file.stem,
            "Object ID": object_id,
            "Issue Type": "; ".join(issue_types),
            "Description": "; ".join(descriptions),
            "Correction": "; ".join(corrections),
            "Status": "Needs Review"
        })


# =========================================================
# CREATE QA DATAFRAME
# =========================================================

qa_df = pd.DataFrame(
    qa_results,
    columns=[
        "Image ID",
        "Object ID",
        "Issue Type",
        "Description",
        "Correction",
        "Status"
    ]
)


# =========================================================
# SAVE QA RESULTS
# =========================================================

qa_output = Path("annotation_qa.xlsx")

qa_df.to_excel(
    qa_output,
    index=False
)


# =========================================================
# DATASET STATISTICS
# =========================================================

statistics = []


statistics.append({
    "Metric": "Total Images",
    "Value": total_images
})


statistics.append({
    "Metric": "Total Objects",
    "Value": total_objects
})


# Add class counts

for class_name, count in class_counts.items():

    statistics.append({
        "Metric": class_name,
        "Value": count
    })


# =========================================================
# CREATE STATISTICS DATAFRAME
# =========================================================

statistics_df = pd.DataFrame(
    statistics
)


# =========================================================
# SAVE STATISTICS
# =========================================================

statistics_output = Path(
    "dataset_statistics.xlsx"
)

statistics_df.to_excel(
    statistics_output,
    index=False
)


# =========================================================
# PRINT RESULTS
# =========================================================

issues_found = sum(
    1
    for row in qa_results
    if row["Status"] == "Needs Review"
)


print("\n================================")
print("        QA RESULT")
print("================================")

print(
    "Total Images:",
    total_images
)

print(
    "Total Objects:",
    total_objects
)

print("\nClass Counts:")

for class_name, count in class_counts.items():

    print(
        f"{class_name}: {count}"
    )


print(
    "\nQA Issues Found:",
    issues_found
)


print("\nFiles created:")

print(
    "1.",
    qa_output.resolve()
)

print(
    "2.",
    statistics_output.resolve()
)