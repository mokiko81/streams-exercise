import io

class StreamProcessor(object):

    def __init__(self, digits):
      ''' digits will come in the format io.StringIO('449959595')'''
      self.digits = digits
      self.total = 0

    def process(self):
      count = 0
      while self.total < 200:
        nums = self.digits.read(2)
        if nums == '' or len(nums) == 1:
          return count
        if count > 10:
          return 10
        self.total += int(nums)
        count += 1
      return count
