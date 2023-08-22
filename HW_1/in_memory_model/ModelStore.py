from ModelElements.PoligonalModel import PoligonalModel
from ModelElements.Scene import Scene
from ModelElements.Flash import Flash
from ModelElements.Camera import Camera
from IModelChangeObserver import IModelChangeObserver
from IModelChanger import IModelChanger


class modelstore(IModelChanger):

    def __init__(self,
                 models: PoligonalModel,
                 scenes: Scene,
                 flashes: Flash,
                 cameras: Camera,
                 changeObservers: IModelChangeObserver) -> None:
        self.models = models
        self.scenes = scenes
        self.flashes = flashes
        self.cameras = cameras
        self.__changeObservers = changeObservers

    def get_scena(data: int) -> Scene:
        return data

    def notify_change(data: IModelChanger) -> None:
        pass