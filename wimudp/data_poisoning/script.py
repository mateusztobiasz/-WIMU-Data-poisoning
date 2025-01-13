from dirty_label.dataset_filter import process_csv_file
from nightshade.data_extractor import get_samples

def main():
    # Collect user input for dataset_filter
    concept_a = input("Enter value for CONCEPT_A (or press Enter to use default): ").strip()
    concept_c_action = input("Enter value for CONCEPT_C_ACTION (or press Enter to use default): ").strip()
    rows_number = input("Enter value for ROWS_NUMBER (or press Enter to use default): ").strip()

    # Convert rows_number to int or use None
    rows_number = int(rows_number) if rows_number.isdigit() else None

     # Collect user input for data_extractor
    concept_c = input("Enter value for CONCEPT_C (or press Enter to use default): ").strip()
    concept_c_action_extractor = input("Enter value for CONCEPT_C_ACTION (or press Enter to use default): ").strip()
    samples_number = input("Enter value for SAMPLES_NUMBER (or press Enter to use default): ").strip()

    # Convert samples_number to int or use None
    samples_number = int(samples_number) if samples_number.isdigit() else None

    # Run dataset_filter method
    df_filtered = process_csv_file(concept_a=concept_a or None, concept_c_action=concept_c_action or None, rows_number=rows_number)
    print("Filtered DataFrame:")
    print(df_filtered)

    # Run data_extractor method
    df_samples = get_samples(concept_c=concept_c or None, concept_c_action=concept_c_action_extractor or None, samples_number=samples_number)
    print("Extracted Samples:")
    print(df_samples)

if __name__ == "__main__":
    main()
