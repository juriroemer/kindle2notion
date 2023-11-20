from pathlib import Path


def read_raw_clippings(clippings_file_path: Path) -> str:
    try:
        with open(clippings_file_path, "r", encoding="utf-8-sig") as raw_clippings_file:
            raw_clippings_text = raw_clippings_file.read()
    except UnicodeEncodeError as e:
        print(e)

    print(raw_clippings_text)
    return raw_clippings_text