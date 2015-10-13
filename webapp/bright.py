#!/usr/bin/env python
#encoding=utf-8

from bottle import run, get, post, request
import LED

meta = '<meta name="viewport" content="width=device-width,initial-scale=1.0,user-scalable=yes">'

form = '''
<form action="/bright" method="post">
<input type="range" name="brightvalue" value="0" min="0" max="100">
<input type="submit" value="Bright">
</form>
'''
html = meta + form
led_instance = LED.led_brightness(18)

@get('/bright')
def bright():
	return html

@post('/bright')
def do_bright():
	sliderValue = request.forms.get('brightvalue')
	led_instance.duty(int(sliderValue))
	return '%s<br>%s' % (sliderValue, html)

run(host='192.168.18.101', port=8080, debug=True)
