import png
import math
from flask import Flask
from flask import render_template, url_for, request, send_file

app = Flask(__name__)

def hex2rgb(value):
  value = value.lstrip('#') #strip pound sign if entered
  r = '0x'+value[:2]
  g = '0x'+value[2:4]
  b = '0x'+str(value[4:])
  rgb = (int(r, 16), int(g, 16), int(b, 16))
  return rgb


@app.route('/', methods=['POST', 'GET'])
def index():
  if request.method == 'POST':
    hexvalue = request.form['hexcode']
    alphavalue = request.form['alpha']
    r = hex2rgb(hexvalue)
    a = math.ceil(255 * (alphavalue / 100))
    # make png
    array = [[r[0], r[1], r[2], a],
             [r[0], r[1], r[2], a],
             [r[0], r[1], r[2], a],
             [r[0], r[1], r[2], a],
             [r[0], r[1], r[2], a],
             [r[0], r[1], r[2], a],
             [r[0], r[1], r[2], a],
             [r[0], r[1], r[2], a],
             [r[0], r[1], r[2], a]]

             
    png.from_array(array, 'RGBA').save("small_smiley.png")
    # create png file name
    png_file_name = hexvalue + '_' + alphavalue + '.png'
    # return png
    return send_file('small_smiley.png', attachment_filename=png_file_name, as_attachment=True)
  return render_template('base.html')

@app.route('/<hex>')
def get_color(hex):
  return render_template('color.html', hex=hex)

# def make_png(usr_hex, alpha):


if __name__ == '__main__':
  app.run()