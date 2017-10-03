import itach as i

commands = {'toggle_power':"sendir,1:3,7,40064,1,1,96,23,49,23,25,23,49,23,25,23,49,23,25,23,25,23,25,23,25,23,25,23,25,23,49,23,49,23,25,23,25,908,97,23,49,23,25,23,49,23,25,23,49,23,25,23,25,23,25,23,25,23,25,23,25,23,49,23,49,23,25,23,25,908,97,23,49,23,25,23,49,23,25,23,49,23,25,23,25,23,25,23,25,23,25,23,25,23,49,23,49,23,25,23,25,908,97,23,49,23,25,23,49,23,25,23,49,23,25,23,25,23,25,23,25,23,25,23,25,23,49,23,49,23,25,23,25,908,97,23,49,23,25,23,49,23,25,23,49,23,25,23,25,23,25,23,25,23,25,23,25,23,49,23,49,23,25,23,25,908,97,23,49,23,25,23,49,23,25,23,49,23,25,23,25,23,25,23,25,23,25,23,25,23,49,23,49,23,25,23,25,4000",
			'input_sat':"sendir,1:3,1,40192,1,1,97,23,49,23,49,23,25,23,25,23,25,23,25,23,25,23,25,23,25,23,25,23,25,23,49,23,49,23,25,23,49,898,96,23,49,23,49,23,25,23,25,23,25,23,25,23,25,23,25,23,25,23,25,23,25,23,49,23,49,23,25,23,49,888,96,23,49,23,49,23,25,23,25,23,25,23,25,23,25,23,25,23,25,23,25,23,25,23,49,23,49,23,25,23,49,921,97,23,49,23,49,23,25,23,25,23,25,23,25,23,25,23,25,23,25,23,25,23,25,23,49,23,49,23,25,23,49,921,97,23,49,23,49,23,25,23,25,23,25,23,25,23,25,23,25,23,25,23,25,23,25,23,49,23,49,23,25,23,49,921,97,23,49,23,49,23,25,23,25,23,25,23,25,23,25,23,25,23,25,23,25,23,25,23,49,23,49,23,25,23,49,921,97,23,49,23,49,23,25,23,25,23,25,23,25,23,25,23,25,23,25,23,25,23,25,23,49,23,49,23,25,23,49,4000",
			'input_tv':"sendir,1:3,1,40192,1,1,97,23,25,23,49,23,25,23,49,23,25,23,49,23,49,23,25,23,25,23,25,23,25,23,49,23,49,23,25,23,25,874,96,23,25,23,49,23,25,23,49,23,25,23,49,23,49,23,25,23,25,23,25,23,25,23,49,23,49,23,25,23,25,864,96,23,25,23,49,23,25,23,49,23,25,23,49,23,49,23,25,23,25,23,25,23,25,23,49,23,49,23,25,23,25,897,97,23,25,23,49,23,25,23,49,23,25,23,49,23,49,23,25,23,25,23,25,23,25,23,49,23,49,23,25,23,25,897,97,23,25,23,49,23,25,23,49,23,25,23,49,23,49,23,25,23,25,23,25,23,25,23,49,23,49,23,25,23,25,897,97,23,25,23,49,23,25,23,49,23,25,23,49,23,49,23,25,23,25,23,25,23,25,23,49,23,49,23,25,23,25,897,97,23,25,23,49,23,25,23,49,23,25,23,49,23,49,23,25,23,25,23,25,23,25,23,49,23,49,23,25,23,25,4000",
			'input_bd':"sendir,1:3,1,40192,2,1,97,23,25,23,49,23,49,23,25,23,49,23,25,23,25,23,25,23,25,23,25,23,25,23,49,23,25,23,25,23,25,23,49,23,25,23,49,23,25,23,25,628,96,23,25,23,49,23,49,23,25,23,49,23,25,23,25,23,25,23,25,23,25,23,25,23,49,23,25,23,25,23,25,23,49,23,25,23,49,23,25,23,25,624,96,23,25,23,49,23,49,23,25,23,49,23,25,23,25,23,25,23,25,23,25,23,25,23,49,23,25,23,25,23,25,23,49,23,25,23,49,23,25,23,25,660,97,23,25,23,49,23,49,23,25,23,49,23,25,23,25,23,25,23,25,23,25,23,25,23,49,23,25,23,25,23,25,23,49,23,25,23,49,23,25,23,25,660,97,23,25,23,49,23,49,23,25,23,49,23,25,23,25,23,25,23,25,23,25,23,25,23,49,23,25,23,25,23,25,23,49,23,25,23,49,23,25,23,25,4000",
			'toggle_mute':"sendir,1:3,1,40192,1,1,97,23,25,23,25,23,49,23,25,23,49,23,25,23,25,23,25,23,25,23,25,23,25,23,49,23,49,23,25,23,25,912,96,23,25,23,25,23,49,23,25,23,49,23,25,23,25,23,25,23,25,23,25,23,25,23,49,23,49,23,25,23,25,912,96,23,25,23,25,23,49,23,25,23,49,23,25,23,25,23,25,23,25,23,25,23,25,23,49,23,49,23,25,23,25,934,97,23,25,23,25,23,49,23,25,23,49,23,25,23,25,23,25,23,25,23,25,23,25,23,49,23,49,23,25,23,25,935,97,23,25,23,25,23,49,23,25,23,49,23,25,23,25,23,25,23,25,23,25,23,25,23,49,23,49,23,25,23,25,935,97,23,25,23,25,23,49,23,25,23,49,23,25,23,25,23,25,23,25,23,25,23,25,23,49,23,49,23,25,23,25,4000",
			'volume_up':"sendir,1:3,1,40192,1,1,97,23,25,23,25,23,49,23,25,23,49,23,25,23,25,23,25,23,25,23,25,23,25,23,49,23,49,23,25,23,25,912,96,23,25,23,25,23,49,23,25,23,49,23,25,23,25,23,25,23,25,23,25,23,25,23,49,23,49,23,25,23,25,912,96,23,25,23,25,23,49,23,25,23,49,23,25,23,25,23,25,23,25,23,25,23,25,23,49,23,49,23,25,23,25,934,97,23,25,23,25,23,49,23,25,23,49,23,25,23,25,23,25,23,25,23,25,23,25,23,49,23,49,23,25,23,25,935,97,23,25,23,25,23,49,23,25,23,49,23,25,23,25,23,25,23,25,23,25,23,25,23,49,23,49,23,25,23,25,935,97,23,25,23,25,23,49,23,25,23,49,23,25,23,25,23,25,23,25,23,25,23,25,23,49,23,49,23,25,23,25,4000",
			'volume_down':"sendir,1:3,1,40192,1,1,97,23,25,23,25,23,49,23,25,23,49,23,25,23,25,23,25,23,25,23,25,23,25,23,49,23,49,23,25,23,25,912,96,23,25,23,25,23,49,23,25,23,49,23,25,23,25,23,25,23,25,23,25,23,25,23,49,23,49,23,25,23,25,912,96,23,25,23,25,23,49,23,25,23,49,23,25,23,25,23,25,23,25,23,25,23,25,23,49,23,49,23,25,23,25,934,97,23,25,23,25,23,49,23,25,23,49,23,25,23,25,23,25,23,25,23,25,23,25,23,49,23,49,23,25,23,25,935,97,23,25,23,25,23,49,23,25,23,49,23,25,23,25,23,25,23,25,23,25,23,25,23,49,23,49,23,25,23,25,935,97,23,25,23,25,23,49,23,25,23,49,23,25,23,25,23,25,23,25,23,25,23,25,23,49,23,49,23,25,23,25,4000"
			}

def send_command(command):
	return i.send_command(commands[command])

def toggle_power():
	return send_command('toggle_power')

def toggle_mute():
	return send_command('toggle_mute')

def volume_up():
	return send_command('toggle_mute')

def volume_down():
	return send_command('toggle_mute')

def volume_repeat(number):
	number = (number + 1)/2
	x = 0
	if number < 0:
		while x > number:
			volume_down()
			x -= 1
	elif number > 0:
		while x < number:
			volume_up()
			x +=1
	else:
		return "error"
	return "completeir"

def set_input(input):
	input = input.upper()
	if input == 'SAT':
		return send_command('input_sat')
	elif input == 'TV':
		return send_command('input_tv')
	elif input == 'BD':
		return send_command('input_bd')
	return "error"

def set_ip(ip):
	return i.set_ip(ip)

if __name__ == "__main__":
	# Example
	stereo.set_ip('192.168.1.12')
	stereo.toggle_power()
	stereo.volume_repeat(30)
