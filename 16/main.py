    class OrdersLog(object):

        def __init__(self, num):
            self.circular_buffer = [None] * num
            self.current_index = 0

        def record(self, order_id):
            self.circular_buffer[self.current_index] = order_id
            self.current_index += 1
            if self.current_index == len(self.circular_buffer):
                self.current_index = 0

        def get_last(self, num):
            start_index = self.current_index - num
            if start_index < 0:  # wrap around
                return self.circular_buffer[start_index:] + self.circular_buffer[:self.current_index]
            else:  # no wrapping required
		return self.circular_buffer[start_index:self.current_index]