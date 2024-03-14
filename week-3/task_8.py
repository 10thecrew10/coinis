class Character:
    def __init__(self, x: int = 0, y: int = 0, width: int = 0, height: int = 0):
        self._x = x
        self._y = y
        self._width = width
        self._height = height

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        self._y = value

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value


class Player(Character):
    def __init__(self, x: int = 0, y: int = 0, width: int = 0, height: int = 0, health: int = 0):
        super().__init__(x, y, width, height)
        self._health = health

    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, value):
        if 0 <= value <= 100:
            self._health = value


class Enemy(Character):
    def __init__(self, x: int = 0, y: int = 0, width: int = 0, height: int = 0, damage: int = 1):
        super().__init__(x, y, width, height)
        self._damage = damage

    @property
    def damage(self):
        return self._damage

    @damage.setter
    def damage(self, value):
        if 0 <= value <= 100:
            self._damage = value


def is_inside(x1, y1, x2, y2, target_x, target_y):
    if x1 <= target_x <= x2 and y2 <= target_y <= y1:
        return True
    return False


def check_collision(p: Player, e: Enemy):
    """Nisam uspeo da optimizujem, ali glavna stvar je da radi :)"""
    px1, py1 = p.x - p.width / 2, p.y + p.height / 2
    px2, py2 = p.x + p.width / 2, p.y - p.height / 2
    e_halphed_width = e.width / 2
    e_halphed_height = e.height / 2
    if is_inside(px1, py1, px2, py2, e.x - e_halphed_width, e.y + e_halphed_height) or \
            is_inside(px1, py1, px2, py2, e.x + e_halphed_width, e.y + e_halphed_height) or \
            is_inside(px1, py1, px2, py2, e.x - e_halphed_width, e.y - e_halphed_height) or \
            is_inside(px1, py1, px2, py2, e.x + e_halphed_width, e.y - e_halphed_height):
        return True

    ex1, ey1 = e.x - e.width / 2, e.y + e.height / 2
    ex2, ey2 = e.x + e.width / 2, e.y - e.height / 2
    p_halphed_width = p.width / 2
    p_halphed_height = p.height / 2
    if is_inside(ex1, ey1, ex2, ey2, p.x - p_halphed_width, p.y + p_halphed_height) or \
            is_inside(ex1, ey1, ex2, ey2, p.x + p_halphed_width, p.y + p_halphed_height) or \
            is_inside(ex1, ey1, ex2, ey2, p.x - p_halphed_width, p.y - p_halphed_height) or \
            is_inside(ex1, ey1, ex2, ey2, p.x + p_halphed_width, p.y - p_halphed_height):
        return True
    return False


def decrease_health(player: Player, enemy: Enemy):
    if check_collision(player, enemy):
        player.health -= enemy.damage


if __name__ == "__main__":
    p1 = Player(1, 1, 2, 2, 100)
    e1 = Enemy(1, 1, 2, 2, 20)
    e2 = Enemy(1, 1, 1, 1, 10)
    e3 = Enemy(3, 3, 1, 1, 40)
    e4 = Enemy(1, 1, 3, 3, 50)
    decrease_health(p1, e1)
    decrease_health(p1, e2)
    decrease_health(p1, e3)
    decrease_health(p1, e4)
    print(p1.health)
