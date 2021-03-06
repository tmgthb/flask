from flask import Flask, request, render_template
import os
from bokeh.embed import components
from bokeh.plotting import figure
from bokeh.resources import INLINE
from bokeh.util.string import encode_utf8  

port = int(os.environ.get("PORT", 5000))

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/gptneo/')
def gptneo():
    return render_template('gptneo.html')

@app.route('/info/')
def info():
    return render_template('info.html')

@app.route('/dashboard')
def dashboard():

    # init a basic bar chart:
    # http://bokeh.pydata.org/en/latest/docs/user_guide/plotting.html#bars
    fig = figure(plot_width=600, plot_height=600)
    fig.background_fill_color = "white"
    fig.vbar(
        x=[2018, 2019, 2020, 2021],
        width=0.5,
        bottom=0,
        top=[2.7, 0.2, 2.6, 6.9],
        color='navy'
    )

    # grab the static resources
    js_resources = INLINE.render_js()
    css_resources = INLINE.render_css()

    # render template
    script, div = components(fig)
    html = render_template(
        'dashboard.html',
        plot_script=script,
        plot_div=div,
        js_resources=js_resources,
        css_resources=css_resources,
    )
    return encode_utf8(html)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port) #https://github.com/dpgaspar/Flask-AppBuilder/issues/733#issuecomment-379009480
    #app.run()


