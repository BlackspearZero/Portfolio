extends Sprite2D

var pos: Vector2 = Vector2.ZERO
const speed: int = 1
var test_scale: int = 1

func _ready():
	position = Vector2(100,200)
	position = pos

	test_scale = 2
	scale = Vector2(test_scale, test_scale)

func _process(delta):
	pos.x += speed
	position = pos
