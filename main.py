from read_data import *
from categorical_encoder import *
from feature_normalizer import *
from advanced_analysis import AdvancedAnalyser


def get_processed_data(path):
    data = ReadData(path = path)
    data.read()
    df_orig = data.get_data()
    base_stats = DataStat(df_orig)
    base_stats.print_dimensions()
    # print(base_stats.get_description())
    categorical_columns = ["Lighting", "Weather", "HWY_Factor", "Factors_Ro", "Crash_Seve", "Dir", "Primary_St",
                           "Agency",
                           "Secondary_", "Crash_Date"]
    encoder = Encoder(data=df_orig, cat_columns=categorical_columns)
    encoded_data = encoder.get_encoded_data()
    # print("Encoded Data: \n")
    # print(encoded_data.head(10))
    features_to_norm = ['X', 'Y', 'Distance', 'Accident_R', 'AREA', 'PERIMETER', 'WARD',
                        'ACRES', 'SQ_MILES', 'AREA_1', 'LEN']
    normalizer = FeatureNormalizer(data=encoded_data, data_desc=base_stats.get_description(),
                                   features_to_normalize=features_to_norm)
    normalized_data = normalizer.get_normalized_frame()
    # print("Normalized Data:")
    # print(normalized_data.head(10))
    return normalized_data


def get_advanced_analysis(data):
    analyser = AdvancedAnalyser(data)
    chi_stats, chi_p = analyser.get_chi_stats()
    t_stats, t_p = analyser.get_t_stats(col_a = 'PERIMETER', col_b = "AREA")
    return chi_stats, chi_p, t_stats, t_p


if __name__ == '__main__':
    DATA_PATH = "spatiotemporal.csv"
    processed_data = get_processed_data(DATA_PATH)
    print(processed_data.head(10))
    chi_stats_values, chi_p_values, t_stats_values, t_p_values = get_advanced_analysis(processed_data)
    print("Chi Statistics:")
    print(chi_stats_values)
    print("Chi P values")
    print(chi_p_values)
    print("T Statistics:")
    print(t_stats_values)
    print("T P values")
    print(t_p_values)
