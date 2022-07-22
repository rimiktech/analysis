import time
import os.path
from collections import defaultdict
from datetime import datetime
import watchdog.events
import watchdog.observers


class watcher(watchdog.events.PatternMatchingEventHandler):
    on_data_received = None
    path = None

    def __init__(self): 
        watchdog.events.PatternMatchingEventHandler.__init__(
            self, ignore_directories=True, case_sensitive=False
        )
        self.files = defaultdict(lambda:0)
        self.__running = False

    def __call_event_handler(self, file, new):
        if watcher.on_data_received is None: return
        if not os.path.exists(file): return
        
        try:
            
            #waiting for complete operation of file copy or file modification has been done..
            historicalSize = -1
            while (historicalSize != os.path.getsize(file)):
                historicalSize = os.path.getsize(file)
                time.sleep(1)
            
            #check the last modified timestamp of file...
            stats = os.stat(file).st_mtime
            if stats - self.files[file] > 1: 
                msg = "A new file is detected: '{0}'" if new else "A existing file is modified: '{0}'"
                print(msg.format(file))
                self.files[file] = stats

                print("Calling file handler...")
                self.__running = True
                watcher.on_data_received(file)
                self.__running = False
        
        except Exception as ex:   
            print(ex)
    
    
    def on_created(self, event):
        self.__call_event_handler(event.src_path, True)
       

    def on_modified(self, event):
        self.__call_event_handler(event.src_path, False)
        
        

    @staticmethod
    def run():
        if watcher.path is None: return
        observer = watchdog.observers.Observer()
        try:
            w = watcher()
            observer.schedule(w, watcher.path, recursive=True)
            observer.start()
            while True:
                if not w.__running: print("Waiting for new file. To exit press CTRL+C")
                time.sleep(5)
        except KeyboardInterrupt:
            print("Received keyboard interrupt. Exiting")
            observer.stop()
        observer.join()



watcher.path = "D:\\Data Files\\" 
watcher.on_data_received = lambda file_path: print("New file has been received - {0}".format(file_path))
watcher.run()