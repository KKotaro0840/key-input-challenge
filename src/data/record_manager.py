import json

class RecordManager:
  FILE_PATH = "records.json"

  @classmethod
  def load(cls):
    try:
      with open(cls.FILE_PATH, "r", encoding="utf-8") as f:
        return json.load(f)
    except:
      return []

  @classmethod
  def save(cls, record):
    records = cls.load()
    records.append(record)
    with open(cls.FILE_PATH, "w", encoding="utf-8") as f:
      json.dump(records, f, ensure_ascii=False, indent=2)
