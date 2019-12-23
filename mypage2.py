import web

urls = ("/", "index")

app = web.application(urls, globals())


class index:
    def GET(self):
        render = web.template.render('templates')
        input = web.input(name="Anonymous")
        return render.hello(input.name)


app.run()
