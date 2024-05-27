import uuid

class IdGenerator:
  def gnrt_id(self):
    return str(uuid.uuid4())