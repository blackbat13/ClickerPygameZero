import pgzrun
import random
import pygame

TITLE = "Pig Hunt"
WIDTH = 1200
HEIGHT = 800
MARGIN = 400

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

beet_buy_btn = Actor("button")
beet_buy_btn.x = WIDTH - (MARGIN / 2)
beet_buy_btn.y = 50
beet_buy_btn.cost = 5

beet_points_btn = Actor("button")
beet_points_btn.x = WIDTH - (MARGIN / 2)
beet_points_btn.y = 150
beet_points_btn.cost = 10
beet_points_btn.points = 1

pig_buy_btn = Actor("button")
pig_buy_btn.x = WIDTH - (MARGIN / 2)
pig_buy_btn.y = 250
pig_buy_btn.cost = 100

pig_vel_btn = Actor("button")
pig_vel_btn.x = WIDTH - (MARGIN / 2)
pig_vel_btn.y = 350
pig_vel_btn.cost = 5
pig_vel_btn.v = 3.0

carrot_buy_btn = Actor("button")
carrot_buy_btn.x = WIDTH - (MARGIN / 2)
carrot_buy_btn.y = 450
carrot_buy_btn.cost = 20

carrot_points_btn = Actor("button")
carrot_points_btn.x = WIDTH - (MARGIN / 2)
carrot_points_btn.y = 550
carrot_points_btn.cost = 50
carrot_points_btn.points = 5

rabbit_buy_btn = Actor("button")
rabbit_buy_btn.x = WIDTH - (MARGIN / 2)
rabbit_buy_btn.y = 650
rabbit_buy_btn.cost = 500

rabbit_vel_btn = Actor("button")
rabbit_vel_btn.x = WIDTH - (MARGIN / 2)
rabbit_vel_btn.y = 750
rabbit_vel_btn.cost = 300
rabbit_vel_btn.v = 20


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
    if cursor.points <= 10**9:
        screen.draw.text(f"{cursor.points:,}$", center=(
            (WIDTH-MARGIN) / 2, 50), fontsize=60, color="#fdee00")
    else:
        screen.draw.text(f"{cursor.points:.2e}$", center=(
            (WIDTH-MARGIN) / 2, 50), fontsize=60, color="#fdee00")


def draw_buttons():
    beet_points_btn.draw()
    screen.draw.text(f"Beet points: {beet_points_btn.points}->{beet_points_btn.points+1}\n{beet_points_btn.cost:,}$",
                     center=beet_points_btn.pos, fontsize=25, color="white")
    pig_vel_btn.draw()
    screen.draw.text(f"Pig speed: {pig_vel_btn.v:.1f}->{(pig_vel_btn.v+0.2):.1f}\n{pig_vel_btn.cost:,}$",
                     center=pig_vel_btn.pos, fontsize=25, color="white")
    beet_buy_btn.draw()
    screen.draw.text(f"New beet\n{beet_buy_btn.cost:,}$",
                     center=beet_buy_btn.pos, fontsize=25, color="white")
    pig_buy_btn.draw()
    screen.draw.text(f"New pig\n{pig_buy_btn.cost:,}$",
                     center=pig_buy_btn.pos, fontsize=25, color="white")
    carrot_buy_btn.draw()
    screen.draw.text(f"New carrot\n{carrot_buy_btn.cost:,}$",
                     center=carrot_buy_btn.pos, fontsize=25, color="white")
    carrot_points_btn.draw()
    screen.draw.text(f"Carrot points: {carrot_points_btn.points}->{carrot_points_btn.points*2}\n{carrot_points_btn.cost:,}$",
                     center=carrot_points_btn.pos, fontsize=25, color="white")
    rabbit_buy_btn.draw()
    screen.draw.text(f"New rabbit\n{rabbit_buy_btn.cost:,}$",
                     center=rabbit_buy_btn.pos, fontsize=25, color="white")
    rabbit_vel_btn.draw()
    screen.draw.text(f"Rabbit speed: {rabbit_vel_btn.v}->{rabbit_vel_btn.v + 5}\n{rabbit_vel_btn.cost:,}$",
                     center=rabbit_vel_btn.pos, fontsize=25, color="white")

def update():
    for animal in animal_list:
        animal.x += animal.vx
        animal.y += animal.vy

        bot(animal)

        for vegie in vegie_list[:]:
            if animal.colliderect(vegie):
                vegie.x = random.randint(50, WIDTH - 50 - MARGIN)
                vegie.y = random.randint(50, HEIGHT - 50)
                if vegie.image == "beetroot":
                    cursor.points += beet_points_btn.points
                if vegie.image == "carrot":
                    cursor.points += carrot_points_btn.points
                animal.vegie = random.choice(vegie_list)


def on_mouse_down(pos):
    if beet_points_btn.collidepoint(pos) and cursor.points >= beet_points_btn.cost:
        cursor.points -= beet_points_btn.cost
        beet_points_btn.cost += beet_points_btn.cost // 2
        beet_points_btn.points += 1
    if pig_vel_btn.collidepoint(pos) and cursor.points >= pig_vel_btn.cost:
        cursor.points -= pig_vel_btn.cost
        pig_vel_btn.cost += pig_vel_btn.cost // 3
        pig_vel_btn.v += 0.2
    if beet_buy_btn.collidepoint(pos) and cursor.points >= beet_buy_btn.cost:
        cursor.points -= beet_buy_btn.cost
        beet_buy_btn.cost += beet_buy_btn.cost
        vegie_list.append(Actor("beetroot", (random.randint(
            50, WIDTH - 50 - MARGIN), random.randint(50, HEIGHT - 50))))
    if pig_buy_btn.collidepoint(pos) and cursor.points >= pig_buy_btn.cost:
        cursor.points -= pig_buy_btn.cost
        pig_buy_btn.cost += pig_buy_btn.cost * 2
        animal = Actor("pig_down")
        animal.x = random.randint(50, WIDTH - 50 - MARGIN)
        animal.y = random.randint(50, HEIGHT - 50)
        animal.vx = 0
        animal.vy = 0
        animal.type = "pig"
        animal.vegie = random.choice(vegie_list)
        animal_list.append(animal)
    if carrot_buy_btn.collidepoint(pos) and cursor.points >= carrot_buy_btn.cost:
        cursor.points -= carrot_buy_btn.cost
        carrot_buy_btn.cost += carrot_buy_btn.cost * 3
        vegie_list.append(Actor("carrot", (random.randint(
            50, WIDTH - 50 - MARGIN), random.randint(50, HEIGHT - 50))))
    if carrot_points_btn.collidepoint(pos) and cursor.points >= carrot_points_btn.cost:
        cursor.points -= carrot_points_btn.cost
        carrot_points_btn.cost += carrot_points_btn.cost * 5
        carrot_points_btn.points *= 2
    if rabbit_buy_btn.collidepoint(pos) and cursor.points >= rabbit_buy_btn.cost:
        cursor.points -= rabbit_buy_btn.cost
        rabbit_buy_btn.cost += rabbit_buy_btn.cost * 4
        animal = Actor("rabbit_down")
        animal.x = random.randint(50, WIDTH - 50 - MARGIN)
        animal.y = random.randint(50, HEIGHT - 50)
        animal.vx = 0
        animal.vy = 0
        animal.type = "rabbit"
        animal.vegie = random.choice(vegie_list)
        animal_list.append(animal)
    if rabbit_vel_btn.collidepoint(pos) and cursor.points >= rabbit_vel_btn.cost:
        cursor.points -= rabbit_vel_btn.cost
        rabbit_vel_btn.cost += rabbit_vel_btn.cost * 3
        rabbit_vel_btn.v += 5


def on_mouse_move(pos):
    cursor.pos = pos


def bot(animal):
    v = 0
    if animal.type == "pig":
        v = pig_vel_btn.v
    if animal.type == "rabbit":
        v = rabbit_vel_btn.v
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
