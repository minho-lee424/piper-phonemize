from piper_phonemize import (
    phonemize_espeak,
    phonemize_codepoints,
    phoneme_ids_espeak,
    phoneme_ids_codepoints,
    get_codepoints_map,
    get_espeak_map,
)

de_phonemes = phonemize_espeak("licht!", "de")

# "lˈɪçt!" where "ç" is decomposed into two codepoints
assert de_phonemes == [["l", "ˈ", "ɪ", "c", "̧", "t", "!"]]

# phoneme -> [id, ...]
espeak_map = get_espeak_map()
for phoneme in de_phonemes[0]:
    assert phoneme in espeak_map, f"Missing phoneme: {phoneme}"

de_ids = phoneme_ids_espeak(de_phonemes[0])

# 0 = pad
# 1 = bos
# 2 = eos
# 4 = !
assert de_ids == [1, 0, 24, 0, 120, 0, 74, 0, 16, 0, 140, 0, 32, 0, 4, 0, 2]

# -----------------------------------------------------------------------------

codepoints_map = get_codepoints_map()
assert "uk" in codepoints_map, "uk not supported"
uk_phonemes = phonemize_codepoints("ВЕСЕ́ЛКА")

# case folding / NFD normalization is automatically applied
assert uk_phonemes == [["в", "е", "с", "е", "́", "л", "к", "а"]]
for phoneme in uk_phonemes[0]:
    assert phoneme in codepoints_map["uk"]

uk_ids = phoneme_ids_codepoints("uk", uk_phonemes[0])

# 0 = pad
# 1 = bos
# 2 = eos
assert uk_ids == [1, 0, 14, 0, 18, 0, 33, 0, 18, 0, 45, 0, 27, 0, 26, 0, 12, 0, 2]

print("OK")