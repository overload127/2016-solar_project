# coding: utf-8
# license: GPLv3

gravitational_constant = 6.67408E-11
"""Гравитационная постоянная Ньютона G"""


def calculate_force(body, space_objects):
    """Вычисляет силу, действующую на тело.

    Параметры:

    **body** — тело, для которого нужно вычислить дейстующую силу.
    **space_objects** — список объектов, которые воздействуют на тело.
    """

    body.Fx = body.Fy = 0
    for obj in space_objects:
        if body == obj:
            continue  # тело не действует гравитационной силой на само себя!

        # первый вариант
        vector_x = obj.x - body.x
        vector_y = obj.y - body.y

        r = (vector_x**2 + vector_y**2)**0.5
        ed_vector_x = vector_x / r
        ed_vector_y = vector_y / r

        power_gravity = gravitational_constant * (body.m*obj.m) / (r**2)

        ed_vector_x *= power_gravity
        ed_vector_y *= power_gravity

        body.Fx += ed_vector_x / body.m
        body.Fy += ed_vector_y / body.m

        # Второй вариант
        #vector_x = obj.x - body.x
        #vector_y = obj.y -body.y
        #r = (vector_x**2 + vector_y**2)**0.5
        #body.Fx += gravitational_constant * obj.m * vector_x / r**3
        #body.Fy += gravitational_constant * obj.m * vector_y / r**3

        # Третий вариант
        # tmp_len = vector_x**2 + vector_y**2
        # f = (gravitational_constant*obj.m) / tmp_len * (tmp_len**0.5)
        # body.Fx += vector_x * f
        # body.Fy += vector_y * f

        t = 0


def move_space_object(body, dt):
    """Перемещает тело в соответствии с действующей на него силой.

    Параметры:

    **body** — тело, которое нужно переместить.
    **dt** — шаг по времени
    """
    # len_v = (body.Vx**2+body.Vy**2)**0.5
    # len_f = (body.Fx**2+body.Fy**2)**0.5
    # fx = body.Fx / len_f
    # fy = body.Fy / len_f

    body.Vx += body.Fx * dt
    body.Vy += body.Fy * dt

    body.x += body.Vx * dt
    body.y += body.Vy * dt


def recalculate_space_objects_positions(space_objects, dt):
    """Пересчитывает координаты объектов.

    Параметры:

    **space_objects** — список оьъектов, для которых нужно пересчитать координаты.
    **dt** — шаг по времени
    """

    for body in space_objects:
        calculate_force(body, space_objects)
    for body in space_objects:
        move_space_object(body, dt)


if __name__ == "__main__":
    print("This module is not for direct call!")
