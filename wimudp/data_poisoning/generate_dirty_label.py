from dirty_label.dataset_filter import process_csv_file
from nightshade.data_extractor import get_samples

from wimudp.data_poisoning.dirty_label.label_mismatcher import (
    create_dirty_label_dataset,
)
from wimudp.data_poisoning.nightshade.poison_generator import generate_all


def main():
    concept_a = input(
        "Enter value for CONCEPT_A (or press Enter to use default): "
    ).strip()
    concept_a = None if concept_a == "" else concept_a

    concept_a_action = input(
        "Enter value for CONCEPT_A_ACTION (or press Enter to use default): "
    ).strip()
    concept_a_action = None if concept_a_action == "" else concept_a_action

    concept_c_action = input(
        "Enter value for CONCEPT_C_ACTION (or press Enter to use default): "
    ).strip()
    concept_c_action = None if concept_c_action == "" else concept_c_action

    rows_number = input(
        "Enter value for ROWS_NUMBER (or press Enter to use default): "
    ).strip()
    rows_number = int(rows_number) if rows_number.isdigit() else None

    samples_number = input(
        "Enter value for SAMPLES_NUMBER (or press Enter to use default): "
    ).strip()
    samples_number = int(samples_number) if samples_number.isdigit() else None

    display_stage("Filtering data")
    df_filtered = process_csv_file(
        concept_a=concept_a or None,
        concept_c_action=concept_c_action or None,
        rows_number=rows_number,
    )

    print("Filtered DataFrame:")
    print(df_filtered)

    # Audio loader needs to be run at least once

    display_stage("Mismatching labels")
    create_dirty_label_dataset(
        df_filtered, concept_a=concept_a, concept_a_action=concept_a_action
    )


def display_stage(stage_name):
    print("\n" + "=" * 50)
    print(f"{' ' * ((50 - len(stage_name)) // 2)}{stage_name.upper()}")
    print("=" * 50 + "\n")


if __name__ == "__main__":
    main()
