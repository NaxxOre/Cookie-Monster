from flask import Flask, request, redirect, make_response, render_template_string

app = Flask(__name__)
app.secret_key = 'super_secret_ctf_key_123!'

LOGIN_HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Cookie Monster</title>
</head>
<body>
    <h1>Please log in to eat admin cookie 🍪</h1>
    {% if message %}
        <p style="color: red;">{{ message }}</p>
    {% endif %}
    <form method="POST">
        <label>Username:</label>
        <input type="text" name="username"><br>
        <label>Password:</label>
        <input type="password" name="password"><br>
        <button type="submit">Login</button>
    </form>
</body>
</html>
"""

STORY_HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Not Admin</title>
</head>
<body>
    <h2>I am not Admin but I can tell you a good story...</h2>
    <p>
        Thomas Mcoy, no second C, is a name you’ve probably never seen. Maybe you’ve spotted “Tommy M.” buried in the acknowledgments of a bestseller or scrawled on a Starbucks cup while he tapped away on a Chromebook in a corner booth. But you won’t find his name on a book cover.

Tommy, you see, is the best ghostwriter in America. Maybe the world.

The book about the astronaut who battled alcoholism? Tommy.

The one by the Yankee who named names with too much pride? Also Tommy.

Fourteen CEOs, each with a different spin on leadership: “The Pyramid of Power,” “The Confidence Column,” “The Effectiveness Spectrum”? All Tommy’s inventions.

He wrote the last thirteen Wingnut Wilson thrillers and four of the last five presidential memoirs. He even filled in on the Wilson the Dog comic strip for two months in 2006 when Dan Harkins had shingles.

He could write anything except, apparently, his own story.

Which is how I got involved.

I’m Ted McGinn. Adjunct professor at a third-tier state school in New Jersey. Once upon a time, I was a go-to guy for media tie-ins. I wrote five mysteries based on Police: NY, two sci-fi trilogies for the Planet Force 9 franchise, and twelve paperback romances spun off from the soap opera Almost Kissed. Hack work, sure, but it paid for some decent real estate in Jersey City and gave me just enough credibility to teach people who still believed writing could save them.

Then one Thursday morning, I got a call.

“Is this Professor Ted McGinn?”

The voice was gravelly, amused, and somehow familiar.

“This is Thomas Mcoy. I need your help.”

We met at a diner off Route 17, where the booths still had real leather and the waitresses called everyone “hon.” Tommy was already seated, a half-empty coffee mug in front of him and a yellow legal pad filled with scribbles.

He looked like someone’s retired uncle, part office job, part Little League coach. Heavy black glasses hiding heavier eyes, a windbreaker, and a Yankees hat that had seen better days suggested nothing of his bibliography. The only giveaway was the pen. Montblanc. Heavy. Glossy. Like a knife someone meant to keep sharpened. A gift, I assumed, from one of his famous friends.

“You’re taller than I thought,” he said, not looking up.

“I get that a lot,” I said, which I don’t.

He gestured to the seat across from him. “Thanks for coming. I know this is weird.”

“Weird’s relative,” I said. “You wrote the Secretary of Agriculture’s memoir, didn’t you?”

“Ghosted it, yeah,” he said. “But this time I’m trying to do something different.”

He slid a thin folder across the table. Inside was a rough outline: Early Life, The Work, Regret, Maybe Love? Each section had three or four bullet points, but they were vague, hesitant. The notes of a man who’d spent a lifetime writing other people’s stories and now had no idea how to tell his own.

“You said on the phone you had writer’s block,” I said.

“It’s worse than that,” he said. “It’s like I don’t exist unless I write for someone else. I can’t find the angle on myself. Everything I start sounds fake or pompous or like a press release.”

“And you want me to...?”

“Help me find the thread,” he said. “You wrote this line in The Interrupted Vacation, about how love perseveres, even through regret. That one got under my skin. You ever read something and wish you wrote it yourself?”

I shrugged. “I don’t read many soap opera tie-ins.”

Tommy smiled. “You’ve never been stuck for two days in a Romanian airport with no cell service and a newsstand where the only book in English you didn’t write is The Interrupted Vacation?”

“That’s the kind of irony I wish my students understood,” I joked.

The waitress came by with coffee. He ordered another black. I asked for a Sprite and a ham and cheese on rye.

“You know,” I said, “I’m still trying to figure out why you called me. There are better writers. Cleaner prose. Bigger names.”

“Maybe. But none of them know how to get past the cornball and hit the nerve,” he said. “Your books have heart. Even when they’re ridiculous.”

“That’s generous,” I said, unsure whether I was being complimented or insulted.

He looked up at me then, and his voice softened. “It’s not. I’ve spent my whole life writing what other people want. You wrote what someone needed.”

We sat with that.

Then he added, “Besides, there’s something about you. Like we’ve met before.”

I gave him a look.

He backtracked. “Not literally. Just… something about the way you write feels familiar.”

That should have pinged something. Instead, I let it pass.

“I want this to be the one they put my name on,” he said quietly.

I nodded. “Then let’s get started.”

We began the next morning. Tommy insisted we work analog. No laptops. Just pens, legal pads, and the occasional Post-it war on the kitchen table.

His outline became our map. We started with Early Life, but every time I asked a question, he swerved.

“I could tell you about my childhood,” he said, “but it’s all boilerplate. Quiet blue-collar father, complicated mother. First Communion. My sister was nice to me; she eventually moved to Chicago and married a banker. We see each other every few years at our cousins’ kids' weddings. Move along.”

“So, nothing formative?” I asked. “No school suspensions? No heartbreaks? No weird obsessions with volcanoes or frogs?”

He cracked half a smile. “I preferred libraries to people. That’s as formative as it gets. With a 4.0 and not many friends, I went to Holy Cross when it was still boys, and majored in English and Theology. I thought about becoming a priest but couldn’t write homilies.”

“You couldn’t write homilies?” I said. “That’s your line?”

He raised an eyebrow. “Preaching is harder than people think.”

“I’m not disagreeing. I just didn’t expect a guy who wrote My Quarterback Mind to be so... ecclesiastical.”

He actually laughed at that. “We contain multitudes.”

We moved on to The Work, where he came alive. He mimicked the authors he’d ghosted: the breathy Hollywood memoirist, the grizzled quarterback, and the spiritual CEO who talked about leverage and mindfulness in the same sentence. It was uncanny and often hilarious.

I’d start laughing, and he’d crack up too. <a href="/4dm1n" hidden></a> But then he’d go quiet. Not sad, just... emptied.

“You okay?” I asked one afternoon after he nailed a perfect impression of the “faith-based space entrepreneur.”

“I’m fine,” he said. “This part’s just muscle memory.”

“Then what’s next?”

He glanced at the outline.

“Regret,” he said, and stood up to make more coffee.

A week in, I’d had enough.

“You know,” I said, “if you want this book to mean something, you’re going to have to stop hiding behind other people’s voices.”

He stared at me. “You think I’m hiding?”

“I think you’re performing.”

He didn’t argue. He rubbed his face and said, “You ever leave a story out of fear?”

“Every writer does.”

“Yeah. Well. Sometimes the stories I didn’t write were the ones that aged the worst.”

That night over dinner, he told me about a son he had never met. Just floated it out, mid-salad.

“His name was Eddie,” he said.

“You’re just dropping that in now?”

“I don’t know what I’m doing,” he said, poking at his food. “That’s why you’re here.”

I nodded, writing the name down carefully. Then I looked at him, not as a project or paycheck, but as a man trying to say something true for once.

Later, I found a Post-it on my legal pad that I hadn’t written.

You only get to rewrite the past once. Make it count.

The next morning, I brought it up.

“That Romanian airport story, what were you reading before The Interrupted Vacation saved you?”

He didn’t look up from his notebook.

“I’ve never been to Romania.”

I blinked. “But that’s what you said.”

He waved a hand like brushing away a gnat. “Oh, right. No, I just made that up. It sounded better than saying I found it in a used bookstore in Weehawken.”

It sounded offhand. But something cracked. Not a lie, a fracture in the façade. A crease in the page before the story folds.

It happened late one night. We hadn’t spoken in over an hour. Tommy stood at the counter, writing. I stayed at the table, pretending to sort through interview notes, but mostly watching him.

Normally, he’d scribble a few lines, cross them out, swear softly, and start over. But not this time. This time he just kept going, steady, focused, quiet. When he finally set the pen down, his hand hovered over the page for a second like he wasn’t sure whether to give it up.

He walked over and handed me five handwritten pages. No title. No chapter number. Just unfiltered prose.

I left because I didn’t know how to stay.

I watched from further than I should have.      
    </p>
</body>
</html>
"""

ROBOT_HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Robot</title>
    <style>
        body {
            background: url('https://example.com/robot.jpg') no-repeat center center;
            background-size: cover;
            text-align: center;
            padding-top: 20%;
        }
    </style>
</head>
<body>
    <h1>Oh, I am not Admin again. I am just the robot following admin🤖</h1>
</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.cookies.get('admin') == '1000':
            return redirect('/story')
        
        username = request.form.get('username', '')
        password = request.form.get('password', '')
        
        if username and password:  # If both fields are filled
            resp = make_response(render_template_string(LOGIN_HTML, 
                   message="Do you think I will use admin:1000?"))
            resp.set_cookie('user', 'guest')
            return resp
    
    return render_template_string(LOGIN_HTML)

@app.route('/story')
def story():
    if request.cookies.get('admin') != '1000':
        return redirect('/')
    return render_template_string(STORY_HTML)


@app.route('/4dm1n')
def robot():
    return render_template_string(ROBOT_HTML)


@app.route('/4dm1n/robots.txt')
def robots_txt():
    # Flag is hidden here
    resp = make_response("User-agent: *\nDisallow: *\n\nCSECCTF{0k_y0u_w1n}")
    resp.headers['Content-Type'] = 'text/plain'
    return resp


if __name__ == '__main__':
    app.run(debug=True, port=8000)
