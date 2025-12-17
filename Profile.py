from flask import Flask, render_template_string

app = Flask(__name__)

profile = {
    "username": "Swiper",
    "profile_pic": "https://example.com/path/to/profile.jpg",  # Replace with your image URL
    "links": {
        "LinkedIn": "https://linkedin.com/in/swiper",
        "Discord": "https://discord.com/@Swiperrrrrrrr"
    },
    "about_me": """
    <p>Hello! I'm Swiper. Welcome to my personal site.</p>
    <p>I am passionate about coding and web development.</p>
    """
}

HTML_TEMPLATE = """
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8" />
    <title>{{ username }}'s Profile</title>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;600&display=swap');
        * {
            margin: 0; padding: 0; box-sizing: border-box;
        }
        body {
            font-family: 'Poppins', sans-serif;
            background: linear-gradient(135deg, #6B73FF 0%, #000DFF 100%);
            color: #fff;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            padding: 20px;
        }
        .container {
            background: rgba(255, 255, 255, 0.1);
            border-radius: 16px;
            width: 100%;
            max-width: 480px;
            box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
            backdrop-filter: blur(10px);
            -webkit-backdrop-filter: blur(10px);
            padding: 30px 40px;
            text-align: center;
        }
        img {
            width: 140px;
            height: 140px;
            object-fit: cover;
            border-radius: 50%;
            border: 4px solid #fff;
            box-shadow: 0 4px 15px rgba(255,255,255,0.3);
            margin-bottom: 20px;
            transition: transform 0.3s ease;
        }
        img:hover {
            transform: scale(1.05);
        }
        h1 {
            font-weight: 600;
            font-size: 2.8rem;
            margin-bottom: 10px;
            text-shadow: 0 2px 6px rgba(0,0,0,0.3);
        }
        .links {
            margin: 25px 0;
            display: flex;
            justify-content: center;
            gap: 20px;
        }
        .links a {
            background: #fff;
            color: #000DFF;
            padding: 12px 18px;
            border-radius: 40px;
            font-weight: 600;
            text-decoration: none;
            box-shadow: 0 4px 12px rgba(255,255,255,0.35);
            transition: background-color 0.3s ease, color 0.3s ease;
        }
        .links a:hover {
            background: #000DFF;
            color: #fff;
            box-shadow: 0 6px 20px rgba(0,13,255,0.75);
        }
        .about {
            font-weight: 300;
            font-size: 1.1rem;
            line-height: 1.6;
            border-top: 1px solid rgba(255,255,255,0.3);
            padding-top: 20px;
            margin-top: 20px;
            text-align: left;
            color: #e0e0e0;
            user-select: text;
        }
        @media (max-width: 520px) {
            .container {
                padding: 20px;
            }
            h1 {
                font-size: 2rem;
            }
            .links {
                flex-direction: column;
                gap: 15px;
            }
            .links a {
                font-size: 1rem;
                padding: 10px 0;
            }
            .about {
                font-size: 1rem;
                text-align: center;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <img src="{{ profile_pic }}" alt="Profile Picture" loading="lazy" />
        <h1>{{ username }}</h1>
        <div class="links">
            {% for name, url in links.items() %}
            <a href="{{ url }}" target="_blank" rel="noopener noreferrer">{{ name }}</a>
            {% endfor %}
        </div>
        <div class="about">
            {{ about_me|safe }}
        </div>
    </div>
</body>
</html>
"""

@app.route("/")
def profile_page():
    return render_template_string(
        HTML_TEMPLATE,
        username=profile["username"],
        profile_pic=profile["profile_pic"],
        links=profile["links"],
        about_me=profile["about_me"],
    )


if __name__ == "__main__":
    app.run(debug=True)
