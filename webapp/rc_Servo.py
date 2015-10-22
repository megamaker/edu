#!/usr/bin/env python
#encoding=utf-8

from bottle import run, get, post, request

meta = '<meta name="viewport" content="width=device-width,initial-scale=2.0,user-scalable=no">'
body = '''
<form action="/servo" method="post">
	<button type="submit" name="side" value="L">-</button>
	<button type="submit" name="side" value="R">+</button>
</form>
'''
html = '<head>%s</head><body>%s</body>' % (meta, body)

@get('/servo')
def servo():
	return html

@post('/servo')
def do_servo():
	path = '/home/pi/dev/src/webapp'
	f = open('%s/servoAngle' % path, 'r')
	angle = int(f.readline().strip())
	f.close()

	side = request.forms.get('side')
	if side == 'L':
		if angle == -90: pass
		else: angle -= 45
	elif side == 'R':
		if angle == 90: pass
		else: angle += 45
	print side, angle
	
	f = open('%s/servoAngle' % path, 'w')
	f.write(str(angle))
	f.close()
	f = open('%s/servoStatus' % path, 'w')
	f.write('1')
	f.close()

	return html

run(host='192.168.18.101', port=8080, debug=True)
