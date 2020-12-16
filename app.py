from flask import Flask, request, render_template
import matplotlib.pyplot as plt
import numpy as np
import urllib
from io import BytesIO

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


# dataset
# scatter
sx1 = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 8, 8]
sy1 = [3, 2, 5, 4, 5, 2, 1, 6, 6, 10, 6, 8, 5, 6, 7, 7, 4, 8]

sx2 = [7, 7.5, 8, 8, 10, 12, 12, 13, 14, 14, 15, 16, 16, 17, 17, 18, 19, 19]
sy2 = [12, 16, 10, 12, 16, 10, 18, 14, 12, 18, 16, 15, 19, 14, 18, 14, 18, 16]

sx3 = [5, 6, 7, 8, 9, 10, 10, 12, 14, 15, 15, 16, 17, 16, 18, 19]
sy3 = [1, 2, 4, 1, 4, 2, 8, 4, 10, 6, 5, 8, 12, 3, 9, 6]
# histogram
hx1 = np.random.normal(0, 10, 1000)
hx2 = np.random.normal(8, 4, 800)
hx3 = np.random.normal(-36, 20, 900)


@app.route('/plot/scat')
def plot_scat():
    fig, ax = plt.subplots(1, 1)

    # obtain query parameters
    scat_c1 = request.args.get('scat-color1', type=str)
    scat_c2 = request.args.get('scat-color2', type=str)
    scat_c3 = request.args.get('scat-color3', type=str)
    scat_num = request.args.get('scat-num', type=int)

    # produce scatter plot(s)
    ax.scatter(sx1, sy1,  marker='o', c=scat_c1)
    if scat_num >= 2:
        ax.scatter(sx2, sy2, marker='o', c=scat_c2)
    if scat_num >= 3:
        ax.scatter(sx3, sy3, marker='o', c=scat_c3)
    png_out = BytesIO()

    # set limits
    ax.set_xlim([0, 20])
    ax.set_ylim([0, 20])

    plt.savefig(png_out, format="png", bbox_inches="tight")
    img_data = urllib.parse.quote(png_out.getvalue())

    return "data:image/png:base64," + img_data


@app.route('/plot/hist')
def plot_hist():
    fig, ax = plt.subplots(1, 1)

    # set bin width
    bins = 50

    # obtain query parameters
    hist_c1 = request.args.get('hist-color1', type=str)
    hist_c2 = request.args.get('hist-color2', type=str)
    hist_c3 = request.args.get('hist-color3', type=str)
    hist_num = request.args.get('hist-num', type=int)
    hist_alpha = request.args.get('hist-alpha-value', type=float)

    # produce histograms
    ax.hist(hx1, bins=bins, color=hist_c1, alpha=hist_alpha)
    if hist_num >= 2:
        ax.hist(hx2, bins=bins, color=hist_c2, alpha=hist_alpha)
    if hist_num >= 3:
        ax.hist(hx3, bins=bins, color=hist_c3, alpha=hist_alpha)
    png_out = BytesIO()

    plt.savefig(png_out, format="png", bbox_inches="tight")
    img_data = urllib.parse.quote(png_out.getvalue())

    return "data:image/png:base64," + img_data


@app.route('/plot/line')
def plot_line():
    fig, ax = plt.subplots(1, 1)

    # obtain query parameters
    curve1 = request.args.get('curve1', type=str)
    curve2 = request.args.get('curve2', type=str)
    curve3 = request.args.get('curve3', type=str)
    curve_types = [curve1, curve2, curve3]
    line_num = request.args.get('line-num', type=int)
    line_c1 = request.args.get('line-color1', type=str)
    line_c2 = request.args.get('line-color2', type=str)
    line_c3 = request.args.get('line-color3', type=str)
    line_colors = [line_c1, line_c2, line_c3]

    # curves
    x = np.linspace(-2, 2, 1000)
    y1 = np.sin(x)
    y2 = np.cos(x)
    y3 = np.exp(x)
    y4 = np.log(x)
    y5 = np.sinh(x)
    y6 = np.cosh(x)

    for i in range(line_num):
        if curve_types[i] == "sin":
            ax.plot(x, y1, color=line_colors[i])
        elif curve_types[i] == "cos":
            ax.plot(x, y2, color=line_colors[i])
        elif curve_types[i] == "exp":
            ax.plot(x, y3, color=line_colors[i])
        elif curve_types[i] == "log":
            ax.plot(x, y4, color=line_colors[i])
        elif curve_types[i] == "sinh":
            ax.plot(x, y5, color=line_colors[i])
        elif curve_types[i] == "cosh":
            ax.plot(x, y6, color=line_colors[i])

    png_out = BytesIO()

    plt.savefig(png_out, format="png", bbox_inches="tight")
    img_data = urllib.parse.quote(png_out.getvalue())

    return "data:image/png:base64," + img_data


if __name__ == '__main__':
    app.run(debug=True, port=5000)
