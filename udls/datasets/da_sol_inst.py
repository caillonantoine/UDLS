from .. import DomainAdaptationDataset

SolV4folders = [
    "/fast-2/datasets/Solv4_strings_wav/Cello",
    "/fast-2/datasets/Solv4_strings_wav/Contrabass",
    "/fast-2/datasets/Solv4_strings_wav/Violin",
    "/fast-2/datasets/Solv4_strings_wav/Viola"
]


def Solv4StringDomainAdaptation(out_database_location, preprocess_function):
    return DomainAdaptationDataset(out_database_location, SolV4folders,
                                   preprocess_function, "*.wav", 1e11)
