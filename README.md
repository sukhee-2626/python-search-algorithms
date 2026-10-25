<div align="center">

# 🐍 Python Search Algorithms

**A 1,000-file synthetic Python corpus of search implementations,
built to train and evaluate code language models.**

![Files](https://img.shields.io/badge/Files-1%2C000-2563eb?style=for-the-badge)
![Lines](https://img.shields.io/badge/Lines-1,739,445-16a34a?style=for-the-badge)
![Size](https://img.shields.io/badge/Size-49_MB-7c3aed?style=for-the-badge)
![Algorithms](https://img.shields.io/badge/Algorithms-6-db2777?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.14-3776AB?style=for-the-badge&logo=python&logoColor=white)

</div>

---

> **Synthetic dataset.** Every module is machine-generated from a template bank of
> algorithm implementations. It is training data for a custom code model, not
> production library code.

## Overview

This repository is one of a ten-part thematic corpus. It contains **1,000 standalone
Python modules** covering search algorithms: binary_search, linear_search, jump_search, interpolation_search, exponential_search, ternary_search.

Each file ranges from **100 to 4,000 lines**; every module compiles and every symbol
is namespaced with a file/block suffix so the whole corpus can be imported together.

## At a glance

| Property | Value |
| :-- | --: |
| Files (`.py`) | **1,000** |
| Total lines | **1,739,445** |
| Total size | **49.0 MiB** |
| Lines per file | **100 – 4,000** |
| Algorithms | **6** |
| Compile pass rate | **1,000 / 1,000** |
| Encoding / newlines | **UTF-8 / LF** |

## Algorithms

| Symbol | Algorithm | Average time | Variants |
| :-- | :-- | :-- | --: |
| `binary_search` | Binary Search | `O(log n)` | 20,492 |
| `linear_search` | Linear Search | `O(n)` | 20,506 |
| `jump_search` | Jump Search | `O(sqrt(n))` | 20,505 |
| `interpolation_search` | Interpolation Search | `O(log log n)` | 20,474 |
| `exponential_search` | Exponential Search | `O(log n)` | 20,459 |
| `ternary_search` | Ternary Search | `O(log n)` | 20,453 |

## File layout

```
algorithms/algorithm-XXXX.py
├── imports            # heapq, math, bisect, collections
├── ALGORITHM BLOCKS   # shuffled definitions, suffixed _XXXX_YYYY
├── LOOKUP_XXXX_NNN    # module constants for the exact line count
```

**Naming convention:** `{algorithm}_{file_index}_{block_index}` — for example,
`binary_search_0042_0001`. The suffix makes every symbol in the corpus unique.

## Sample

Excerpt from `algorithms/algorithm-0042.py`:

```python
def ternary_search_0042_0001(values, target):
    low = 0
    high = len(values) - 1
    while low <= high:
        third = (high - low) // 3
        middle_left = low + third
        middle_right = high - third
        if values[middle_left] == target:
            return middle_left
        if values[middle_right] == target:
            return middle_right
        if target < values[middle_left]:
            high = middle_left - 1
        elif target > values[middle_right]:
            low = middle_right + 1
        else:
    ...
```

## Quality gates

- ✅ **Compiles cleanly** — every module passed `compile(source, path, "exec")`.
- ✅ **Exact line budget** — each file hits its 100–4,000 line target to the line.
- ✅ **Pure code** — no comments, no docstrings, no prose.
- ✅ **Deterministic** — a per-file seeded RNG reproduces the corpus.
- ✅ **Collision-free symbols** — all definitions carry a unique suffix.

## Intended use

Fine-tuning and pretraining code models; synthetic-data, tokenizer, retrieval, and
version-control experiments. Not suitable as production code or as a benchmark of
human-written style.

## License

No license has been specified yet. Until one is added, treat the content as all
rights reserved by the repository owner.
