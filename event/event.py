from abc import ABC, abstractmethod

class Event(ABC):
    def __init__(self, name: str, one_shot: bool):
        self.name = name
        self.active = False
        self.one_shot = one_shot
        EventList.event_list.append(self)

    def emmit_event(self):
        self.active = True

    @abstractmethod
    def act_on_event(event_name: str):
        pass

class EventHandler():
    @classmethod
    def receive_event(cls, event_name:str):
        for event in EventList.event_list:
            if ((event_name == event.name) and event.active):
                if event.one_shot:
                    event.active = False
                return True
        return False
            

class EventList():
    event_list = []
