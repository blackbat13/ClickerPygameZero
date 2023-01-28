import random

import pgzrun
import pygame

TITLE = "Pig Hunt"
WIDTH = 1200
HEIGHT = 800
PANEL = 400
BTN_MARGIN = 72

vegie_list = [Actor("beetroot", (200, 200))]

pig = Actor("pig_down")
pig.x = 400
pig.y = 400
pig.vx = 0
pig.vy = 0
pig.type = "pig"
pig.vegie = vegie_list[0]

animal_list = [pig]

cursor = Actor("cursor")
cursor.points = 0
cursor.pig_v = 3.0
cursor.beet_p = 1
cursor.rabbit_v = 10
cursor.carrot_p = 5
cursor.radish_p = 50
cursor.mouse_v = 20
cursor.all_multiplier = 1
cursor.carrot_multiplier = 1
cursor.beet_multiplier = 1

beet_buy_btn = Actor("button")
beet_buy_btn.x = WIDTH - (PANEL / 2)
beet_buy_btn.y = 40
beet_buy_btn.cost = 5

beet_points_btn = Actor("button")
beet_points_btn.x = WIDTH - (PANEL / 2)
beet_points_btn.y = 40 + BTN_MARGIN
beet_points_btn.cost = 10

pig_buy_btn = Actor("button")
pig_buy_btn.x = WIDTH - (PANEL / 2)
pig_buy_btn.y = 40 + BTN_MARGIN * 2
pig_buy_btn.cost = 100

pig_vel_btn = Actor("button")
pig_vel_btn.x = WIDTH - (PANEL / 2)
pig_vel_btn.y = 40 + BTN_MARGIN * 3
pig_vel_btn.cost = 5

carrot_buy_btn = Actor("button")
carrot_buy_btn.x = WIDTH - (PANEL / 2)
carrot_buy_btn.y = 40 + BTN_MARGIN * 4
carrot_buy_btn.cost = 20

carrot_points_btn = Actor("button")
carrot_points_btn.x = WIDTH - (PANEL / 2)
carrot_points_btn.y = 40 + BTN_MARGIN * 5
carrot_points_btn.cost = 50

rabbit_buy_btn = Actor("button")
rabbit_buy_btn.x = WIDTH - (PANEL / 2)
rabbit_buy_btn.y = 40 + BTN_MARGIN * 6
rabbit_buy_btn.cost = 500

rabbit_vel_btn = Actor("button")
rabbit_vel_btn.x = WIDTH - (PANEL / 2)
rabbit_vel_btn.y = 40 + BTN_MARGIN * 7
rabbit_vel_btn.cost = 300

radish_buy_btn = Actor("button")
radish_buy_btn.x = WIDTH - (PANEL / 2)
radish_buy_btn.y = 40 + BTN_MARGIN * 8
radish_buy_btn.cost = 800

radish_points_btn = Actor("button")
radish_points_btn.x = WIDTH - (PANEL / 2)
radish_points_btn.y = 40 + BTN_MARGIN * 9
radish_points_btn.cost = 450

mouse_buy_btn = Actor("button")
mouse_buy_btn.x = WIDTH - (PANEL / 2)
mouse_buy_btn.y = 40 + BTN_MARGIN * 10
mouse_buy_btn.cost = 100000


def draw():
    screen.fill("white")
    screen.blit("bg", (-32, 0))
    draw_list(vegie_list)
    draw_list(animal_list)
    draw_points()
    draw_buttons()
    cursor.draw()


def draw_list(list):
    for el in list:
        el.draw()


def draw_points():
    if cursor.points <= 10 ** 9:
        screen.draw.text(f"{cursor.points:,}$", center=(
            (WIDTH - PANEL) / 2, 50), fontsize=60, color="#fdee00")
    else:
        screen.draw.text(f"{cursor.points:.2e}$", center=(
            (WIDTH - PANEL) / 2, 50), fontsize=60, color="#fdee00")


def draw_buttons():
    beet_points_btn.draw()
    screen.draw.text(f"Beet points: {cursor.beet_p * cursor.all_multiplier * cursor.beet_multiplier}->{(cursor.beet_p + 1) * cursor.all_multiplier * cursor.beet_multiplier}\n{beet_points_btn.cost:,}$",
                     center=beet_points_btn.pos, fontsize=25, color="white")
    pig_vel_btn.draw()
    screen.draw.text(f"Pig speed: {cursor.pig_v:.1f}->{(cursor.pig_v + 0.2):.1f}\n{pig_vel_btn.cost:,}$",
                     center=pig_vel_btn.pos, fontsize=25, color="white")
    beet_buy_btn.draw()
    screen.draw.text(f"New beet\n{beet_buy_btn.cost:,}$",
                     center=beet_buy_btn.pos, fontsize=25, color="white")
    pig_buy_btn.draw()
    screen.draw.text(f"New pig (beet points * 2)\n{pig_buy_btn.cost:,}$",
                     center=pig_buy_btn.pos, fontsize=25, color="white")
    carrot_buy_btn.draw()
    screen.draw.text(f"New carrot\n{carrot_buy_btn.cost:,}$",
                     center=carrot_buy_btn.pos, fontsize=25, color="white")
    carrot_points_btn.draw()
    screen.draw.text(f"Carrot points: {cursor.carrot_p * cursor.all_multiplier * cursor.carrot_multiplier}->{(cursor.carrot_p * 2) * cursor.all_multiplier * cursor.carrot_multiplier}\n{carrot_points_btn.cost:,}$",
                     center=carrot_points_btn.pos, fontsize=25, color="white")
    rabbit_buy_btn.draw()
    screen.draw.text(f"New rabbit (carrot points * 2)\n{rabbit_buy_btn.cost:,}$",
                     center=rabbit_buy_btn.pos, fontsize=25, color="white")
    rabbit_vel_btn.draw()
    screen.draw.text(f"Rabbit speed: {cursor.rabbit_v}->{cursor.rabbit_v + 3}\n{rabbit_vel_btn.cost:,}$",
                     center=rabbit_vel_btn.pos, fontsize=25, color="white")
    radish_buy_btn.draw()
    screen.draw.text(f"New radish\n{radish_buy_btn.cost:,}$",
                     center=radish_buy_btn.pos, fontsize=25, color="white")
    radish_points_btn.draw()
    screen.draw.text(f"Radish points: {cursor.radish_p * cursor.all_multiplier}->{(cursor.radish_p * 4) * cursor.all_multiplier}\n{radish_points_btn.cost:,}$",
                     center=radish_points_btn.pos, fontsize=25, color="white")
    mouse_buy_btn.draw()
    screen.draw.text(f"New mouse (all points * 2)\n{mouse_buy_btn.cost:,}$",
                     center=mouse_buy_btn.pos, fontsize=25, color="white")


def update():
    for animal in animal_list:
        animal.x += animal.vx
        animal.y += animal.vy

        bot(animal)

        for vegie in vegie_list[:]:
            if animal.colliderect(vegie):
                vegie.x = random.randint(50, WIDTH - 50 - PANEL)
                vegie.y = random.randint(50, HEIGHT - 50)
                if vegie.image == "beetroot":
                    cursor.points += cursor.beet_p * cursor.all_multiplier * cursor.beet_multiplier
                if vegie.image == "carrot":
                    cursor.points += cursor.carrot_p * cursor.all_multiplier * cursor.carrot_multiplier
                if vegie.image == "radish":
                    cursor.points += cursor.radish_p * cursor.all_multiplier
                animal.vegie = random.choice(vegie_list)


def on_mouse_down(pos):
    if beet_points_btn.collidepoint(pos) and cursor.points >= beet_points_btn.cost:
        cursor.points -= beet_points_btn.cost
        beet_points_btn.cost += beet_points_btn.cost // 2
        cursor.beet_p += 1
    if pig_vel_btn.collidepoint(pos) and cursor.points >= pig_vel_btn.cost:
        cursor.points -= pig_vel_btn.cost
        pig_vel_btn.cost += pig_vel_btn.cost // 3
        cursor.pig_v += 0.2
    if beet_buy_btn.collidepoint(pos) and cursor.points >= beet_buy_btn.cost:
        cursor.points -= beet_buy_btn.cost
        beet_buy_btn.cost *= 2
        vegie_list.append(Actor("beetroot", (random.randint(
            50, WIDTH - 50 - PANEL), random.randint(50, HEIGHT - 50))))
    if pig_buy_btn.collidepoint(pos) and cursor.points >= pig_buy_btn.cost:
        cursor.points -= pig_buy_btn.cost
        pig_buy_btn.cost *=  2
        animal = Actor("pig_down")
        animal.x = random.randint(50, WIDTH - 50 - PANEL)
        animal.y = random.randint(50, HEIGHT - 50)
        animal.vx = 0
        animal.vy = 0
        animal.type = "pig"
        animal.vegie = random.choice(vegie_list)
        animal_list.append(animal)
        cursor.beet_multiplier += 1
    if carrot_buy_btn.collidepoint(pos) and cursor.points >= carrot_buy_btn.cost:
        cursor.points -= carrot_buy_btn.cost
        carrot_buy_btn.cost *=  3
        vegie_list.append(Actor("carrot", (random.randint(
            50, WIDTH - 50 - PANEL), random.randint(50, HEIGHT - 50))))
    if carrot_points_btn.collidepoint(pos) and cursor.points >= carrot_points_btn.cost:
        cursor.points -= carrot_points_btn.cost
        carrot_points_btn.cost *=  5
        cursor.carrot_p *= 2
    if rabbit_buy_btn.collidepoint(pos) and cursor.points >= rabbit_buy_btn.cost:
        cursor.points -= rabbit_buy_btn.cost
        rabbit_buy_btn.cost *=  4
        animal = Actor("rabbit_down")
        animal.x = random.randint(50, WIDTH - 50 - PANEL)
        animal.y = random.randint(50, HEIGHT - 50)
        animal.vx = 0
        animal.vy = 0
        animal.type = "rabbit"
        animal.vegie = random.choice(vegie_list)
        animal_list.append(animal)
        cursor.carrot_multiplier += 1
    if rabbit_vel_btn.collidepoint(pos) and cursor.points >= rabbit_vel_btn.cost:
        cursor.points -= rabbit_vel_btn.cost
        rabbit_vel_btn.cost *= 3
        cursor.rabbit_v += 3
    if radish_buy_btn.collidepoint(pos) and cursor.points >= radish_buy_btn.cost:
        cursor.points -= radish_buy_btn.cost
        radish_buy_btn.cost *= 5
        vegie_list.append(Actor("radish", (random.randint(
            50, WIDTH - 50 - PANEL), random.randint(50, HEIGHT - 50))))
    if radish_points_btn.collidepoint(pos) and cursor.points >= radish_points_btn.cost:
        cursor.points -= radish_points_btn.cost
        radish_points_btn.cost += radish_points_btn.cost * 8
        cursor.radish_p *= 5
    if mouse_buy_btn.collidepoint(pos) and cursor.points >= mouse_buy_btn.cost:
        cursor.points -= mouse_buy_btn.cost
        mouse_buy_btn.cost *= 10
        animal = Actor("mouse_down")
        animal.x = random.randint(50, WIDTH - 50 - PANEL)
        animal.y = random.randint(50, HEIGHT - 50)
        animal.vx = 0
        animal.vy = 0
        animal.type = "mouse"
        animal.vegie = random.choice(vegie_list)
        animal_list.append(animal)
        cursor.all_multiplier += 1


def on_mouse_move(pos):
    cursor.pos = pos


def bot(animal):
    v = 0
    if animal.type == "pig":
        v = cursor.pig_v
    if animal.type == "rabbit":
        v = cursor.rabbit_v
    if animal.type == "mouse":
        v = cursor.mouse_v
    if animal.x - animal.vegie.x >= v:
        animal.vx = -v
        animal.vy = 0
        animal.image = animal.type + "_left"
    elif animal.vegie.x - animal.x >= v:
        animal.vx = v
        animal.vy = 0
        animal.image = animal.type + "_right"
    elif animal.y - animal.vegie.y >= v:
        animal.vx = 0
        animal.vy = -v
        animal.image = animal.type + "_up"
    elif animal.vegie.y - animal.y >= v:
        animal.vx = 0
        animal.vy = v
        animal.image = animal.type + "_down"


pygame.mouse.set_visible(False)
pgzrun.go()
