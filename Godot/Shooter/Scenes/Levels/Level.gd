extends Node2D


func _on_area_2d_body_entered(body):
	print("body has entered")
	print(body)

func _on_area_2d_body_exited(_body):
	print("body has exited")
	
