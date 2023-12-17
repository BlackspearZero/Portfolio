extends CharacterBody2D

var can_laser: bool = true
var can_grenade: bool = true


func _process(_delta):
	
	#input
	var direction = Input.get_vector("left","right","up","down")
	velocity = direction * 500
	move_and_slide()
	
	if Input.is_action_pressed("primary action") and can_laser:
		print("Shoot Laser")
		can_laser = false
		$LaserTimer.start()
		
	if Input.is_action_pressed("secondary action") and can_grenade:
		print("Shoot Grenade")
		can_grenade = false
		$GrenadeTimer.start()


func _on_laser_timer_timeout():
	can_laser = true


func _on_grenade_timer_timeout():
	can_grenade = true
	