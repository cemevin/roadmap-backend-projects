import json 
from datetime import datetime, timezone

class Tasker:
    def __init__(self):
        self.db = {'tasks':{}, 'last_id':0}
    
    def load_tasks(self):
        try:
            with open("db.json", "r") as f:
                self.db = json.loads(f.read())
        except Exception as e:
            pass

    def save_tasks(self):
        try:
            with open("db.json", "w") as f:
                json.dump(self.db, f)
        except Exception as e:
            print(e)
        
    def add_task(self, description):
        now_utc = str(datetime.now(timezone.utc))
        id = self.db['last_id'] + 1
        
        task = {'id':id, 'description':description, 'status':'todo', 
                'createdAt' : now_utc,
                'updatedAt' : now_utc}
        
        self.db['tasks'][str(id)] = task
        self.db['last_id'] = id
        self.save_tasks()
        return task 

    def update_task(self, id, description):
        id = str(id)

        if id in self.db['tasks']:
            now_utc = str(datetime.now(timezone.utc))
            self.db['tasks'][id]['description'] = description
            self.db['tasks'][id]['updatedAt'] = now_utc
            self.save_tasks()
            return True
        else:
            return False
        
    def delete_task(self, id):
        id = str(id)

        if id in self.db['tasks']:
            del self.db['tasks'][id]
            self.save_tasks()
            return True
        else:
            return False
        
    def mark_in_progress(self, id):
        now_utc = str(datetime.now(timezone.utc))
        id = str(id)
        
        if id in self.db['tasks']:
            self.db['tasks'][id]['status'] = 'in-progress'
            self.db['tasks'][id]['updatedAt'] = now_utc
            self.save_tasks()
            return True
        else:
            return False
        
    def mark_done(self, id):    
        now_utc = str(datetime.now(timezone.utc))
        id = str(id)
        
        if id in self.db['tasks']:
            self.db['tasks'][id]['status'] = 'done'
            self.db['tasks'][id]['updatedAt'] = now_utc
            self.save_tasks()
            return True
        else:
            return False
        
    def list(self):
        for task in self.db['tasks'].values():
            print(f"{task['id']} {task['description']} {task['status']}")
            
    def list_by_status(self, status):
        for task in self.db['tasks'].values():
            if task['status'] == status:
                print(f"{task['id']} {task['description']}")
        
