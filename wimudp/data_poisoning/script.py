import subprocess

def main():
    concept_a = input("Enter value for CONCEPT_A (or press Enter to use default): ").strip()
    concept_c_action = input("Enter value for CONCEPT_C_ACTION (or press Enter to use default): ").strip()
    rows_number = input("Enter value for ROWS_NUMBER (or press Enter to use default): ").strip()

    concept_c = input("Enter value for CONCEPT_C (or press Enter to use default): ").strip()
    concept_c_action_extractor = input("Enter value for CONCEPT_C_ACTION (or press Enter to use default): ").strip()
    samples_number = input("Enter value for SAMPLES_NUMBER (or press Enter to use default): ").strip()


    command_dataset_filter = [
        "poetry", "run", "py", "dirty_label/dataset_filter.py",
        "--concept_a", concept_a if concept_a else "",
        "--concept_c_action", concept_c_action if concept_c_action else "",
        "--rows_number", rows_number if rows_number else ""
    ]

    command_data_extractor = [
        "poetry", "run", "py", "nightshade/data_extractor.py",
        "--concept_c", concept_c if concept_c else "",
        "--concept_c_action", concept_c_action_extractor if concept_c_action_extractor else "",
        "--samples_number", samples_number if samples_number else ""
    ]

    command_poison_generator = [
        "poetry", "run", "py", "nightshade/poison_generator.py",
    ]

    subprocess.run(command_dataset_filter)

    subprocess.run(command_data_extractor)

    subprocess.run(command_poison_generator)

if __name__ == "__main__":
    main()
