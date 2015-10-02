#!/usr/bin/env python
#encoding=utf-8

from bottle import run, get, post, request
import web_LED

meta = '<meta name="viewport" content="width=device-width,initial-scale=1.0,user-scalable=yes">'

form = '''
<form action="/blink" method="post">
<input name="on" value="ON" type="submit"/>
<input name="off" value="OFF" type="submit"/>
</form>
'''
html = meta + form

@get('/blink')
def blink():
	return html

@post('/blink')
def do_blink():
	onValue = request.forms.get('on')
	offValue = request.forms.get('off')
	if onValue and not offValue:
		print 'LED ON'
		web_LED.led_on(18)
	elif not onValue and offValue:
		print 'LED OFF'
		web_LED.led_off(18)

	return html

run(host='192.168.0.22', port=8080, debug=True)
