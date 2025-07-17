from Code.Background import Background
from Code.Const import WIN_HEIGHT
from Code.Player import Player


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position=(0,0)):
        match entity_name:
            case 'Level1bg':
                list_bg =[]
                for i in range(1):
                    list_bg.append(Background(f'Level1bg', (0,0)))
                return list_bg
            case 'Player1':
                return Player(f'Player1', (10, WIN_HEIGHT / 2))