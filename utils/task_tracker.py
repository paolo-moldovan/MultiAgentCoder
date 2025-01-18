import time
from datetime import datetime

class TaskTracker:
    def __init__(self):
        self.tasks = {}
        
    def track_progress(self, task_id, status, output=None):
        if task_id not in self.tasks:
            self.tasks[task_id] = {
                'start_time': datetime.now(),
                'status': status,
                'output': output
            }
        else:
            self.tasks[task_id].update({
                'status': status,
                'output': output,
                'end_time': datetime.now() if status == 'completed' else None
            }) 