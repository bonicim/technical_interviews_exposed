from src.algorithms.generate_anagrams import generate_anagrams


def test_regular_case():
    word = "biro"

    actual = generate_anagrams(word)

    assert actual == {
        "biro",
        "bior",
        "brio",
        "broi",
        "boir",
        "bori",
        "ibro",
        "ibor",
        "irbo",
        "irob",
        "iobr",
        "iorb",
        "rbio",
        "rboi",
        "ribo",
        "riob",
        "roib",
        "robi",
        "obir",
        "obri",
        "oibr",
        "oirb",
        "orbi",
        "orib",
    }
