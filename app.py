from flask import Flask, request, render_template, redirect, url_for, session, Markup
from function import get_title_content_img
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)

@app.route('/',methods=['GET','POST'])
def index():
    if request.method == 'POST':
        url = request.form.get('url')
        title, content, img = get_title_content_img(url)
        session['url'] = url
        session['title'] = title
        session['content'] = content
        session['img'] = img
        html = Markup(f'<blockquote class="blogcard" style="width:auto;border:1px solid #aaa;margin:1em 0;padding:1em;line-height:1.4;text-align:left;background:#fff;"><a href="{url}" target="_blank" style="display:block;text-decoration:none;"><div style="width:100%;margin:0 0 .5em;"><span style="font-size:18px;font-weight:700;color:#333">{title}</span></div><div style="min-height:100px;"><div style="float:left;width:100px;height:100px;margin:0 .5em;position:relative;"><img src="{img}" alt="thumbnail" style="display:block;margin:0;padding:0;width:100%;height:auto;border:none;position:absolute;top:50%;transform:translateY(-50%);"/></div><div style="padding:0 .5em;overflow:hidden;text-overflow:ellipsis;"><span style="font-size:14px;font-weight:400;color:#666">{content}</span><br/><span style="font-size:12px;font-weight:400;color:#373">https://lets-hack.tech/programming/languages/python/beautifulsoup/</span></div></div></a></blockquote>')
        session['html'] = html
        return redirect(url_for('result'))
    else:
        return render_template('index.html')

@app.route('/result')
def result():
    html = session['html']
    return render_template('result.html', preview=html)

if __name__ == '__main__':
    app.run(debug=True)