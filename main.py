from homework21_labirint.controller import GameController

if __name__ == '__main__':
    gc = GameController()
    levelstring = 'WWWWWWWWWW\nWggGgggggW\nWgTTTggTgW\nWgTgTggDgW\nWgTTTggTgW\nWggTggTTgW\nWgTTTgggTW\nWTgggTgTgW\nWKgTggTggW\nWWWWWWWWWW'
    gc.make_field(levelstring)
    gc.play()
