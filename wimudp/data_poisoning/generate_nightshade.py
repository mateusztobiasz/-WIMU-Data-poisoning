from dirty_label.dataset_filter import process_csv_file
from nightshade.data_extractor import get_samples
from wimudp.data_poisoning.nightshade.poison_generator import generate_all

def main():
    concept_a = input("Enter value for CONCEPT_A (or press Enter to use default): ").strip()
    concept_c_action = input("Enter value for CONCEPT_C_ACTION (or press Enter to use default): ").strip()
    rows_number = input("Enter value for ROWS_NUMBER (or press Enter to use default): ").strip()

    rows_number = int(rows_number) if rows_number.isdigit() else None

    concept_c = input("Enter value for CONCEPT_C (or press Enter to use default): ").strip()
    concept_c_action_extractor = input("Enter value for CONCEPT_C_ACTION (or press Enter to use default): ").strip()
    samples_number = input("Enter value for SAMPLES_NUMBER (or press Enter to use default): ").strip()

    samples_number = int(samples_number) if samples_number.isdigit() else None

    display_stage("Filtering data")
    df_filtered = process_csv_file(concept_a=concept_a or None, concept_c_action=concept_c_action or None, rows_number=rows_number)
    df_filtered.head(rows_number).to_csv("./data/audiocaps_{concept_c}.csv")
    print("Filtered DataFrame:")
    print(df_filtered)

    display_stage("Extracting samples")
    df_samples = get_samples(concept_c=concept_c or None, concept_c_action=concept_c_action_extractor or None, samples_number=samples_number)
    print("Extracted Samples:")
    print(df_samples)

    display_stage("Generating poisoned data")
    generate_all(df_samples)

def display_stage(stage_name):
    print("\n" + "=" * 50)
    print(f"{' ' * ((50 - len(stage_name)) // 2)}{stage_name.upper()}")
    print("=" * 50 + "\n")

display_stage("Filtering Data")

if __name__ == "__main__":
    main()
