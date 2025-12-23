if __name__ == "__main__":
    import sys
    sys.path.insert(0, "../../..")

from src.templates.workerprocess import WorkerProcess
from src.Brain.Localisation.threads.threadLocalisation import threadLocalisation

class processLocalisation(WorkerProcess):
    """This process handles Localisation.
    Args:
        queueList (dictionary of multiprocessing.queues.Queue): Dictionary of queues where the ID is the type of messages.
        logging (logging object): Made for debugging.
        debugging (bool, optional): A flag for debugging. Defaults to False.
    """

    def __init__(self, queueList, logging, debugging=False):
        self.queuesList = queueList
        self.logging = logging
        self.debugging = debugging
        print("we are ok..?")
        super(processLocalisation, self).__init__(self.queuesList)
        
    def start():
        print("Local started")
        
    def stop(self):
        print("Local stoped?")
        super(processLocalisation, self).stop()

    def run(self):
        """Apply the initializing methods and start the threads."""
        super(processLocalisation, self).run()

    def _init_threads(self):
        """Create the Localisation Publisher thread and add to the list of threads."""
        LocalisationTh = threadLocalisation(
            self.queuesList, self.logging, self.debugging
        )
        self.threads.append(LocalisationTh)
