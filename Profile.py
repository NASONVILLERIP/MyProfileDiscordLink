from flask import Flask, render_template_string

app = Flask(__name__)

username = "Swiper"
profile = {
    "name": "Not Leaking",
    "bio": "I'm a Gorilla Tag Copy Modder , and I do C++.",
    "location": "Nuh-uh",
    "email": "lamarjackson123571@gmail.com"
}
links = {
    "GitHub": "https://discord.com/@m4tt3rz",
    "LinkedIn": "https://linkedin.com/in/swiper",
    "Twitter": "https://twitter.com/swiper"
}
about_me = """
<h2>About Me</h2>
<p>I am a software developer with a passion for creating web applications and learning new technologies.</p>
<p>In my free time, I enjoy reading, hiking, and exploring new places.</p>
"""

template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{{ username }}'s Website</title>
    <style>
        body { font-family: Arial, sans-serif; max-width: 800px; margin: 40px auto; padding: 0 20px; }
        header { border-bottom: 2px solid #333; padding-bottom: 10px; margin-bottom: 20px; }
        nav a { margin-right: 15px; text-decoration: none; color: #007BFF; }
        nav a:hover { text-decoration: underline; }
        section { margin-bottom: 30px; }
        ul { list-style-type: none; padding-left: 0; }
        ul li { margin-bottom: 5px; }
    </style>
</head>
<body>
    <header>
        <h1>{{ username }}</h1>
        <nav>
            <a href="/">Profile</a>
            <a href="/links">Links</a>
            <a href="/about">About Me</a>
        </nav>
    </header>

    {% block content %}{% endblock %}
</body>
</html>
"""

profile_template = """
{% extends "base.html" %}
{% block content %}
<section>
    <h2>Profile</h2>
    <p><strong>Name:</strong> {{ profile.name }}</p>
    <p><strong>Bio:</strong> {{ profile.bio }}</p>
    <p><strong>Location:</strong> {{ profile.location }}</p>
    <p><strong>Email:</strong> <a href="mailto:{{ profile.email }}">{{ profile.email }}</a></p>
</section>
{% endblock %}
"""

links_template = """
{% extends "base.html" %}
{% block content %}
<section>
    <h2>Links</h2>
    <ul>
        {% for name, url in links.items() %}
        <li><a href="{{ url }}" target="_blank" rel="noopener">{{ name }}</a></li>
        {% endfor %}
    </ul>
</section>
{% endblock %}
"""

about_template = """
{% extends "base.html" %}
{% block content %}
<section>
    {{ about_me|safe }}
</section>
{% endblock %}
"""

from flask import render_template

from jinja2 import DictLoader
app.jinja_loader = DictLoader({
    'base.html': template,
    'profile.html': profile_template,
    'links.html': links_template,
    'about.html': about_template,
})

@app.route("/")
def profile_page():
    return render_template("profile.html", username=username, profile=profile)

@app.route("/links")
def links_page():
    return render_template("links.html", username=username, links=links)

@app.route("/about")
def about_page():
    return render_template("about.html", username=username, about_me=about_me)

if __name__ == "__main__":
    app.run(debug=True)
