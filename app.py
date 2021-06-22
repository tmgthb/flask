from flask import Flask, request, render_template
import os
from bokeh.embed import components
from bokeh.plotting import figure
from bokeh.resources import INLINE
from bokeh.util.string import encode_utf8
from bokeh.layouts import row
from bokeh.layouts import gridplot
from bokeh.layouts import layout
from bokeh.palettes import Spectral6
from bokeh.models import ColumnDataSource
from bokeh.models import HoverTool, WheelZoomTool, BoxZoomTool, LassoSelectTool
from bokeh.models.widgets import Panel, Tabs, Toggle, TextInput
from bokeh.io import output_notebook, show
from bokeh.layouts import column  

port = int(os.environ.get("PORT", 5000))

app = Flask(__name__)

@app.route('/')
def home():
    return 'Start Page'

@app.route('/info/')
def info():
    return render_template('info.html')

@app.route('/dashboard')
def dashboard():
    x1=[2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019]
    y1=[99.5, 99.3, 98.5, 97.0, 96, 94, 84, 55, 35, ]
    x2=[2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019]
    y2=[0.5, 0.7, 1.5, 3, 4, 6, 16, 45, 65, ]
    volume =  {'x1_volume': x1,
                    'y1_volume': y1,
                    'x2_volume': x2,
                    'y2_volume': y2}
    
    volume_01 =ColumnDataSource(volume)
        
    fig = figure(title="Old vs New", x_axis_label='Year', y_axis_label='%', plot_width=1600, plot_height=800)
    fig.background_fill_color = "white"
    fig.line(x='x1_volume', y='y1_volume', line_color="#36abb5", line_width=3, line_alpha=0.4, legend='Old', source=volume_01)  
    fig.line(x='x2_volume', y='y2_volume', line_color="#ed5565", line_width=3, line_alpha=0.4, legend='New', source=volume_01, hover_color="purple")
    # https://www.color-hex.com/color-palette/30415
    

    fig.add_tools(HoverTool(tooltips = [('Year', '@x1_volume'),
                             ('Volume change old:', '@y1_volume%'),
                             ('Volume change new:', '@y2_volume%')]), WheelZoomTool(), BoxZoomTool(), LassoSelectTool())

    
    
    
    tab_a_1 = Panel(child=fig, title="Old vs New status")

    # grab the static resources
    js_resources = INLINE.render_js()
    css_resources = INLINE.render_css()

    # render template
    script, div = components(tabs_a)
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


