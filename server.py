"""
RUN with python server.py

Serves static files in the /static directory
"""
import web

urls = (
    '/(.*)', 'knowledgebase'
)
app = web.application(urls, globals())

class knowledgebase:
    pass

if __name__ == "__main__":
    app.run()
