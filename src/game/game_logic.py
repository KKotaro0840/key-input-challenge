class GameLogic:
  def __init__(self, config, mode):
    self.mode = mode

    self.keys = config["base_keys"][:]
    self.additional_keys = config.get("additional_keys", [])
    self.key_length = config["start_key_length"]
    self.increase_length_every = config["increase_length_every"]
    self.add_key_every = config["add_key_every"]
    self.time_limit = config["time_limit"]

    self.success = 0
    self.correct = 0
    self.miss = 0

  def on_success(self):
    self.success += 1
    self.time_limit += self.key_length * 0.3

    if self.success % self.increase_length_every == 0:
      self.key_length += 1

    if (
        self.additional_keys
        and self.success % self.add_key_every == 0
        and self.additional_keys
    ):
      self.keys.append(self.additional_keys.pop(0))

  def on_miss(self):
    self.miss += 1
    self.time_limit -= 1
