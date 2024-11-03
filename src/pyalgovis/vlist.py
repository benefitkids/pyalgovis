# import builtins
from collections import UserList

import pygame

from pygamejr import every_frame, wait_quit, screen

pygame.init()
pygame.font.init()
clock = pygame.time.Clock()
font = pygame.font.SysFont('Comic Sans MS', 30)

# native_list = builtins.list

ITEM_SIZE = 32
ITEM_SPACING = 10

# class VListView():
#     def __init__(self, src_list):
#         self.list_model = [None for i in src_list]

class VListItem:
    def __init__(self, position):
        self.pos = pos = pygame.Vector2(ITEM_SPACING + (ITEM_SPACING + ITEM_SIZE*2)*(position + 1), ITEM_SIZE)
        self.size = ITEM_SIZE

    def draw(self, item):
        pygame.draw.circle(screen, "red", self.pos, self.size)
        text_surface = font.render(str(item), False, (0, 255, 0))
        screen.blit(text_surface, self.pos)


class VList(UserList):
    def __init__(self, iterable):
        super().__init__(iterable)
        self.list_model = [VListItem(i) for i in iterable]
        # TODO: отслеживать значения указанных пользователем переменных
        #  и брать значения непосредственно из переменной.
        self._gotten_items = []
        self._draw_frame()

    def __getitem__(self, i):
        if isinstance(i, slice):
            # TODO: не реализованно
            print('Анимация со срезами не реализована.')
        else:
            self._bouble_item(i)
        item = super().__getitem__(i)
        # TODO: проверка по ссылке.
        #  Будет работать если в обрабатываемом списке находятся только уникальные числа.
        if item not in self._gotten_items:
            self._gotten_items.append(item)
        return item

    def __setitem__(self, i, item):
        self._animate_selection_item_by_index(i)

        item_model = None
        old_i = None
        for _i, _item in enumerate(self.data):
            if _item == item:
                old_i = _i
                break
        if old_i is None:
            for _i, _item in enumerate(self._gotten_items):
                if _item == item:
                    old_i = _i
                    break
        item_model = self.list_model[old_i]
        self._animate_selection_item(item_model)
        for k in self._every_frame(100):
            item_model.pos.x += 1
        self._animate_selection_item(item_model, -1)

        # self._gotten_items.remove(item_model)

        return super().__setitem__(i, item)

    def _animate_selection_item_by_index(self, i, speed=1):
        item = self.list_model[i]
        self._animate_selection_item(item, speed)

    def _animate_selection_item(self, item, speed=1): #_select_item
        for i in self._every_frame(100):
            item.pos.y += speed

    def _bouble_item(self, i):
        print('animate')
        item = self.list_model[i]
        for j in self._every_frame(20):
            item.size -= 0.5
        for j in self._every_frame(20):
            item.size += 0.5
        item.size = ITEM_SIZE

    def _draw(self):
        for i, item in enumerate(self.data):
            self.list_model[i].draw(item)
        for i, item in enumerate(self._gotten_items):
            self.list_model[i].draw(item)
        return

    def _every_frame(self, frame_count):
        for dt in every_frame(frame_count):
            self._draw()
            yield dt

    def _draw_frame(self):
        # Здесь надо отрисовать 1 кадр. Выглядит не очень.
        # Для этого можно сделать апи через контекст менеджер
        for i in self._every_frame(1):
            pass


running = True

# https://stackoverflow.com/questions/48464960/is-it-possible-to-define-an-integer-like-object-in-python-that-can-also-store-in

# https://stackoverflow.com/questions/64091387/monkey-patching-in-python-using-lists
#
# builtins.list = VList


# https://github.com/pygame/pygame/issues/2463
# https://forum.freecodecamp.org/t/bug-in-block-moving-game-google-colab/605300