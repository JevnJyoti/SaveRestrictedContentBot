from flask import Flask
app= flask(__name__)

@app.route('/')
def  hello_world():
  return 'greymatters'


if __name__ == "__main__":
  app.run()
