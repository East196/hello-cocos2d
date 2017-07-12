# 地图碰撞 Map Colliders

## 概览 Overview
如果场景上有一个角色在移动，我们可以使用非连续近似的方法每帧更新其位置。

If a scene has an actor moving, we may update its position from frame to frame using the discrete approximation:

```text
velocity = velocity + acceleration * dt
position = position + velocity * dt
```

在角色没有碰到障碍物的时候，这是一个好方法。

That’s fine when the actor does not find an obstacle, like a wall.

当角色撞上了一个障碍物，我们通常希望

If there is an obstacle, we usually want to

停止位置的变换让角色能碰到障碍物但是不会和障碍物重叠

stop the position change so the actor touches the obstacle but does not overlap it.

能够感觉速度上的改变（停止？反弹？）

do something sensible with the velocity (stop ?, bounce ?).

障碍物（钉子？草？）本身做出一些反应

maybe do some action based on which obstacle (spikes ?, glass ?).

想要做到这些，我们可以使用方块代表角色和障碍物，来进行这些计算

To do this we can represent the actor and the obstacles as rects with sides parallel to the axis, and do the calculations.

地图碰撞提供了这些功能

This is what map colliders do given:

角色速度，方块之前？和实验性的方块之后？

the actor velocity, rect before and tentative rect after

包含障碍物的地图图层

a map layer that contains a number of obstacles

他将会

it will

更新速率和位置

Properly update the velocity and the position.

在察觉角色撞到障碍物的时候调用合适的方法

Call appropriate methods when it detects the actor bumped into an obstacle.

在x/y轴发生碰撞的时候做出反应
Tell if any collision in the x and / or y axis happened.

一些地图碰撞器( RectMapCollider, RectMapWithPropsCollider)适用于瓦片地图，另一些(TmxObjectMapCollider) 适用于非瓦片地图~~
While some mapcolliders are meant to be used in tiled maps ( RectMapCollider, RectMapWithPropsCollider), others (TmxObjectMapCollider) can be used with no tiles at all.

### 更新速率和位置 Properly update the velocity and the position

The position and the velocity update can be written as:
```text
vx, vy = actor.velocity

# using the player controls, gravity and other acceleration influences
# update the velocity
vx = (keyboard[key.RIGHT] - keyboard[key.LEFT]) * actor.MOVE_SPEED
vy += GRAVITY * dt
if actor.on_ground and keyboard[key.SPACE]:
    vy = actor.JUMP_SPEED

# with the updated velocity calculate the (tentative) displacement
dx = vx * dt
dy = vy * dt

# get the player's current bounding rectangle
last = actor.get_rect()

# build the tentative displaced rect
new = last.copy()
new.x += dx
new.y += dy

# account for hitting obstacles, it will adjust new and vx, vy
actor.velocity = mapcollider.collide_map(maplayer, last, new, vx, vy)

# update on_ground status
actor.on_ground = (new.y == last.y)

# update player position; player position is anchored at the center of the image rect
actor.position = new.center
```

How velocity changes in a collision is handled by method on_bump_handler(); it can be set to custom code or to one of the stock handlers:

on_bump_bounce(): Bounces when a wall is touched.
on_bump_stick(): Stops all movement when any wall is touched. (sticky bomb...).
on_bump_slide(): Blocks movement only in the axis that touched a wall. (player...).
For convenience, a stock handler can be specified at instantiation time with the velocity_on_bump parameter.

Call appropriate methods when it detects actor bumped into an obstacle

When mapcollider.collide_map detects that actor collides with obj ‘someobj’ from side ‘someside’, it will call mapcollider.collide_<someside>(someobj).

There ‘someside’ is one of ‘left’, ‘right’, ‘top’ and ‘bottom’.

This provides an opportunity to do things based on which object the actor touched, like ‘spike’ ? -> init the spikes animation and kill the actor.

Note that each mapcollider.collide_* can receive multiple calls in the same mapcollider.collide_map call.

Tell if any collision in the x and / or y axis happened

After collide_map returns, the flags mapcollider.bumped_x and mapcollider.bumped_y tells if there has been any collisions along the respective axis.

This can be handy to flip the actor’s animation direction, by example from ‘walk_left’ to ‘walk_right’.

Variants
Currently they are three map colliders variants:

RectMapCollider

Obstacles are rectangular tiles grouped into a RectMapLayer; all non empty cells are deemed solid.

implementation

RectMapWithPropsCollider

Obstacles are rectangular tiles grouped into a RectMapLayer, cells use properties “left”, “right”, “top” and “bottom” to signal which side(s) block movements.

A solid block would probably have all four sides set; a platform can set only the top so the player might jump up from underneath and pass through.

For convenience these properties would typically be set on the tiles themselves, rather than on individual cells. Of course for the cell which is the entrance to a secret area you could override a wall’s properties to set the side to False and allow ingress.

See Map, Cell and Tile Properties for information about properties.

implementation

TmxObjectMapCollider

Obstacles are TmxObjects grouped into a TmxObjectLayer, each object is meant to block movement.

A common use case is to do moving platforms in a platform game.

implementation

How to use
There are basically two ways to include this functionality into an actor class:

as a component, essentially passing (mapcollider, maplayer) in the actor’s __init__ method.
mixin style, by using RectMapCollider or a subclass as a secondary base class for the actor.
The component way is more decoupled while the Mixin style is more powerful because the collision code will have access to the entire actor through its self attribute.

To have a working instance, the behavior of the velocity in a collision must be defined, and that’s the job of the method on_bump_handler

if one of the stock on_bump_<variant> suits the requirements, suffices to write:

mapcollider.on_bump_handler = mapcollider.on_bump_<desired variant>
or passing a selector at instantiation time:

mapcollider = MapCollider(<desired variant>)
for custom behavior define on_bump_handler in a subclass and instantiate it.